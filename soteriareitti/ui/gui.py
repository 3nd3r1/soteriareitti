""" soteriareitti/ui/gui.py """
import tkinter
import tkintermapview

from ui.ui import Ui
from soteriareitti.utils.utils_geo import Location


class Gui(Ui):
    """ Graphical interface class """

    def __init__(self):
        super().__init__()
        self._root = tkinter.Tk()
        self._root.geometry("800x600")
        self._root.title("SoteriaReitti")

        self._map_widget = tkintermapview.TkinterMapView(
            self._root, width=800, height=600, corner_radius=0)
        self._map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def run(self):
        self._root.mainloop()

    def create_marker(self, location: Location):
        self._map_widget.set_marker(location.latitude, location.longitude)
