import exceptions
import models
import settings


def play():
    """
    creating players
    :return:
    """
    print("Please, enter your name: ", end='')
    name = input()
    level = settings.START_ENEMY_LEVEL
    player = models.Player(name)
    enemy = models.Enemy(level)
    command = ''
    while command != 'start':
        print("To start the game enter 'start' here: ", end='')
        command = input()
        player.verify_commands(command)
    while True:
        try:
            print(player.attack(enemy))
            print(player.defence(enemy))
        except exceptions.EnemyDown:
            player.scores_up(5)
            level += 1
            enemy = models.Enemy(level)
            print(f'Enemy down. \n'
                  f'Going to LEVEL {level}. Player has {player.lives} lives from {settings.START_LIVES} and'
                  f' {player.score} scores.')
    return None


def main():
    """
    description
    :return:
    """

    try:
        play()
    except exceptions.GameOver as g_over:
        print(f'Game over, {g_over.name}. You have {g_over.score} scores.')
    except KeyboardInterrupt:
        pass
    finally:
        print('Goodbye')


if __name__ == '__main__':
    main()
