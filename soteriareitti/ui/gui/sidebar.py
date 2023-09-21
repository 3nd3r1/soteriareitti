""" soteriareitti/ui/gui/sidebar.py """
import customtkinter

from soteriareitti.core.emergency import EmergencyType
from soteriareitti.core.responder import ResponderType


class Sidebar(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master=master, width=250, *args, **kwargs)
        self.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self._title = customtkinter.CTkLabel(master=self, text="SoteriaReitti", font=("Ubuntu", 32))
        self._title.grid(row=0, column=0, columnspan=3, sticky="w", padx=5, pady=5)

        self._em_title = customtkinter.CTkLabel(
            master=self, text="New emergency:", font=("Ubuntu", 24))
        self._em_title.grid(row=1, column=0, columnspan=3, sticky="w", padx=5, pady=5)

        self._em_location_label = customtkinter.CTkLabel(
            master=self, text="Location:", font=("Ubuntu", 16))
        self._em_location_label.grid(row=2, column=0, columnspan=3, sticky="w", padx=5, pady=5)

        self._em_location = customtkinter.CTkLabel(
            master=self, textvariable=self.master.map_view.emergency_location_var, font=("Ubuntu", 16))
        self._em_location.grid(row=3, column=0, columnspan=3, sticky="w", padx=5, pady=5)

        self._em_type_label = customtkinter.CTkLabel(master=self, text="Type:", font=("Ubuntu", 16))
        self._em_type_label.grid(row=4, column=0, columnspan=3, sticky="w", padx=5, pady=5)

        self._em_type = customtkinter.CTkOptionMenu(
            master=self, values=[type.value for type in EmergencyType])
        self._em_type.grid(row=5, column=0, columnspan=3, sticky="w", padx=5, pady=5)

        self._em_description_label = customtkinter.CTkLabel(
            master=self, text="Description:", font=("Ubuntu", 16))
        self._em_description_label.grid(row=6, column=0, columnspan=3, sticky="w", padx=5, pady=5)

        self._em_description = customtkinter.CTkTextbox(master=self)
        self._em_description.grid(row=7, column=0, columnspan=3, sticky="w", padx=5, pady=5)

        self._em_responders_label = customtkinter.CTkLabel(
            master=self, text="Responders:", font=("Ubuntu", 16))
        self._em_responders_label.grid(row=8, column=0, columnspan=3, sticky="w", padx=5, pady=5)

        self._em_responders_vars = {}
        self._em_responders_checkboxes = {}

        column = 0
        for responder in ResponderType:
            variable = customtkinter.BooleanVar(value=False)
            checkbox = customtkinter.CTkCheckBox(master=self,
                                                 text=responder.value,
                                                 variable=variable)
            checkbox.grid(row=9, column=column, sticky="w", padx=5, pady=5)
            column += 1
            self._em_responders_vars[responder.value] = variable
            self._em_responders_checkboxes[responder.value] = checkbox

        self._em_submit = customtkinter.CTkButton(
            master=self, text="Create", command=self.create_emergency)
        self._em_submit.grid(row=10, column=0, columnspan=3, sticky="w", padx=5, pady=5)

    def create_emergency(self):
        em_type = self._em_type.get()
        em_responder_types = [k for k, v in self._em_responders_vars if v.get()]
        em_location = self.master.map_view.emergency_location_var.get()
        em_description = self._em_description.get("0.0", "end")
        self.master.app.create_emergency(em_type, em_responder_types, em_location, em_description)
