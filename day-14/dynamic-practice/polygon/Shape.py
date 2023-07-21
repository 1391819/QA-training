# imports
from abc import ABC, abstractclassmethod


# Shape class - parent
class Shape(ABC):
    # forcing the writing of these two methods in any subclass
    @abstractclassmethod
    def get_area(self):
        pass

    @abstractclassmethod
    def get_perimeter(self):
        pass
