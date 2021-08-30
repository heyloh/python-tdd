import sys


class User:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


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
