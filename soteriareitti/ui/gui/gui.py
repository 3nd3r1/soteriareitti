""" soteriareitti/ui/gui.py """
import logging
import tkinter.messagebox
import customtkinter

from soteriareitti.ui.gui.mapview import MapView
from soteriareitti.ui.gui.sidebar import Sidebar

from soteriareitti.core.map import InvalidLocation
from soteriareitti.core.responder import ResponderType
from soteriareitti.core.station import StationType
from soteriareitti.core.emergency import EmergencyType, ResponderNotFound

from soteriareitti.classes.geo import Location

from soteriareitti.utils.settings import Settings
from soteriareitti.utils.file_reader import get_resources
from soteriareitti.utils.simulation import ResponderSimulator

from soteriareitti import SoteriaReitti


class Loader(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)

        customtkinter.CTkLabel(self, text="Loading...", font=("Ubuntu", 32)).grid(row=0, column=1)

    def hide(self):
        self.grid_forget()

    def show(self):
        self.grid(row=0, column=0, rowspan=2, columnspan=2, sticky="nsew")


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


class Gui(customtkinter.CTk):
    """ Graphical interface class """

    APP_TITLE = "SoteriaReitti"
    APP_PLACE = Settings.app_place
    APP_ICON = "icon.png"
    WIDTH = 1280
    HEIGHT = 720

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(Gui.APP_TITLE)
        self.geometry(f"{Gui.WIDTH}x{Gui.HEIGHT}")
        self.minsize(Gui.WIDTH, Gui.HEIGHT)
        self.iconphoto(False, tkinter.PhotoImage(file=get_resources(Gui.APP_ICON)))

        self.protocol("WM_DELETE_WINDOW", self.__on_closing)
        self.bind("<Command-q>", self.__on_closing)
        self.bind("<Command-w>", self.__on_closing)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Variables
        self.simulate_responders = customtkinter.BooleanVar()

        self.em_type = customtkinter.StringVar()
        self.em_location = customtkinter.StringVar()
        self.em_description = customtkinter.StringVar()
        self.em_responder_types = {k: customtkinter.BooleanVar() for k in ResponderType}

        # Other
        self._simulators = {}

        # App
        self.app = SoteriaReitti()

        # Widgets
        self._loader = Loader(master=self)
        self.map_view = MapView(master=self, address=Gui.APP_PLACE)
        self.sidebar = Sidebar(master=self)

    def __load_place(self):
        self.start_loading()
        self.app.load_place(Gui.APP_PLACE)
        self.stop_loading()

    def __on_closing(self, _event=0):
        self.destroy()

    def _update_simulation(self):
        if self.simulate_responders.get() and self.app:
            for simulator in self._simulators.values():
                simulator.update()
                self.map_view.set_responder_marker(simulator.responder)
        self.after(1000, self._update_simulation)

    def start_loading(self):
        logging.debug("Loading started")
        self.sidebar.grid_forget()
        self.map_view.grid_forget()
        self._loader.show()
        self.update()

    def stop_loading(self):
        logging.debug("Loading ended")
        self._loader.hide()
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.map_view.grid(row=0, column=1, sticky="nsew")
        self.update()

    def create_responder(self, pos: tuple):
        dialog = OptionDialog("Select Responder Type", "Create", [r.value for r in ResponderType])
        dialog_input = dialog.get_input()

        if not dialog_input:
            return

        self.start_loading()
        responder_type = ResponderType(dialog_input)

        try:
            new_responder = self.app.create_responder(
                responder_type, Location(pos[0], pos[1]))
        except InvalidLocation:
            self.stop_loading()
            tkinter.messagebox.showerror(title="Error", message="Invalid location")
            return

        self.map_view.set_responder_marker(new_responder)
        self._simulators[new_responder] = ResponderSimulator(new_responder)

        self.stop_loading()

    def create_station(self, pos: tuple):
        dialog = OptionDialog("Select Staton Type", "Create", [s.value for s in StationType])
        dialog_input = dialog.get_input()

        if not dialog_input:
            return

        self.start_loading()
        station_type = StationType(dialog_input)

        try:
            new_station = self.app.create_station(station_type, Location(pos[0], pos[1]))
        except InvalidLocation:
            self.master.stop_loading()
            tkinter.messagebox.showerror(title="Error", message="Invalid location")
            return

        self.map_view.set_station_marker(new_station)
        self.stop_loading()

    def create_emergency(self):
        self.start_loading()
        if not self.em_type.get() or self.em_location.get() == "":
            self.stop_loading()
            tkinter.messagebox.showerror(
                title="Error", message="Emergency type or location missing")
            return

        em_type = EmergencyType(self.em_type.get())
        em_responder_types = [k for k, v in self.em_responder_types.items() if v.get()]
        em_location = Location.from_str(self.em_location.get())
        em_description = self.em_description.get()

        try:
            emergency = self.app.create_emergency(
                em_type, em_responder_types, em_location, em_description)
        except ResponderNotFound:
            self.stop_loading()
            tkinter.messagebox.showerror(title="Error", message="No responders found")
            return

        self.map_view.set_emergency_marker(emergency)
        self.map_view.set_new_emergency_marker(None)

        for responder in emergency.responders:
            path_to_emergency = responder.path_to(emergency)
            self.map_view.draw_path(path_to_emergency)

        self.stop_loading()

    def run(self):
        self.after(10, self.__load_place)
        self.after(10, self._update_simulation)
        self.mainloop()

    def clear(self):
        self.app.clear()
        self.map_view.clear_paths()
        self.map_view.clear_markers()
        self._simulators.clear()
