import pytest
from pytest import raises

from src.auction.domain import User, Auction


@pytest.fixture
def generic_user():
    return User('Generic User', 100.0)


@pytest.fixture
def auction():
    return Auction('Generic Auction')


def test_should_subtract_value_from_user_wallet_when_proposing_a_bid(generic_user, auction):
    generic_user.propose_bid(auction, 50.0)
    assert generic_user.wallet == 50.0


def test_should_allow_propose_bid_when_the_value_is_equal_to_the_value_on_wallet(generic_user, auction):
    generic_user.propose_bid(auction, 100.0)
    assert generic_user.wallet == 0.0


def test_should_not_allow_propose_bid_when_the_value_is_higher_than_the_value_on_wallet(generic_user, auction):
    with raises(ValueError):
        generic_user.propose_bid(auction, 150.0)
