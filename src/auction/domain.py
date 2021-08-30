import sys


class User:

    def __init__(self, name, wallet=500.0):
        self.__name = name
        self.__wallet = wallet

    @property
    def name(self):
        return self.__name

    @property
    def wallet(self):
        return self.__wallet

    def propose_bid(self, auction, value):
        if value > self.__wallet:
            raise ValueError(f'User tried to propose R${value} having only R${self.__wallet}.')

        bid = Bid(self, value)
        auction.propose(bid)

        self.__wallet -= value


class Bid:

    def __init__(self, user, value):
        self.user = user
        self.value = value


class Auction:

    def __init__(self, description):
        self.description = description
        self.__bids = []
        self.highest_bid = sys.float_info.min
        self.lowest_bid = sys.float_info.max

    def propose(self, bid: Bid):
        if not self.__bids or self.__bids[-1].user.name != bid.user.name and bid.value > self.__bids[
            -1].value:
            if bid.value > self.highest_bid:
                self.highest_bid = bid.value

            if bid.value < self.lowest_bid:
                self.lowest_bid = bid.value

            self.__bids.append(bid)
        else:
            raise ValueError("An error occurred on bid propose.")

    @property
    def bids(self):
        return self.__bids[:]
