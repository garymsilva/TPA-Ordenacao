from model.Sort import Sort

class InsertionSort(Sort):
    
    def __init__(self, compareObject):
        super().__init__(compareObject)
        self.identifier("insertion-sort")
    #

    def sort(self, list):
        # TODO
        raise NotImplementedError
    #
#
