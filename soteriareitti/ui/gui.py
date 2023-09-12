""" soteriareitti/ui/gui.py """
import logging
import tkinter
import tkintermapview

from ui.ui import Ui
from soteriareitti.utils.utils_geo import Location


class Gui(Ui):
    """ Graphical interface class """

    def __init__(self):
        self._root = tkinter.Tk()
        self._root.geometry("800x600")
        self._root.title("SoteriaReitti")

        self._map_widget = tkintermapview.TkinterMapView(
            self._root, width=800, height=600, corner_radius=0)
        self._map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self._map_widget.set_address("Töölö, Helsinki, Finland")
        self.__initialize_events()
        super().__init__()

    def __initialize_events(self):
        self._map_widget.add_left_click_map_command(self.__on_left_click)

    def __on_left_click(self, pos: tuple):
        self._app.get_closest_node(Location(*pos))

    def run(self):
        self._root.mainloop()

    def create_marker(self, location: Location):
        logging.debug("Creating marker at %s", location)
        self._map_widget.set_marker(location.latitude, location.longitude)
