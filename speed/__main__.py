from test import Test
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--length', type=int, default=100)
    args = parser.parse_args()

    test = Test()

    test.run(args.length)
