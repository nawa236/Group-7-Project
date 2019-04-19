# mymodule
import unittest
from project import Spades
from project.Spades import Player
from project import cardDeck_print
from project.cardDeck_print import Deck
from project.Spades import Team


class PlayerTest(unittest.TestCase):

    #Test the Creation of a Player
    def test_player_name(self):
        p = Player("Matt", False)
        assert(p.name == "Matt")

    #Test to make sure a deck has 52 cards with no repetitions
    def test_deck(self):
        d = Deck()
        assert(len(d.cards) == 52)

        while (len(d.cards) > 0):
            card = d.cards.pop()
            assert(card not in d.cards)

    #Test Deck Drawing
    def test_drawing(self):
        d = Deck()
        card = d.draw()
        assert(card is not None)
        assert(card not in d.cards)

    #Test Creation of a Team, and Dealing of Cards
    def test_team(self):
        t = Team(Player("P1",False),Player("P2",False))
        d = Deck()
        t.deal_cards(d)
        assert(len(d.cards) == 26)
        assert(len(t.players[0].hand) == 13)
        assert(len(t.players[1].hand) == 13)

    #Test team getting score from individual players' books
    def test_team_score_counter(self):
        t = Team(Player("P1",False),Player("P2",False))
        t.players[0].score = 2
        t.players[1].score = 5
        assert(t.get_score() == 7)




if __name__ == '__main__':
    unittest.main()


#test cards dealt

#test score compared to hand

