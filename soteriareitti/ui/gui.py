""" soteriareitti/ui/gui.py """
import logging
import tkinter
import tkintermapview

from soteriareitti.core.app import SoteriaReitti
from soteriareitti.utils.geo import Location


class Gui:
    """ Graphical interface class """

    def __init__(self):
        self._app = SoteriaReitti("Töölö")
        self._source = None
        self._target = None

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

        if self._target:
            self._map_widget.delete_all_path()
            self._target = None
            self._source = None

        if not self._source:
            self._source = Location(*pos)
        else:
            self._target = Location(*pos)
            path = self._app._map.get_shortest_path(self._source, self._target)
            path = [node.location.as_tuple() for node in path]
            self._map_widget.set_path(path)

    def run(self):
        self._root.mainloop()
