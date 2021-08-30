from typing import List
from unittest import TestCase

from src.auction.domain import User, Bid, Auction


class TestLeilao(TestCase):
    def setUp(self) -> None:
        self.auction = Auction('Generic Auction')

    def simulate_auction_scenery(self, values: List[float] = None, bids: List[Bid] = None) -> None:
        if bids is None:
            bids = []

        if len(bids):
            for bid in bids:
                self.auction.propose(bid)

        else:
            for index, value in enumerate(values, start=1):
                user = User(f'Generic User {index}')
                user_bid = Bid(user, value)
                self.auction.propose(user_bid)

    def test_should_return_the_lowest_and_highest_value_of_bids_when_added_in_ascending_order(self) -> None:
        self.simulate_auction_scenery(values=[100.0, 150.0])

        lowest_value_expected = 100.0
        self.assertEqual(lowest_value_expected, self.auction.lowest_bid)

        highest_value_expected = 150.0
        self.assertEqual(highest_value_expected, self.auction.highest_bid)

    def test_should_not_allow_bids_when_added_in_descending_order(self) -> None:
        with self.assertRaises(ValueError):
            self.simulate_auction_scenery(values=[150.0, 100.0])

    def test_should_return_the_same_value_for_both_lowest_and_highest_when_added_only_a_bid(self) -> None:
        self.simulate_auction_scenery(values=[150.0])

        lowest_value_expected = 150.0
        self.assertEqual(lowest_value_expected, self.auction.lowest_bid)

        highest_value_expected = 150.0
        self.assertEqual(highest_value_expected, self.auction.highest_bid)

    def test_should_return_the_lowest_and_highest_when_added_more_than_two_bids(self) -> None:
        self.simulate_auction_scenery(values=[100.0, 150.0, 220.5])

        lowest_value_expected = 100.0
        self.assertEqual(lowest_value_expected, self.auction.lowest_bid)

        highest_value_expected = 220.5
        self.assertEqual(highest_value_expected, self.auction.highest_bid)

    def test_should_allow_propose_bid_if_there_is_none(self) -> None:
        self.simulate_auction_scenery(values=[120.45])
        received_amount_of_bids = len(self.auction.bids)
        expected_amount_of_bids = 1
        self.assertEqual(expected_amount_of_bids, received_amount_of_bids)

    def test_should_allow_propose_bid_if_last_user_is_different(self) -> None:
        self.simulate_auction_scenery(values=[120.8, 143.9])
        received_amount_of_bids = len(self.auction.bids)
        expected_amount_of_bids = 2
        self.assertEqual(expected_amount_of_bids, received_amount_of_bids)

    def test_should_not_allow_propose_bid_if_last_user_is_the_same(self) -> None:
        generic_user = User('Generic User 1')

        with self.assertRaises(ValueError):
            bids = [Bid(generic_user, 150.55), Bid(generic_user, 200.46)]
            self.simulate_auction_scenery(bids=bids)
