# ----------------------
# Made by Brady Hodge
# Status: In Progress
# Assignment 13B; 1/2
# Module
# ----------------------

class Treat:
    def __init__(self, name, flavor):
        self.treat_name = name
        self.treat_flavor = flavor
        self.calories = 0

    def getDescription(self):
        if self.calories > 0:
            return '{flavor}{name} - ({calorie} cal)'
        else:
            return '{flavor}{name}'

    class Taffy:
        def __init__(self, name, flavor):
            super().__init__(name, flavor)

    class Cookie:
        def __init__(self, name, flavor, calories):
            super().__init__(name, flavor)
            self.calories = calories

        class JumboCookie:
            def __init__(self, name, flavor, calories):
                super().__init__(name, flavor, calories)

            def getDescription(self):
                return '{} Jumbo {} ({} cal)'.format(self.flavor, self.name, self.calories)

    class Brownie:
        def __init__(self, calories, has_nuts):
            super().__init__('Brownie', 'Chocolate')
            self.has_nuts = has_nuts
            self.calories = calories

        def getDescription(self):
           nut_des = ''
           if self.has_nuts:
               nut_des = 'has nuts'
           return super().getDescription() + nut_des

    def get_inventory(self):
        return [ Taffy('Saltwater', 'Orange'), Cookie('Snickerdoo', 'Cinnamon', 200), JumboCookie('Monster Cookie', 'Chocolate', 300), Cookie('Grasshopper', 'mint', 175), Brownie(400, True), Treat('Chick-O-Stick', 'Peanut Butter'), Brownie(350, False)]

