from CivEnums.ENote import ENote


"""
with it all properties of marker can be defined
* marker type
* resource
* visibility
"""


class Marker:

    def __init__(self, mtype, res):
        self.markerType = mtype
        self.resource = res
        if mtype == ENote.RESOURCE:
            self.visibility = True
        else:
            self.visibility = False

    def getSign(self):
        return self.markerType.getSign()

    def getType(self):
        return self.markerType
