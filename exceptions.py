import models


class GameOver(Exception):
    def __init__(self, text, **kwargs):
        self.txt = text
        self.score = kwargs.get('score')
        self.name = kwargs.get('name')


class EnemyDown(Exception):
    pass
