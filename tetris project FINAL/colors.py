class Colors: 
    white = (255, 255, 255)
    dark_grey = (157, 157, 158) 
    green = (6, 201, 45)
    red = (250, 27, 82)
    orange = (255, 139, 0)
    yellow = (254, 208, 0)
    purple = (181, 98, 248)
    cyan = (0, 234, 241)
    blue = (0, 167, 245)
    black = (0, 0, 0)
    darker_grey = (65, 65, 65)

    @classmethod # Allows you to define a method that can be called on a class rather than just one instance
    def get_cell_colors(cls): 
        return [cls.dark_grey, cls.orange, cls.blue, cls.cyan, cls.yellow, cls.green, cls.purple, cls.red] #the order is important as it will correspond to the ID of the block