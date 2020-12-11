"""
Module with the class definition of Hand.


"""
from card import Card

class Hand(object):
    """A Hand is a list of at most 5 Cards.

    Attributes (hidden):
        __cards: a list of objects from class Card. Initialized to to an empty
                 list. The length of __cards is no greater than HANDSIZE.
    Class Constants:
        HANDSIZE = the maximum size of a hand"""

    HANDSIZE= 5


    def getCards(self):
        """Returns: list of cards in self.__cards """
        cardList = self.__cards
        return cardList


    def __init__(self):
        """Initialize self.__cards as an empty list"""
        self.__cards= []


    def isFull(self):
        """Returns: True if self is a full hand; otherwise returns False"""
        #TO DO:
        #Replace pass with your implementation
        if len(self.__cards) >= 5:
            return True
        else:
            return False


    def getHandValue(self):
        """Returns: the sum of the values of the Cards in self (this hand)."""
        #TO DO:
        #Replace pass with your implementation
        cardList = self.getCards()
        total = 0
        for i in cardList:
            total = total + i.getCardValue()
        return total


    def addCard(self, c):
        """Returns: True if self isn't already a full hand; in this case add
        Card c to self (this hand).  Otherwise return False and do not add
        Card c."""
        #TO DO:
        #Replace pass with your implementation
        assert type(c) == Card
        if len(self.__cards) < 5:
            self.__cards.append(c)
            return True
        else:
            return False

    def clearHand(self):
        """Clear out the cards in self (this hand), i.e., set to empty array"""
        self.__cards= []


    def __str__(self):
        """
        Returns: string showing all the Cards in self (this hand).
        If self (this hand) is empty, return the string 'Empty hand'.

        Example: 'QUEEN-H 9-S JACK-C ACE-H 5-D'
        """
        if not self.getCards():
            # In Python, bool(x) evaluates to False if x is an empty list and
            # evaluates to True if x is non-empty.
            # An explicit way to check whether self.cards is empty is
            #     if len(self.getCards())==0
            return 'Empty hand'
        #TO DO:
        #Write code to return the card names of this hand as a string
        else:
            # self.getCards() returns a list with a length > 0.

            cardList = self.getCards()
            name_in_list = []
            for i in cardList:
                name = i.getCardName()
                name_in_list.append(name)

            name_in_string = ""
            for j in name_in_list:
                name_in_string = name_in_string + j + ' '

            result = name_in_string.strip()
            return result
