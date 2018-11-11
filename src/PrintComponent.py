from Component import *
import ComponentTypeConstants
import ComponentCategories
import ComponentHeaders

class PrintComponent(Component):
    name = 'Print'
    type = ComponentTypeConstants.METHOD
    category = ComponentCategories.INTERFACE
    headers = [ComponentHeaders.IOSTREAM]
    args = ['text']

    def parse(self, args):
        return 'cout <<' + args[0]

