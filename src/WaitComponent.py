from Component import *
import ComponentTypeConstants
import ComponentCategories
import ComponentHeaders

class WaitComponent(Component):
    name = 'Wait'
    type = ComponentTypeConstants.METHOD
    category = ComponentCategories.SYSTEM
    headers = [ComponentHeaders.SYSTEM]
    args = [] #array of tuples (name of arg, componentName)
    returnType = ComponentTypeConstants.NONE

    def parse(self, args):
        return 'system("PAUSE");'

