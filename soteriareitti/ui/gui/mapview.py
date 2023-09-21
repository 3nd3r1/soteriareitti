""" soteriareitti/ui/gui/mapview.py """
import customtkinter
import tkintermapview

from soteriareitti.utils.geo import Location


class LocationVar(customtkinter.Variable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self) -> Location | None:
        value = self._tk.globalgetvar(self._name)
        if isinstance(value, Location):
            return value
        return None


class MapView(customtkinter.CTkFrame):
    def __init__(self, master: customtkinter.CTk, address: str, *arg, **kwargs):
        super().__init__(master, *arg, **kwargs)

        self.grid(row=0, column=1, rowspan=1, padx=0, pady=0, sticky="nsew")

        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)

        self.emergency_location_var = LocationVar(value=None)

        self._map_widget = tkintermapview.TkinterMapView(master=self, corner_radius=0)
        self._map_widget.grid(row=1, rowspan=1, columnspan=3, sticky="nswe", padx=0, pady=0)

        self._map_widget.add_left_click_map_command(self.set_emergency_location)

        self._map_widget.set_address(address)

    def set_emergency_location(self, pos: tuple):
        self.emergency_location_var.set(Location(*pos))

        self._map_widget.delete_all_marker()
        self._map_widget.set_marker(pos[0], pos[1], "New Emergency")
