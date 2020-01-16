from random import randint

import exceptions
import settings


class Enemy:
    def __init__(self, level):
        self.level = level
        self.lives = level

    def update_level(self, level):
        if level > self.level:
            self.level = level
            self.lives = level

    def decrease_lives(self):
        self.lives -= 1
        if self.lives <= 0:
            raise exceptions.EnemyDown('Enemy died')
        return self.lives

    @staticmethod
    def select_attack():
        return str(randint(1, 3))


class Player:
    def __init__(self, name, allowed_attacks=['1', '2', '3']):
        self.name = name
        self.lives = settings.START_LIVES
        self.score = 0
        self.allowed_attacks = allowed_attacks

    def decrease_lives(self):
        self.lives -= 1
        if self.lives <= 0:
            raise exceptions.GameOver('Player died', score=self.score, name=self.name)
        return self.lives

    def scores_up(self, delta=1):
        """
        increasing scores, depending upon the reasons of winning
        +1 to scores when winning one batle
        +5 to scores when enemy died
        :param delta:
        :return:
        """
        self.score += delta
        return self.score

    def attack(self, enemy_obj: Enemy):
        """

        :param enemy_obj:
        :return:
        """
        result = "You missed!"
        player_attack = 0

        while not (self.allowed_attacks.count(player_attack)):
            print('Choose your attack. Enter \n'
                  '1 for Wizard \n'
                  '2 for Warrior \n'
                  '3 for Bandit \n'
                  'here: ', end='')
            player_attack = input()

        var_result = fight(player_attack, enemy_obj.select_attack())

        if var_result == 0:
            result = "It's a draw!"
        elif var_result == 1:
            result = "You attacked successfully!"
            self.scores_up()
            enemy_obj.decrease_lives()

        return result

    def defence(self, enemy_obj: Enemy):
        """

        :param enemy_obj:
        :return:
        """
        result = "You defenced successfully!"
        player_defence = 0
        list_defences = ['1', '2', '3']

        while not (list_defences.count(player_defence)):
            print('Choose your defence. Enter \n'
                  '1 for Wizard \n'
                  '2 for Warrior \n'
                  '3 for Bandit \n'
                  'here: ', end='')
            player_defence = input()

        result_attack = fight(enemy_obj.select_attack(), player_defence)

        if result_attack == 0:
            result = "It's a draw!"
        elif result_attack == 1:
            result = "Enemy hits you!"
            self.decrease_lives()

        return result


def fight(attack, defense):
    """
    win if 1>2, 2>3, 3>1
    :param attack:
    :param defense:
    :return:
    """
    result = -1
    if attack == defense:
        result = 0
    elif (attack == '1' and defense == '2') or (attack == '2' and defense == '3') or (attack == '3' and defense == '1'):
        result = 1

    return result
