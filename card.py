"""
Module with the class definition of Card.


"""

class Card(object):
    """ Instances represent a card with a suit and a rank

    Attributes (hidden):
        __suit: suit of card where HEART=0; SPADE=1; DIAMOND=2; CLUB=3;
        __rank: rank of card from Ace, Two, Three,..., Queen, King
                [int in the range 1..13]
    Class Constants:
        HEART, SPADE, DIAMOND, CLUB = numeric value assigned to suit"""

    HEART=   0
    SPADE=   1
    DIAMOND= 2
    CLUB=    3

    def getSuit(self):
        """
        Returns: the suit of self (this Card)"""
        return self.__suit

    def getRank(self):
        """Returns: the rank of self (this Card)"""
        return self.__rank

    def __init__(self, s=None, r=None):
        """Sets this card's suit to s and rank to r.
        Default is a Card with None in both attributes.

        Preconditions: s is an integer in [0..3] representing the suit,
                       r is an integer in [1..13] representing the rank"""
        if s!=None:
            assert type(s)==int
            assert 0<=s and s<=3
        if r!=None:
            assert type(r)==int
            assert 1<=r and r<=13

        self.__suit = s
        self.__rank = r

    def getCardValue(self):
        """ Returns: the value of self (this Card).  Ace has the value 1 and
        each face card has the value 10; the remaining cards each has a value
        that matches its rank."""
        #TO DO:
        #Replace pass with your implementation

        if self.__rank == None:
            return 0
        elif self.__rank >= 1 and self.__rank <= 10:
            return self.__rank
        elif self.__rank >= 10 and self.__rank <= 13:
            return 10


    def getCardName(self):
        """Returns: the string representation of self (this Card).  Example,
        'ACE-C' is the ace of clubs, '3-H' is the 3 of hearts, 'JACK-D'
        is the Jack of diamonds, 'KING-S' is the King of spades, ..., etc.
        If self's attributes are None then return the string 'No card'."""
        #TO DO:
        #Replace pass with your implementation

        suit_string = ['H','S','D','C']
        rank_string = ['ACE','2','3','4','5','6','7','8','9','10','JACK','QUEEN','KING']

        if self.__suit == None or self.__rank == None:
            return 'No card'
        elif self.__suit == 0:
            return rank_string[self.__rank-1] + '-' + suit_string[0]
        elif self.__suit == 1:
            return rank_string[self.__rank-1] + '-' + suit_string[1]
        elif self.__suit == 2:
            return rank_string[self.__rank-1] + '-' + suit_string[2]
        elif self.__suit == 3:
            return rank_string[self.__rank-1] + '-' + suit_string[3]

    def __str__(self):
        """ Returns: the string representation of self (this Card)
        If self's attributes are None then return the string 'No card'.
        Make effective use of available methods in the class. """
        return self.getCardName()
