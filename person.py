"""
Module with class definitions of Person and its two subclasses,
Player and Dealer.


"""

from hand import Hand
from deck import Deck
import random


class Person(object):
    """A Person has a name and a Hand (of Cards) for playing blackjack.

    Attributes (hidden):
        __name = person's name, a string
        __hand = Hand object initialized to be the empty Hand"""


    def getName(self):
        """Returns: the Person's name, a string"""
        return self.__name


    def getHand(self):
        """Returns: the Person's hand, a Hand instance"""
        return self.__hand


    def __init__(self,name=''):
        """Initialize self.__name to nam and self.__hand to a new Hand object
        (with zero Cards).

        Parameter name: a string (default is '') """

        assert type(name)==str, 'name' + ' is not a string'

        self.__name= name
        self.__hand= Hand()


    def __str__(self):
        """Returns: a string containing self's name and hand.  If the hand is a
        bust then display additionally display '<p> busted' where <p> is
        self's name."""
        s= self.getName() + "'s hand: " + str(self.getHand())
        if self.getHand().getHandValue() > 21:
            s= s + '\n' + self.getName() + ' busted.'

        return s


class Player(Person):
    """A Player is a Person.  A Player is not the dealer and keeps track of the
    number of games won and lost.  A Player has three states:  0 indicating
    it has quit the game, 1 indicating HIT for the current round, and 2
    indicating STAY for the current round.

    Attributes (hidden):
        __status: a Player's state, which is one of constants,
                  HIT, STAY, or QUITGAME
        __gamesWon: number of games that self has won (initialized to 0)
        __gamesLost: number of games that self has lost (initialized to 0)

    Class Constants:
        HIT, STAY, QUITGAME = integers representing a Player's action status in
                              one round
    Class Variable:
        numberOfPlayers = an int, the number of players in the game """


    HIT=1
    STAY=2
    QUITGAME=0

    numberOfPlayers= 0


    def getStatus(self):
        """ Returns: self's status"""
        return self.__status


    def setStatus(self, s):
        """ Set self's status to s.
        Parameter s: an int indicating the player's status
        Precondition: s is Player.QUITGAME, Player.HIT, or Player.STAY. """
        # TO DO
        # Replace pass with your implementation
        # Enforce the precondition using assert
        assert type(s) == int
        assert s >= 0 and s <= 2
        self.__status = s


    def __init__ (self,name=''):
        """Increment class variable numberOfPlayers and initialize attributes.

        Initialize player's name to name if name is not empty string.  If name is
        empty string then initialize player's name to the generated string
        'Player<p>' where <p> is the class variable value numberOfPlayers after
        it gets incremented in this method.  Example: if numberOfPlayers is 2
        then the generated string name for the player is 'Player2'

        Initialize self.__status to Player.HIT

        Initialize self.__gamesWon and self.__gamesLost to 0.

        Precondition: name is a string, possibly empty """

        Player.numberOfPlayers= Player.numberOfPlayers + 1

        if not name:
            name= 'Player' + str(Player.numberOfPlayers)

        Person.__init__(self,name)
        self.__gamesWon= 0
        self.__gamesLost= 0
        # TO DO
        # Replace the statement below with a call to your setStatus method
        self.setStatus(Player.HIT)


    def win(self):
        """Increment self.__gamesWon"""
        # TO DO
        # Replace pass with your implementation
        self.__gamesWon += 1


    def lose(self):
        """Increment self.__gamesLost"""
        # TO DO
        # Replace pass with your implementation
        self.__gamesLost += 1


    def showStatistics(self):
        """Print self's name and game statistics (number of games won and
        lost)"""
        print('%s won %d and lost %d games.' %(self.getName(),
                                                 self.__gamesWon,
                                                 self.__gamesLost))


class Dealer(Person):
    """A Dealer is a Person who has a Deck (of Cards) and deals out cards in
    the game of blackjack.  When the Dealer runs out of Cards in its deck it
    gets a new Deck.  No statistics is kept for the Dealer.

    Attributes (hidden):
        __deck: a Deck object inialized to a standard list of 52 cards"""


    def __init__(self):
        """Initialize dealer's name and deck of cards.
        A Dealer is given the name 'Dealer' and a new Deck of Cards."""
        Person.__init__(self, 'Dealer')
        self.prepareNewDeck()


    def prepareNewDeck(self):
        """ Assign to self.__deck a new Deck and shuffle it."""
        # TO DO
        # Replace pass with your implementation
        new_deck = Deck()
        new_deck.shuffle()
        self.__deck = new_deck


    def deal(self, n, hdt):
        """Returns: True if self successfully deals n cards to hand hdt;
        otherwise returns False.

        The dealer (self) deals n cards from its deck to Hand hdt.  Return
        True if the n cards are dealt (added to Hand hdt) successfully;
        otherwise and display a warning/diagnostic message and return False.

        Preconditions:
            n is an int >0
            hdt is a Hand instance """

        assert type(n)==int and n>0
        assert type(hdt)==Hand

        for k in range(n):
            c= self.__deck.takeACard()
            if c==None:
                self.prepareNewDeck()
                c= self.__deck.takeACard()
            status= hdt.addCard(c);
            if status==False:
                print('Unable to deal card #'+ str(k) + ' to the hand')

        return status


    def finishHand(self):
        """The dealer (self) deals card from its deck to its hand until its
           hand's value is >16 or until its hand is full."""
        while self.getHand().getHandValue()<17 and not self.getHand().isFull():
            self.deal(1, self.getHand())
