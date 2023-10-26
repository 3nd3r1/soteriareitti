""" soteriareitti/ui/gui/mapview.py """
from typing import TYPE_CHECKING
import customtkinter
import tkintermapview

from soteriareitti.core.responder import Responder
from soteriareitti.core.station import Station
from soteriareitti.core.emergency import Emergency

from soteriareitti.classes.geo import Location
from soteriareitti.classes.graph import Path


if TYPE_CHECKING:
    from soteriareitti.ui.gui.gui import Gui


# pylint: disable-next=too-many-ancestors
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
        self._emergency_markers = {}
        self._responder_markers = {}
        self._station_markers = {}

        self.__create_map_widget()
        self.__create_search_widget()

    def __create_map_widget(self):
        self._map_widget = tkintermapview.TkinterMapView(master=self, corner_radius=0)
        self._map_widget.grid(row=1, rowspan=1, columnspan=3, sticky="nswe", padx=0, pady=0)

        self._map_widget.add_left_click_map_command(self.__update_new_emergency_location)

        self._map_widget.add_right_click_menu_command(
            "Create Responder", self.master.create_responder, pass_coords=True)
        self._map_widget.add_right_click_menu_command(
            "Create Station", self.master.create_station, pass_coords=True)

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

    def __update_new_emergency_location(self, pos: tuple):
        self.set_new_emergency_marker(Location(*pos))
        self.master.em_location.set(str(Location(*pos)))

    def set_responder_marker(self, responder: Responder):
        if responder in self._responder_markers:
            self._responder_markers[responder].set_position(
                responder.location.latitude, responder.location.longitude)
            return

        new_responder_marker = self._map_widget.set_marker(
            responder.location.latitude, responder.location.longitude,
            responder.type.value, marker_color_outside="#9BDCEA",
            marker_color_circle="#68929B")

        self._responder_markers[responder] = new_responder_marker

    def set_station_marker(self, station: Station):
        if station in self._station_markers:
            self._station_markers[station].set_position(
                station.location.latitude, station.location.longitude)
            return

        new_station_marker = self._map_widget.set_marker(
            station.location.latitude, station.location.longitude,
            station.type.value, marker_color_outside="#30B60E",
            marker_color_circle="#23880A")

        self._station_markers[station] = new_station_marker

    def set_emergency_marker(self, emergency: Emergency):
        if emergency in self._emergency_markers:
            self._emergency_markers[emergency].set_position(
                emergency.location.latitude, emergency.location.longitude)
            return
        new_emergency_marker = self._map_widget.set_marker(
            emergency.location.latitude, emergency.location.longitude,
            emergency.type.value, marker_color_outside="#F97554",
            marker_color_circle="#C05541")
        self._emergency_markers[emergency] = new_emergency_marker

    def set_new_emergency_marker(self, location: Location | None = None):
        if not location and self._new_emergency_marker:
            self._new_emergency_marker.delete()
            self._new_emergency_marker = None
            return

        if self._new_emergency_marker:
            self._new_emergency_marker.set_position(location.latitude, location.longitude)
        else:
            self._new_emergency_marker = self._map_widget.set_marker(
                location.latitude, location.longitude, "New Emergency",
                marker_color_outside="#FDAC61", marker_color_circle="#B07741")

    def clear_paths(self):
        self._map_widget.delete_all_path()

    def clear_markers(self):
        self._new_emergency_marker = None
        self._emergency_markers.clear()
        self._responder_markers.clear()
        self._station_markers.clear()
        self._map_widget.delete_all_marker()

    def draw_path(self, path: Path, color: str = "#FDAC61"):
        self._map_widget.set_path([node.location.as_tuple()
                                  for node in path], color=color)
