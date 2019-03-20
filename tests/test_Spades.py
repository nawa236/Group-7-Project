# mymodule
import unittest
from project import Spades
from project.Spades import Player


class PlayerTest(unittest.TestCase):

    def test_player_score(self):
        p = Player(10)
        assert(p.score == 10)

if __name__ == '__main__':
    unittest.main()