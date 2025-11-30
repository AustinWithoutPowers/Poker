class Suit:
    CLUB: str = 'c'
    DIAMOND: str = 'd'
    HEART: str = 'h'
    SPADE: str = 's'
    _SUITS: list[str] = [CLUB, DIAMOND, HEART, SPADE]

    def __init__(self, suit_str: str) -> None:
        self._suit_str: str = ''
        self._add_suit_str(suit_str=suit_str)
    
    # test: test_suit_str_invalid
    def _add_suit_str(self, suit_str: str) -> None:
        if suit_str not in self._SUITS:
            raise ValueError(f'ERROR: SUITSTRINVALID\nSuit string {suit_str}' + \
                             f' not in {self._SUITS}.')
        self._suit_str = suit_str
    
    # test: test_suit_getter
    @property
    def suit_str(self) -> str:
        return self._suit_str
    # test: test_suit_setter
    @suit_str.setter
    def suit_str(self, suit_str: str) -> None:
        self._add_suit_str(suit_str=suit_str)
    
    # test: test_suit_eq
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Suit):
            return NotImplemented
        return self.suit_str == other.suit_str
    
    # test: test_suit_ne
    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Suit):
            return NotImplemented
        return not self == other

class Number:
    ACE: int = 1
    JACK: int = 11
    QUEEN: int = 12
    KING: int = 13
    ACE2: int = 14
    ACES: list[int] = [ACE, ACE2]
    _NUMBERS: list[int] = [ACE, 2, 3, 4, 5, 6, 7, 8,\
                           9, 10, JACK, QUEEN, KING, ACE2]
    
    def __init__(self, number: int) -> None:
        self._number: int = 0
        self._add_number(number=number)
    
    # test: test_number_invalid
    def _add_number(self, number: int) -> None:
        if number not in self._NUMBERS:
            raise ValueError(f'ERROR: NUMBERINVALID\nNumber {number}' + \
                             f' not in {self._NUMBERS}.')
        self._number = number
    
    # test: test_number_getter
    @property
    def number(self) -> int:
        return self._number
    # test: test_suit_setter
    @number.setter
    def number(self, number: int) -> None:
        self._add_number(number=number)
    
    # test: test_number_eq, test_number_eq_ace_one, test_number_eq_ace_two,
    #       test_number_eq_ace_dif
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Number):
            return NotImplemented
        if self.number in self.ACES:
            return other.number in other.ACES
        return self.number == other.number
    
    # test: test_number_ne, test_number_ne_ace_first, test_number_ne_ace_second
    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Number):
            return NotImplemented
        return not self == other

class Card: ...
class Hand: ...
class CommunityCards: ...