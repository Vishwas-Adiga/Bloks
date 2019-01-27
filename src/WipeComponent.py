from Component import *
import ComponentTypeConstants
import ComponentCategories
import ComponentHeaders

class WipeComponent(Component):
    name = 'Wipe'
    type = ComponentTypeConstants.METHOD
    category = ComponentCategories.SYSTEM
    headers = [ComponentHeaders.SYSTEM]
    args = [] #array of tuples (name of arg, componentName)
    returnType = ComponentTypeConstants.NONE

    def parse(self, args):
        return 'system("CLEAR");'

