from game import PongGame


def main():
    pong = PongGame(640, 480)
    pong.run()


if __name__ == "__main__":
    main()
else:
    raise Exception("This module cannot be imported.")
