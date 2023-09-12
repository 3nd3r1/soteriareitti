""" soteriareitti/ui/gui.py """
import logging
import tkinter
import tkintermapview

from core.app import SoteriaReitti
from utils.utils_geo import Location


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

        closest_node = self._app.get_closest_node(Location(pos[1], pos[0]))

        if closest_node and closest_node.lon and closest_node.lat:
            logging.debug("Closest node: %s", closest_node)

            node_location = Location(float(closest_node.lon), float(closest_node.lat))
            self._map_widget.set_marker(node_location.latitude, node_location.longitude)

    def run(self):
        self._root.mainloop()
