from datetime import datetime


class GameOver(Exception):
    def __init__(self, text, **kwargs):
        self.txt = text
        self.score = kwargs.get('score')
        self.name = kwargs.get('name')
        print(self.txt)
        if self.score > 0:
            self.save_res()

    def save_res(self):
        with open('scores.txt', 'a') as source:
            source.write(f'{self.name} {self.score} {datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")}\n')


class EnemyDown(Exception):
    pass
