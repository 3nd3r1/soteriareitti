""" soteriareitti/ui/gui.py """
import logging
import threading
import customtkinter

from soteriareitti.ui.gui.mapview import MapView
from soteriareitti.ui.gui.sidebar import Sidebar

from soteriareitti.utils.settings import Settings

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
    APP_PLACE = Settings.app_place
    WIDTH = 1280
    HEIGHT = 720

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(Gui.APP_TITLE)
        self.geometry(f"{Gui.WIDTH}x{Gui.HEIGHT}")
        self.minsize(Gui.WIDTH, Gui.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.__on_closing)
        self.bind("<Command-q>", self.__on_closing)
        self.bind("<Command-w>", self.__on_closing)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._loader = Loader(master=self)

        self.map_view = MapView(master=self, address=Gui.APP_PLACE)
        self.sidebar = Sidebar(master=self)

        self.app = SoteriaReitti()

    def __load_place(self):
        self.start_loading()
        self.app.load_place(Gui.APP_PLACE)
        self.stop_loading()

    def __on_closing(self, _event=0):
        self.destroy()

    def start_loading(self):
        logging.debug("Loading started")
        self.sidebar.grid_forget()
        self.map_view.grid_forget()
        self._loader.show()
        self.update()

    def stop_loading(self):
        logging.debug("Loading ended")
        self._loader.hide()
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.map_view.grid(row=0, column=1, sticky="nsew")
        self.update()

    def run(self):
        threading.Thread(target=self.__load_place).start()
        self.mainloop()

    def clear(self):
        self.app.clear()
        self.map_view.clear_paths()
        self.map_view.clear_markers()
