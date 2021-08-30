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
        self.highest_bid = 0.0
        self.lowest_bid = 0.0

    def propose(self, bid: Bid):
        if self._is_bid_invalid(bid):
            raise ValueError("An error occurred on bid propose.")

        if not self._has_bids():
            self.lowest_bid = bid.value

        self.highest_bid = bid.value
        self.__bids.append(bid)

    def _has_bids(self):
        return self.__bids

    def _is_bid_invalid(self, bid):
        return self.__bids and (
                self._is_the_same_user(bid)
                or self._is_bid_lower(bid)
        )

    def _is_the_same_user(self, bid):
        return self.__bids[-1].user.name == bid.user.name

    def _is_bid_lower(self, bid):
        return bid.value <= self.__bids[-1].value

    @property
    def bids(self):
        return self.__bids[:]
