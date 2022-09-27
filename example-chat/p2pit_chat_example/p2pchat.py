from p2pit import Network


class Chat:
    """
    Multi-user chat client example
    """

    def __init__(self, bootstrap):
        """
        We create the network and connect to it.
        """
        self.network = Network()
        self.network.bootstrap(peers=bootstrap)

    def join(self):
        """
        Join a given chat channel.
        """
        self.network.connect(self.settings)

    def run_forever(self):
        pass

    def on_new_peer(self):
        """
        Called when a new peer
        """
