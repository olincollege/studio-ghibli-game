"""

"""

class GhibliGameController:

    def __init__(self):
        pass

    @abstractmethod
    def move(self):
        pass

class KeyController(GhibliGameController):
    """
    Controls sprite with arrow keys and track state of arrow keys.
    """
    
    def move(self):
        pass

class AIController(GhibliGameController):
    """
    Control path of packages/obstacles.
    """

    def move(self):
        pass
