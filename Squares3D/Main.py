from MainClass import MainClass

WINDOW_W = 800
WINDOW_H = 600


def main():

    game = MainClass(WINDOW_W, WINDOW_H, "you_win.ogg")

    while True:
        game.eventLoopProcessing()

        game.checkWinCondition()

        game.drawGame()


if __name__ == '__main__': main()

