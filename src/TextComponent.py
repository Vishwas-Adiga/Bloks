from Component import *
import ComponentTypeConstants
import ComponentCategories
import ComponentHeaders

class TextComponent(Component):
    name = 'Text'
    type = ComponentTypeConstants.VARIABLE
    category = ComponentCategories.TEXT
    headers = []
    args = [] #array of tuples (name of arg, componentName)
    returnType = ComponentTypeConstants.STRING

    def parse(self, args):
        return

