class Colors: 
    dark_grey = (157, 157, 158) 
    green = (204, 255, 153)
    red = (255, 153, 153)
    orange = (255, 204, 153)
    yellow = (255, 255, 153)
    purple = (153, 153, 255)
    cyan = (153, 255, 255)
    blue = (153, 204, 255)

    @classmethod # Allows you to define a method that can be called on a class rather than just one instance
    def get_cell_colors(cls): 
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue] #the order is important as it will correspond to the ID of the block