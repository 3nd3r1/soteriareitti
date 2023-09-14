""" soteriareitti/ui/gui.py """
import logging
import tkinter
import tkintermapview

from soteriareitti.core.app import SoteriaReitti
from soteriareitti.utils.utils_geo import Location


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

        if self._source and self._target:
            self._source = None
            self._target = None
            self._map_widget.delete_all_marker()
            self._map_widget.delete_all_path()

        if not self._source:
            self._source = Location(pos[1], pos[0])
            self._map_widget.set_marker(pos[0], pos[1])
        else:
            self._target = Location(pos[1], pos[0])
            self._map_widget.set_marker(pos[0], pos[1])
            path = self._app.get_path(self._source, self._target)
            if path and len(path) > 1:
                path = [(node.location.latitude, node.location.longitude) for node in path]
                self._map_widget.set_path(path)

    def run(self):
        self._root.mainloop()
