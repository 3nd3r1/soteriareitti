""" soteriareitti/ui/gui/sidebar.py """
from typing import TYPE_CHECKING
from PIL import Image
import customtkinter

from soteriareitti.core.emergency import EmergencyType

from soteriareitti.utils.file_reader import get_resources

if TYPE_CHECKING:
    from soteriareitti.ui.gui.gui import Gui


# pylint: disable-next=too-many-ancestors
class Sidebar(customtkinter.CTkFrame):
    WIDTH = 325
    labels = [
        ("New Emergency:", 24, 1, 0, "w", 5, 5),
        ("Location:", 16, 2, 0, "w", 5, 5),
        ("Type:", 16, 4, 0, "w", 5, 5),
        ("Description:", 16, 6, 0, "w", 5, 5),
        ("Responders:", 16, 8, 0, "w", 5, 5),
    ]

    def __init__(self, master: "Gui", *args, **kwargs):
        super().__init__(master=master, width=Sidebar.WIDTH, *args, **kwargs)
        self.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        self.master: "Gui" = master

        self.__create_widgets()

    def __create_widgets(self):
        self.grid_rowconfigure(11, weight=1)
        # Logo
        logo_image = customtkinter.CTkImage(dark_image=Image.open(
            get_resources("logo.png")), size=(250, 65))
        customtkinter.CTkLabel(self, image=logo_image, text="", width=Sidebar.WIDTH).grid(
            row=0, column=0, sticky="w", padx=5, pady=5)

        # Labels
        for label in Sidebar.labels:
            customtkinter.CTkLabel(self, text=label[0], font=("Ubuntu", label[1])).grid(
                row=label[2], column=label[3], sticky=label[4],
                padx=label[5], pady=label[6])

        # Inputs
        customtkinter.CTkOptionMenu(self, variable=self.master.em_type,
                                    values=[k.value for k in EmergencyType],
                                    width=Sidebar.WIDTH).grid(
            row=5, column=0, sticky="w", padx=5, pady=5)
        customtkinter.CTkLabel(
            self, textvariable=self.master.em_location).grid(
            row=3, column=0, sticky="w", padx=5, pady=5)
        customtkinter.CTkEntry(
            self, textvariable=self.master.em_description, width=Sidebar.WIDTH).grid(
            row=7, column=0, sticky="w", padx=5, pady=5)
        div = customtkinter.CTkFrame(self, width=Sidebar.WIDTH)
        div.grid(row=9, column=0, sticky="w", padx=5, pady=5)
        for column, (key, value) in enumerate(self.master.em_responder_types.items()):
            customtkinter.CTkCheckBox(
                div, text=key.value, variable=value).grid(
                row=0, column=column,  sticky="w", padx=5, pady=5)

        # Create button
        customtkinter.CTkButton(
            self, text="Create", command=self.master.create_emergency, width=Sidebar.WIDTH).grid(
            row=10, column=0, sticky="w", padx=5, pady=5)

        # Clear and simulate responders
        div = customtkinter.CTkFrame(self, width=Sidebar.WIDTH)
        div.grid(row=12, column=0, sticky="w", padx=5, pady=5)

        customtkinter.CTkButton(
            div, text="Clear", command=self.master.clear).grid(
            row=0, column=0, columnspan=1, sticky="w", padx=5, pady=5)
        customtkinter.CTkSwitch(
            div, text="Simulate Responders",
            variable=self.master.simulate_responders).grid(
            row=0, column=1, columnspan=2, sticky="w", padx=5, pady=5)
