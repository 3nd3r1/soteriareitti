""" soteriareitti/ui/gui.py """
import customtkinter

from soteriareitti.ui.gui.mapview import MapView
from soteriareitti.ui.gui.sidebar import Sidebar

from soteriareitti import SoteriaReitti


class Gui(customtkinter.CTk):
    """ Graphical interface class """

    APP_TITLE = "SoteriaReitti"
    WIDTH = 1280
    HEIGHT = 720

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.app = SoteriaReitti("Töölö")

        self.title(Gui.APP_TITLE)
        self.geometry(f"{Gui.WIDTH}x{Gui.HEIGHT}")
        self.minsize(Gui.WIDTH, Gui.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.__on_closing)
        self.bind("<Command-q>", self.__on_closing)
        self.bind("<Command-w>", self.__on_closing)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.map_view = MapView(master=self, address="Töölö")
        self.sidebar = Sidebar(master=self)

    def __on_closing(self, _event=0):
        self.destroy()

    def run(self):
        self.mainloop()
