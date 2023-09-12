""" soteriareitti/ui/gui.py """
import logging
import tkinter
import tkintermapview

from core.app import SoteriaReitti
from utils.utils_geo import GeoUtils, Location, Distance


class Gui:
    """ Graphical interface class """

    def __init__(self):
        self._app = SoteriaReitti()
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
        logging.debug("Left click at %s", pos)
        bounding_box = GeoUtils.calculate_bbox(Location(*pos), Distance(100))

        self._map_widget.set_polygon(bounding_box.as_polygon())

    def run(self):
        self._root.mainloop()
