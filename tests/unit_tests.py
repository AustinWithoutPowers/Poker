import unittest
from src.classes import Suit, Number

class SuitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.test_suit = Suit(suit_str=Suit.CLUB)
    
    def test_suit_str_invalid(self):
        with self.assertRaises(Exception) as context:
            _ = Suit('p')
        self.assertTrue('ERROR: SUITSTRINVALID' in str(context.exception))
    
    def test_suit_getter(self):
        self.assertEqual(self.test_suit.suit_str, Suit.CLUB)
    
    def test_suit_setter(self):
        test_suit = Suit(suit_str=Suit.CLUB)
        test_suit.suit_str = Suit.DIAMOND
        self.assertEqual(test_suit.suit_str, Suit.DIAMOND)
    
    def test_suit_eq(self):
        self.assertTrue(self.test_suit == Suit(Suit.CLUB))

    def test_suit_ne(self):
        self.assertTrue(self.test_suit != Suit(Suit.DIAMOND))

class NumberTests(unittest.TestCase):
    def setUp(self) -> None:
        self.test_number = Number(number=2)
    
    def test_number_invalid(self):
        with self.assertRaises(Exception) as context:
            _ = Number(29)
        self.assertTrue('ERROR: NUMBERINVALID' in str(context.exception))
    
    def test_number_getter(self):
        self.assertEqual(self.test_number.number, 2)
    
    def test_number_setter(self):
        test_number = Number(number=Number.ACE)
        test_number.number = 2
        self.assertEqual(test_number.number, 2)
    
    def test_number_eq(self):
        self.assertTrue(self.test_number == Number(2))
    
    def test_number_eq_ace_one(self):
        test_ace = Number(number=Number.ACE)
        test_another_ace = Number(number=Number.ACE)
        self.assertTrue(test_ace == test_another_ace)
    
    def test_number_eq_ace_two(self):
        test_ace = Number(number=Number.ACE2)
        test_another_ace = Number(number=Number.ACE2)
        self.assertTrue(test_ace == test_another_ace)
    
    def test_number_eq_ace_dif(self):
        test_ace = Number(number=Number.ACE)
        test_another_ace = Number(number=Number.ACE2)
        self.assertTrue(test_ace == test_another_ace)

    def test_number_ne(self):
        self.assertTrue(self.test_number != Number(3))
    
    def test_number_ne_ace_first(self):
        test_ace = Number(number=Number.ACE)
        self.assertTrue(test_ace != self.test_number)
    
    def test_number_ne_ace_second(self):
        test_ace = Number(number=Number.ACE)
        self.assertTrue(self.test_number != test_ace)

if __name__ == '__main__':
    unittest.main()