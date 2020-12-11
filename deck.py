"""
Module with the class definition of Deck.


"""
from card import Card
import random

class Deck(object):
    """A Deck is a list of 52 Cards.

    Attributes:
        cards: a list of objects from class Card. Initialized to a standard 52 deck of cards.
    Class Constants:
        NUMSUITS: number of suits
        NUMRANKS: number of ranks """

    NUMSUITS=4
    NUMRANKS=13


    def __init__(self):
        """
        Initialize self.cards to a list of 52 Cards.
        This is a standard deck of cards used for games such as Blackjack.
        The cards should not be shuffled. That is, they should be added in
        order of suit according to the order given in the Card Class and in
        order of rank (i.e. Hearts should be added first and each Heart card
        should be added with increasing rank).
        """
        #TO DO:
        #Replace pass with your implementation
        self.cards = []

        for i in range(Deck.NUMSUITS):
            for j in range(1, Deck.NUMRANKS+1):
                c = Card(i,j)
                self.cards.append(c)


    def shuffle(self):
        """Shuffle self.cards """
        for k in range(len(self.cards)-1,1,-1):
        # Swap kth card with a card in position p, where p is
        # randomly chosen in [0..k-1]
            p= random.randint(0,k-1)
            tempCard= self.cards[k]
            self.cards[k]= self.cards[p]
            self.cards[p]= tempCard


    def takeACard(self):
        """Returns: the last Card in self.cards (this deck) or returns None.

        If self.cards is not empty then return the last Card object in
        self.cards and make self.cards one element shorter (i.e., take away the
        last card from the deck).  If self is empty then return None. """
        #TO DO:
        #Replace pass with your implementation

        if len(self.cards) != 0:
            last = self.cards[-1]
            self.cards = self.cards[:-1]
            return last
        elif len(self.cards) == 0:
            return None


    def __str__(self):
        """Returns: a string of the card names of all the cards in this deck.
        If the deck is empty, return the string 'Empty deck'. """
        if not self.cards:
            # In Python, bool(x) evaluates to False if x is an empty list and
            # evaluates to True if x is non-empty.
            # An explicit way to check whether self.cards is empty is
            #     if len(self.cards)==0
            return 'Empty deck'
        else:
            card_names = [str(x) for x in self.cards()]
            return ' '.join(card_names)
