import abc

class Sort(abc.ABC):
    def __init__(self, compareObject):
        self.compareObject = compareObject
    #

    @property # This allows to handle the object attribute like this: mySortObject.identifier
    def identifier(self):
        return self._identifier
    #

    @identifier.setter
    def identifier(self, identifier):
        self._identifier = identifier
    #

    @property
    def compareObject(self, compareObject):
        self._compareObject = compareObject
    #

    @abc.abstractmethod
    def sort(self, list):
        pass
    #
#
