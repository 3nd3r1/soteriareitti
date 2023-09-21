"""
tests/helpers.py
This file contains helper functions for the tests
"""


import tkinter
import tkintermapview


def draw_path(path, place="Töölö"):
    root = tkinter.Tk()
    root.geometry("800x600")
    root.title("SoteriaReitti")

    map_widget = tkintermapview.TkinterMapView(root, width=800, height=600, corner_radius=0)
    map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    map_widget.set_address(place)

    map_widget.set_path([node.location.as_tuple() for node in path])
    root.mainloop()
