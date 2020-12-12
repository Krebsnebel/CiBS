class HighlightObject:

    def __init__(self, imgObj, pos):
        self.imgObj = imgObj
        self.position = pos

    def getPosition(self):
        return self.position

    def getImgObj(self):
        return self.imgObj
