import ppapparse


if __name__ == '__main__':
    while True:
        try:
            s = input('PPAPScript> ')
        except EOFError:
            break
        ppapparse.parse(s)
