""" soteriareitti/ui/ui.py """

from abc import ABC, abstractmethod

from core.app import SoteriaReitti
from utils.utils_geo import Location


class Ui(ABC):
    def __init__(self):
        """ Abstract class for all userinterfaces """
        self._app = SoteriaReitti(self)

    @abstractmethod
    def run(self):
        """ Method used for running the ui """

    @abstractmethod
    def create_marker(self, location: Location):
        """ Methods used for creating a marker on the ui"""
