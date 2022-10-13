from importlib.resources import path


class Character:
    def __init__(self,chemin,animated:bool=False):
        self.chemin = chemin
        