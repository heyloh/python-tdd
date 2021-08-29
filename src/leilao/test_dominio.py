from typing import List
from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao


class TestAvaliador(TestCase):
    def setUp(self) -> None:
        self.leilao = Leilao('Generic Auction')

    def simulate_auction_scenery(self, values: List[float]) -> None:
        for index, value in enumerate(values, start=1):
            user = Usuario(f'Generic User {index}')
            lance_user = Lance(user, value)
            self.leilao.propoe(lance_user)

    def test_should_return_the_lowest_and_highest_value_of_bids_when_added_in_ascending_order(self) -> None:
        self.simulate_auction_scenery([100.0, 150.0])

        menor_valor_esperado = 100.0
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)

        maior_valor_esperado = 150.0
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_should_return_the_lowest_and_highest_value_of_bids_when_added_in_descending_order(self) -> None:
        self.simulate_auction_scenery([150.0, 100.0])

        menor_valor_esperado = 100.0
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)

        maior_valor_esperado = 150.0
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_should_return_the_same_value_for_both_lowest_and_highest_when_added_only_a_bid(self) -> None:
        self.simulate_auction_scenery([150.0])

        menor_valor_esperado = 150.0
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)

        maior_valor_esperado = 150.0
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_should_return_the_lowest_and_highest_when_added_more_than_two_bids(self) -> None:
        self.simulate_auction_scenery([220.5, 100.0, 150.0])

        menor_valor_esperado = 100.0
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)

        maior_valor_esperado = 220.5
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
