""" soteriareitti/ui/gui/sidebar.py """
from typing import TYPE_CHECKING
import customtkinter

from soteriareitti.core.emergency import EmergencyType
from soteriareitti.core.responder import ResponderType

from soteriareitti.utils.geo import Location

if TYPE_CHECKING:
    from soteriareitti.ui.gui.gui import Gui


class Sidebar(customtkinter.CTkFrame):
    labels = [
        ("SoteriaReitti", 32, 0, 0, 3, "w", 5, 5),
        ("New Emergency:", 24, 1, 0, 3, "w", 5, 5),
        ("Location:", 16, 2, 0, 3, "w", 5, 5),
        ("Type:", 16, 4, 0, 3, "w", 5, 5),
        ("Description:", 16, 6, 0, 3, "w", 5, 5),
        ("Responders:", 16, 8, 0, 3, "w", 5, 5),
    ]

    def __init__(self, master: "Gui", *args, **kwargs):
        super().__init__(master=master, width=250, *args, **kwargs)
        self.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.master: "Gui" = master
        self.em_type = customtkinter.StringVar()
        self.em_location = customtkinter.StringVar()
        self.em_description = customtkinter.StringVar()
        self.em_responder_types = {k: customtkinter.BooleanVar() for k in ResponderType}

        self.__create_widgets()

    def __create_widgets(self):
        # Labels
        for label in Sidebar.labels:
            customtkinter.CTkLabel(self, text=label[0], font=("Ubuntu", label[1])).grid(
                row=label[2], column=label[3], columnspan=label[4], sticky=label[5],
                padx=label[6], pady=label[7])

        # Inputs
        customtkinter.CTkOptionMenu(
            self, variable=self.em_type, values=[k.value for k in EmergencyType]).grid(
            row=5, column=0, columnspan=3, sticky="w", padx=5, pady=5)
        customtkinter.CTkLabel(
            self, textvariable=self.em_location).grid(
            row=3, column=0, columnspan=3, sticky="w", padx=5, pady=5)
        customtkinter.CTkEntry(
            self, textvariable=self.em_description, width=200).grid(
            row=7, column=0, columnspan=3, sticky="w", padx=5, pady=5)

        column = 0
        for key, value in self.em_responder_types.items():
            customtkinter.CTkCheckBox(
                self, text=key.value, variable=value).grid(
                row=9, column=column, columnspan=1, sticky="w", padx=5, pady=5)
            column += 1

        customtkinter.CTkButton(
            self, text="Create", command=self.create_emergency).grid(
            row=10, column=0, columnspan=3, sticky="w", padx=5, pady=5)

    def create_emergency(self):
        self.master.event_generate("<<LoadingStart>>")
        self.master.update()
        em_type = EmergencyType(self.em_type.get())
        em_responder_types = [k for k, v in self.em_responder_types.items() if v.get()]
        em_location = Location.from_str(self.em_location.get())
        em_description = self.em_description.get()

        emergency = self.master.app.create_emergency(
            em_type, em_responder_types, em_location, em_description)

        self.master.map_view.clear_paths()

        for responder in emergency.responders:
            path_to_emergency = responder.path_to(emergency.location)
            self.master.map_view.draw_path(path_to_emergency, "#FF0000")

        for station in emergency.stations_from:
            path_to_emergency = station.path_to(emergency.location)
            self.master.map_view.draw_path(path_to_emergency, "#0000FF")

        self.master.event_generate("<<LoadingEnd>>")
