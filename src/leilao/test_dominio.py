from typing import List
from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao


class TestLeilao(TestCase):
    def setUp(self) -> None:
        self.leilao = Leilao('Generic Auction')

    def simulate_auction_scenery(self, values: List[float] = None, bids: List[Lance] = None) -> None:
        if bids is None:
            bids = []

        if len(bids):
            for bid in bids:
                self.leilao.propoe(bid)

        else:
            for index, value in enumerate(values, start=1):
                user = Usuario(f'Generic User {index}')
                lance_user = Lance(user, value)
                self.leilao.propoe(lance_user)

    def test_should_return_the_lowest_and_highest_value_of_bids_when_added_in_ascending_order(self) -> None:
        self.simulate_auction_scenery(values=[100.0, 150.0])

        menor_valor_esperado = 100.0
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)

        maior_valor_esperado = 150.0
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_should_return_the_lowest_and_highest_value_of_bids_when_added_in_descending_order(self) -> None:
        self.simulate_auction_scenery(values=[150.0, 100.0])

        menor_valor_esperado = 100.0
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)

        maior_valor_esperado = 150.0
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_should_return_the_same_value_for_both_lowest_and_highest_when_added_only_a_bid(self) -> None:
        self.simulate_auction_scenery(values=[150.0])

        menor_valor_esperado = 150.0
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)

        maior_valor_esperado = 150.0
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_should_return_the_lowest_and_highest_when_added_more_than_two_bids(self) -> None:
        self.simulate_auction_scenery(values=[220.5, 100.0, 150.0])

        menor_valor_esperado = 100.0
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)

        maior_valor_esperado = 220.5
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_should_allow_propose_bid_if_there_is_none(self) -> None:
        self.simulate_auction_scenery(values=[120.45])
        quantidade_recebida_de_lances = len(self.leilao.lances)
        quantidade_esperada_de_lances = 1
        self.assertEqual(quantidade_esperada_de_lances, quantidade_recebida_de_lances)

    def test_should_allow_propose_bid_if_last_user_is_different(self) -> None:
        self.simulate_auction_scenery(values=[120.8, 143.9])
        quantidade_recebida_de_lances = len(self.leilao.lances)
        quantidade_esperada_de_lances = 2
        self.assertEqual(quantidade_esperada_de_lances, quantidade_recebida_de_lances)

    def test_should_not_allow_propose_bid_if_last_user_is_the_same(self) -> None:
        generic_user = Usuario('Generic User 1')
        try:
            bids = [Lance(generic_user, 150.55), Lance(generic_user, 200.46)]
            self.simulate_auction_scenery(bids=bids)
            self.fail(msg="Did not raise an error.")
        except ValueError:
            quantidade_recebida_de_lances = len(self.leilao.lances)
            quantidade_esperada_de_lances = 1
            self.assertEqual(quantidade_esperada_de_lances, quantidade_recebida_de_lances)
