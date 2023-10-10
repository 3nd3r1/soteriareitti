""" soteriareitti/ui/gui/mapview.py """
from typing import TYPE_CHECKING
import customtkinter
import tkintermapview

from soteriareitti.core.responder import ResponderType
from soteriareitti.core.station import StationType

from soteriareitti.classes.geo import Location
from soteriareitti.classes.graph import Path

from soteriareitti.utils.simulation import ResponderSimulator

if TYPE_CHECKING:
    from soteriareitti.ui.gui.gui import Gui


class OptionDialog(customtkinter.CTkToplevel):
    def __init__(self, title: str, button_text: str, options: list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x500")
        self.minsize(500, 500)

        self.title(title)
        self.lift()
        self.attributes("-topmost", True)
        self.protocol("WM_DELETE_WINDOW", self.__on_closing)
        self.after(10, self.__create_widgets)
        self.resizable(False, False)
        self.grab_set()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=1)

        self.__title = title
        self.__button_text = button_text
        self.__options = options

        self.__value = None
        self.__variable = customtkinter.StringVar(master=self)

    def __create_widgets(self):
        customtkinter.CTkLabel(self, text=self.__title, font=(
            "Ubuntu", 32)).grid(row=1, column=1, pady=10)
        customtkinter.CTkOptionMenu(self, variable=self.__variable,
                                    values=self.__options).grid(row=2, column=1, pady=10)
        customtkinter.CTkButton(self, text=self.__button_text,
                                command=self.__on_submit).grid(row=3, column=1, pady=10)

    def __on_submit(self, _event=0):
        self.__value = self.__variable.get()
        self.__on_closing()

    def __on_closing(self, _event=0):
        self.grab_release()
        self.destroy()

    def get_input(self) -> str:
        self.master.wait_window(self)
        return self.__value


class MapView(customtkinter.CTkFrame):
    def __init__(self, master: "Gui", address: str, *arg, **kwargs):
        super().__init__(master, *arg, **kwargs)

        self.grid(row=0, column=1, rowspan=1, padx=0, pady=0, sticky="nsew")

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)

        self.master: "Gui" = master
        self.address_var = customtkinter.StringVar(value=address)

        self._new_emergency_marker = None
        self._responder_markers = {}
        self._station_markers = {}

        self.simulate_responders = customtkinter.BooleanVar(value=False)
        self.responder_simulators = {}
        self.master.after(0, self._update_simulation)

        self.__create_map_widget()
        self.__create_search_widget()

    def __create_map_widget(self):
        self._map_widget = tkintermapview.TkinterMapView(master=self, corner_radius=0)
        self._map_widget.grid(row=1, rowspan=1, columnspan=3, sticky="nswe", padx=0, pady=0)

        self._map_widget.add_left_click_map_command(self.set_emergency_location)

        self._map_widget.add_right_click_menu_command(
            "Create Responder", self._create_responder, pass_coords=True)
        self._map_widget.add_right_click_menu_command(
            "Create Station", self._create_station, pass_coords=True)

        self._map_widget.set_address(self.address_var.get())

    def __create_search_widget(self):
        search_entry = customtkinter.CTkEntry(master=self, placeholder_text="Address..",
                                              textvariable=self.address_var)
        search_entry.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        search_entry.bind("<Return>", self.__update_address)

        search_button = customtkinter.CTkButton(master=self, text="Search", width=90,
                                                command=self.__update_address)
        search_button.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)

    def __update_address(self, _event=None):
        self._map_widget.set_address(self.address_var.get())

    def _update_simulation(self):
        if self.simulate_responders.get() and self.master.app:
            for responder_simulator in self.responder_simulators.values():
                responder_simulator.update()
                pos = responder_simulator.responder.location.as_tuple()
                self._responder_markers[responder_simulator.responder].set_position(pos[0], pos[1])
        self.master.after(1000, self._update_simulation)

    def _create_responder(self, pos: tuple):
        dialog = OptionDialog("Select Responder Type", "Create", [r.value for r in ResponderType])
        dialog_input = dialog.get_input()

        if not dialog_input:
            return

        self.master.start_loading()
        responder_type = ResponderType(dialog_input)

        new_responder = self.master.app.create_responder(responder_type, Location(pos[0], pos[1]))
        new_marker = self._map_widget.set_marker(pos[0], pos[1], responder_type.value)
        self._responder_markers[new_responder] = new_marker
        self.responder_simulators[new_responder] = ResponderSimulator(
            self.master.app.map, new_responder)
        self.master.stop_loading()

    def _create_station(self, pos: tuple):
        dialog = OptionDialog("Select Staton Type", "Create", [s.value for s in StationType])
        dialog_input = dialog.get_input()

        if not dialog_input:
            return

        self.master.start_loading()
        station_type = StationType(dialog_input)

        new_station = self.master.app.create_station(station_type, Location(pos[0], pos[1]))
        new_marker = self._map_widget.set_marker(pos[0], pos[1], station_type.value,
                                                 marker_color_circle="#0000FF")

        self._station_markers[new_station] = new_marker
        self.master.stop_loading()

    def set_emergency_location(self, pos: tuple):
        self.master.sidebar.em_location.set(str(Location(pos[0], pos[1])))

        if self._new_emergency_marker:
            self._new_emergency_marker.set_position(pos[0], pos[1])
        else:
            self._new_emergency_marker = self._map_widget.set_marker(
                pos[0], pos[1], "New Emergency")

    def clear_paths(self):
        self._map_widget.delete_all_path()

    def clear_markers(self):
        self._new_emergency_marker = None
        self._responder_markers.clear()
        self._station_markers.clear()
        self._map_widget.delete_all_marker()

    def draw_path(self, path: Path, color: str = "#0000FF"):
        self._map_widget.set_path([node.location.as_tuple()
                                  for node in path], color=color)
