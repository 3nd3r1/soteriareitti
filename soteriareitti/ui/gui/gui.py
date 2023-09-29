""" soteriareitti/ui/gui.py """
import logging
import customtkinter

from soteriareitti.ui.gui.mapview import MapView
from soteriareitti.ui.gui.sidebar import Sidebar

from soteriareitti import SoteriaReitti


class Loader(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)

        customtkinter.CTkLabel(self, text="Loading...", font=("Ubuntu", 32)).grid(row=0, column=1)

    def hide(self):
        self.grid_forget()

    def show(self):
        self.grid(row=0, column=0, rowspan=2, columnspan=2, sticky="nsew")


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

        self.bind("<<LoadingStart>>", self.__on_loading_start)
        self.bind("<<LoadingEnd>>", self.__on_loading_end)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.map_view = MapView(master=self, address="Töölö")
        self.sidebar = Sidebar(master=self)

        self._loader = Loader(master=self)

    def __on_loading_start(self, _event=0):
        logging.debug("Loading started")
        self.sidebar.grid_forget()
        self.map_view.grid_forget()
        self._loader.show()

    def __on_loading_end(self, _event=0):
        logging.debug("Loading ended")
        self._loader.hide()
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.map_view.grid(row=0, column=1, sticky="nsew")

    def __on_closing(self, _event=0):
        self.destroy()

    def run(self):
        self.mainloop()
