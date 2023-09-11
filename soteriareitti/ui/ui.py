""" soteriareitti/ui/ui.py """
import logging
import tkinter
import tkintermapview

from core.app import SoteriaReitti


class Ui:
    def __init__(self):
        self._app = SoteriaReitti()

        self._root = tkinter.Tk()
        self._root.geometry("800x600")
        self._root.title("SoteriaReitti")

        self._map_widget = tkintermapview.TkinterMapView(
            self._root, width=800, height=600, corner_radius=0)
        self._map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.__init_event_listeners()

    def __init_event_listeners(self):
        self._map_widget.add_left_click_map_command(self._on_map_left_click)

    def _on_map_left_click(self, pos):
        closest_node = self._app.get_closest_node(pos)
        logging.debug(closest_node)

    def run(self):
        self._root.mainloop()
