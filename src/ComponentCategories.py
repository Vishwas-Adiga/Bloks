import client.assets.icons.IconsManager as Icons

SYSTEM = {'id': 1, 'name': 'System', 'icon': Icons.systemCategory(30, 30)}
LOGIC = {'id': 2, 'name': 'Logic', 'icon': Icons.logicCategory(30, 30)}
MATH = {'id': 3, 'name': 'Math', 'icon': Icons.mathCategory(30, 30)}
CONTROL = {'id': 4, 'name': 'Control', 'icon': Icons.controlCategory(30, 30)}
INTERFACE = {'id': 5, 'name': 'Interface', 'icon': Icons.interfaceCategory(30, 30)}

def getCategories():
    return [SYSTEM, LOGIC, MATH, CONTROL, INTERFACE]
