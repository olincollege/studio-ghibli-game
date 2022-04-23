"""
Display home/start screen, background of game, win/death screen, scores.
"""

class GhibliGameView:

    def __init__(self):
        pass

    @abstractmethod
    def display(self):
        pass

class GraphicsView(GhibliGameView):

    def display(self):
        pass