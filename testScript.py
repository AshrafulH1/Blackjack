"""
Tests for Card, Deck, Hand, and Person classes


"""
from card import Card
from deck import Deck
from hand import Hand
from person import *
import testcase

def test_Class_Card():
    """
    Tests methods for Card objects
    """
    print('Testing Card Class')

    card_dict = {
        Card.HEART:0,Card.SPADE:1,Card.DIAMOND:2,Card.CLUB:3
    }
    for key in card_dict:
        testcase.assert_equals(card_dict[key],key)

    c1 = Card(0, 12) # Instantiate a Queen of Hearts
    c2 = Card(Card.SPADE, 9)  # Instantiate a 9 of Spades, using the constant name
    c3 = Card(Card.CLUB, 11)  # Instantiate a JACK of Clubs, using the constant name
    c4 = Card(0, 1) # Instantiate a ACE of Hearts
    c5 = Card() # Instantiate Default

    # Testing getSuit and getRank
    testcase.assert_equals(1,c2.getSuit())
    testcase.assert_equals(11,c3.getRank())
    testcase.assert_equals(None,c5.getRank())

    #Testing getCardValue
    testcase.assert_equals(10,c1.getCardValue())
    #TODO : FINISH TESTING c2-c5
    testcase.assert_equals(19,c2.getCardValue() + c3.getCardValue())
    testcase.assert_equals(9,c2.getCardValue())
    testcase.assert_equals(10,c3.getCardValue())
    testcase.assert_equals(1,c4.getCardValue())
    testcase.assert_equals(0,c5.getCardValue())
    testcase.assert_equals(1,c5.getCardValue() + c4.getCardValue())


    #Testing getCardName
    testcase.assert_equals('QUEEN-H',c1.getCardName())
    #TODO : FINISH TESTING c2-c5
    testcase.assert_equals('9-S',c2.getCardName())
    testcase.assert_equals('JACK-C',c3.getCardName())
    testcase.assert_equals('ACE-H',c4.getCardName())
    testcase.assert_equals('No card',c5.getCardName())

    testcase.assert_equals('No card',str(c5))


def test_Class_Hand():
    """
    Tests methods for Hand objects
    """
    print('Testing Class Hand')
    h = Hand()             # an empty hand
    testcase.assert_equals('Empty hand', str(h))
    testcase.assert_equals(0,h.getHandValue())
    testcase.assert_equals(False,h.isFull())
    testcase.assert_equals([],h.getCards())# No card, since the hand is empty

    cards = [
        Card(0, 12),
        Card(Card.SPADE, 9),
        Card(Card.CLUB, 11),
        Card(0, 1),
        Card(2,5),
        Card(2,6),
    ]

    testcase.assert_error(h.addCard,3)    # error: invalid argument type

    testcase.assert_equals(True,h.addCard(cards[0]))
    #TODO: TEST AND ADD CARDS FROM THE LIST ABOVE UNTIL THE DECK IS FULL
    testcase.assert_equals(True,h.addCard(cards[1]))
    testcase.assert_equals(True,h.addCard(cards[2]))
    testcase.assert_equals(True,h.addCard(cards[3]))
    testcase.assert_equals(True,h.addCard(cards[4]))
    testcase.assert_equals(False,h.addCard(cards[5]))
    testcase.assert_equals(True,h.isFull())



    value = 0
    for card in cards[:-1]:
        value += card.getCardValue()
    testcase.assert_equals(value,h.getHandValue())

    for ind in range(len(cards)-1):
        cards[ind] = cards[ind].getCardName()
    cards.pop()
    testcase.assert_equals(' '.join(cards),str(h))


def test_Class_Deck():
    """
    Tests methods for Deck objects
    """
    print('Testing Class Deck')
    d = Deck() # Instantiate a Deck object
    check_deck = [
    'ACE-H','2-H','3-H','4-H','5-H','6-H','7-H','8-H','9-H','10-H','JACK-H',
    'QUEEN-H', 'KING-H',
    'ACE-S','2-S','3-S','4-S','5-S','6-S','7-S','8-S','9-S','10-S','JACK-S',
    'QUEEN-S', 'KING-S',
    'ACE-D','2-D','3-D','4-D','5-D','6-D','7-D','8-D','9-D','10-D','JACK-D',
    'QUEEN-D', 'KING-D',
    'ACE-C','2-C','3-C','4-C','5-C','6-C','7-C','8-C','9-C','10-C','JACK-C',
    'QUEEN-C', 'KING-C'
    ]
    testcase.assert_equals(52,len(d.cards)) # Deck has 52 cards
    str_deck = [str(x) for x in d.cards]
    testcase.assert_equals(check_deck,str_deck) # Deck has 52 cards

    #TODO: test method takeACard
    testcase.assert_equals('KING-C', str(d.takeACard()))
    testcase.assert_equals(51, len(d.cards)) # deck has 51 cards after taking one

    for i in range(len(d.cards)):
        d.takeACard()

    testcase.assert_equals(None, d.takeACard())

def test_Class_Person():
    """
    Practice using Person Class methods
    """
    #TODO : practice using Person's methods
    p = Person('N')
    testcase.assert_equals("N's hand: Empty hand", str(p))
    testcase.assert_equals('N', p.getName())
    testcase.assert_equals('Empty hand', str(p.getHand()))
    p.getHand().getHandValue()
    p.getHand().addCard(Card(0, 12))
    testcase.assert_equals('10', str(p.getHand().getHandValue()))


def test_Class_Player():
    """
    Tests methods for Player objects
    """
    print('Testing Class Player')
    jane = Player('Jane')
    testcase.assert_equals(1,jane.getStatus())
    jane.setStatus(Player.STAY)
    testcase.assert_equals(2,jane.getStatus())
    testcase.assert_error(jane.setStatus,5)    # error: invalid player status
    anon= Player()
    testcase.assert_equals('Player2\'s hand: Empty hand', str(anon))
    testcase.assert_equals('Empty hand', str(jane.getHand()))
    c1 = Card(1, 6) # Instantiate a Queen of Hearts
    jane.getHand().addCard(c1)
    testcase.assert_equals('6-S', str(jane.getHand()))   # should see 6 of Spades
    c2 = Card(Card.SPADE, 9)  # Instantiate a 9 of Spades, using the constant name
    jane.getHand().addCard(c2)
    testcase.assert_equals('Jane\'s hand: 6-S 9-S',str(jane))


def test_Class_Dealer():
    """
    Tests methods for Dealer objects
    """
    print('Testing Class Dealer')
    dealer= Dealer()
    testcase.assert_equals('Dealer\'s hand: Empty hand', str(dealer))
    testcase.assert_equals(True,dealer.deal(2, dealer.getHand()))
    # responsible for print statements in script output
    testcase.assert_equals(False,dealer.deal(6, dealer.getHand()))
    dealer.getHand().clearHand()
    testcase.assert_equals('Empty hand',str(dealer.getHand()))
    dealer.finishHand()
    bool = dealer.getHand().isFull() or 16 < dealer.getHand().getHandValue()
    testcase.assert_equals(True, bool)


test_Class_Card()
test_Class_Hand()
test_Class_Deck()
test_Class_Person()
test_Class_Player()
test_Class_Dealer()
print('All tests passed!')
