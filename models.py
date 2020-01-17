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
    def __init__(self, name):
        self.name = name
        self.lives = settings.START_LIVES
        self.score = 0

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

    def verify_commands(self, command, **kwargs):
        if command == 'show scores':
            self.show_scores()
        elif command == 'exit':
            self.exit_func()
        elif command == 'help':
            self.help_func()
        # elif command == 'start':
        #     self.start_game(**kwargs)
        return None

    # def start_game(self, **kwargs):
    #     self.lives = settings.START_LIVES
    #     self.score = 0
    #     kwargs['enemy_arg'].level = settings.START_ENEMY_LEVEL
    #     kwargs['enemy_arg'].lives = settings.START_ENEMY_LEVEL
    #     return None

    @staticmethod
    def help_func():
        for element in settings.ListCommands:
            print(element.value)
        return None

    def exit_func(self):
        raise exceptions.GameOver('You stopped the game', score=self.score, name=self.name)

    @staticmethod
    def show_scores():
        with open('scores.txt') as source:
            print(source.read())
        # return None

    def choose_hero(self, action):
        command = 0
        while [var.value for var in settings.AllowedAttacks].count(command) < 1:
            print(f'Choose your {action}. Enter \n'
                  '1 for Wizard \n'
                  '2 for Warrior \n'
                  '3 for Bandit \n'
                  'here: ', end='')
            command = input()
            self.verify_commands(command)
        return command

    def attack(self, enemy_obj: Enemy):
        """

        :param enemy_obj:
        :return:
        """
        result = "You missed!"
        player_attack = self.choose_hero('attack')
        var_result = self.fight(player_attack, enemy_obj.select_attack())

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
        player_defence = self.choose_hero('defence')
        result_attack = self.fight(enemy_obj.select_attack(), player_defence)

        if result_attack == 0:
            result = "It's a draw!"
        elif result_attack == 1:
            result = "Enemy hits you!"
            self.decrease_lives()

        return result

    @staticmethod
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

