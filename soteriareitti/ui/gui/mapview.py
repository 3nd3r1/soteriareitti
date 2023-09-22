""" soteriareitti/ui/gui/mapview.py """
import customtkinter
import tkintermapview

from soteriareitti.core.responder import ResponderType
from soteriareitti.core.station import StationType
from soteriareitti.utils.geo import Location
from soteriareitti.utils.graph import Path


class MapView(customtkinter.CTkFrame):
    def __init__(self, master, address: str, *arg, **kwargs):
        super().__init__(master, *arg, **kwargs)

        self.grid(row=0, column=1, rowspan=1, padx=0, pady=0, sticky="nsew")

        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)

        self._map_widget = tkintermapview.TkinterMapView(master=self, corner_radius=0)
        self._map_widget.grid(row=1, rowspan=1, columnspan=3, sticky="nswe", padx=0, pady=0)

        self._map_widget.add_left_click_map_command(self.set_emergency_location)

        self._map_widget.add_right_click_menu_command(
            "Create ambulance", self._create_ambulance, pass_coords=True)
        self._map_widget.add_right_click_menu_command(
            "Create hospital", self._create_hospital, pass_coords=True)

        self._map_widget.set_address(address)

        self._new_emergency_marker = None

    def _create_ambulance(self, pos: tuple):
        self.master.app.create_responder(ResponderType.AMBULANCE, Location(pos[0], pos[1]))
        self._map_widget.set_marker(pos[0], pos[1], "Ambulance")

    def _create_hospital(self, pos: tuple):
        self.master.app.create_station(StationType.HOSPITAL, Location(pos[0], pos[1]))
        self._map_widget.set_marker(pos[0], pos[1], "Hospital")

    def set_emergency_location(self, pos: tuple):
        self.master.sidebar.em_location.set(Location(pos[0], pos[1]))

        if self._new_emergency_marker:
            self._new_emergency_marker.set_position(pos[0], pos[1])
        else:
            self._new_emergency_marker = self._map_widget.set_marker(
                pos[0], pos[1], "New Emergency")

    def draw_path(self, path: Path):
        self._map_widget.delete_all_path()
        self._map_widget.set_path([node.location.as_tuple() for node in path])
