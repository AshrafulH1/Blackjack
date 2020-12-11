"""
Module with a function to run a game of blackjack


"""

from card import Card
from deck import Deck
from hand import Hand
from person import *


def simBlackjack(playerNames):
    """ Simulate a game of Blackjack.  playerNames is a 1-d list of
    strings; each string is the name of one player."""

    print('Welcome to Blackjack\n\n')

    numPlayers= len(playerNames)

    #Instantiate the dealer and players
    d= Dealer()
    players =[]
    for k in range(numPlayers):
        players.append(Player(playerNames[k]))

    playing= 1

    while playing>0:
        #Deal a new round:  Clear the hand of the dealer and each active player.
        #Reset each active player's status to HIT.  The dealer and each active
        #player gets 2 cards; display their hands.
        d.getHand().clearHand()
        tf= d.deal(2, d.getHand())
        print(d)
        for pl in players:
           if pl.getStatus()!=Player.QUITGAME:
               pl.getHand().clearHand()
               pl.setStatus(Player.HIT)
               tf= d.deal(2, pl.getHand())
               print(pl)

        #For each active player, repeatedly obtain user input and perform the
        #action until each the player is at stay/21/bust/fullhand
        for pl in players:
            while (pl.getStatus()!=Player.QUITGAME and
                   pl.getStatus()!=Player.STAY and
                   pl.getHand().getHandValue() < 21 and
                   not (pl.getHand().isFull())):
                action= int(input(
                    '\nWhat would %s like to do? (1:HIT  2:STAY  0:QUIT GAME) '
                    % pl.getName()))
                pl.setStatus(action)
                if action==Player.HIT:
                    tf= d.deal(1, pl.getHand())
                    print(pl)

        #Dealer finishes its hand.  Evaulate this round, display results, and
        #for each active player update its statistics.
        d.finishHand()
        print('\n----------------------------------------\n')

        # TODO: Student code here
        dHand = d.getHand()
        print("Dealer's hand: " + str(dHand))
        dealerValue = d.getHand().getHandValue()

        for i in players:
            playerValue = i.getHand().getHandValue()
            if dealerValue > 21 and playerValue <= 21:
                print(d.getName() + " busted.")

        for p1 in players:
            if p1.getStatus() != Player.QUITGAME:
                pHand = p1.getHand()
                print(p1.getName() + "'s hand: " + str(pHand))

                playerValue = p1.getHand().getHandValue()

                if (playerValue > dealerValue and playerValue <= 21) or (
                   (playerValue <= 21 and dealerValue > 21)):
                    print(p1.getName() + " won.")
                    p1.win()
                elif playerValue > 21 or playerValue <= dealerValue:
                    if playerValue <= 21 and dealerValue < 21:
                        print(p1.getName() + " lost.")
                    elif playerValue > 21:
                        print(p1.getName() + " busted.")
                    p1.lose()

        print('\n----------------------------------------\n')

        #Start another round?  NO if there're no active players; otherwise
        #prompt user for input.
        numActivePlayers= 0
        for pl in players:
            if pl.getStatus()!=Player.QUITGAME:
                numActivePlayers= numActivePlayers + 1

        if numActivePlayers==0:
            playing= 0
        else:
            playing= int(input('Start another round? (1:YES  0:NO) '))
            print('\n')


    #Display final statistics (#games won and lost) of all players
    #TODO: Student code here
    for p1 in players:
        #pHand = p1.getHand()
        p1.showStatistics()

    print('Goodbye')


# Script code
if __name__ == '__main__':
    playerNames= ['Ash', 'Bart']
    simBlackjack(playerNames)
