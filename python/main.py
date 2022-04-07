import logging

from tournament import Tournament
import argparse

def configure_arguments():
    parser = argparse.ArgumentParser(description="Flip a switch by setting a flag")
    parser.add_argument('-v', action='store_true')
    return parser.parse_args()

def configure_logging(verbose: bool): 
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARN)

if __name__ == '__main__':
    args = configure_arguments()
    configure_logging(args.v)
    tournament = Tournament()
    tournament.start()
