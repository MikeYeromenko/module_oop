from enum import Enum


START_LIVES = 5
START_ENEMY_LEVEL = 1


class AllowedAttacks(Enum):
    Wizard = '1'
    Warrior = '2'
    Bandit = '3'


class ListCommands(Enum):
    show_scores = 'show scores - this command shows the scores of all of the players'
    exit = 'exit - interrupts the game. If the quantity of your scores is more then 0, they will be saved'
    help = 'help - shows all the commands with their description'
    start = 'start - starts the game. This command works only once for one playing session'
