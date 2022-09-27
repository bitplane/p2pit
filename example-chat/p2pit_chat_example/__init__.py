from argparse import ArgumentParser
from sys import argv

from oslo_utils.netutils import parse_host_port

from .p2pchat import Chat


def parse_args(args: dict) -> dict:
    """
    Parses the command line arguments.
    Might also quit the process, if you pass -h
    """

    parser = ArgumentParser("Starts a multi-user chat client")
    parser.add_argument("-b", "--bootstrap", default="router.bittorrent.com:6881")

    args = parser.parse_args(args)

    args.bootstrap = [parse_host_port(host) for host in args.bootstrap.split(",")]

    return args


def main(args: dict = argv[1:]):
    """
    Starts the chat client
    """
    args = parse_args(args)
    chat = Chat(bootstrap=args["bootstrap"])
    chat.connect()
    chat.run_forever()
