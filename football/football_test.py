import unittest
from players import Player, Quarterback
from teams import *
from game import Game
# TODO - some things you can add...

# import the `season` file and make sure generate_random_games only
# makes games with appropriate team names (and never has a team playing itself)

# Complete the FootballGameTest


class FootballGameTest(unittest.TestCase):
    '''test the class'''
    def test_field_goal_made(self):
        pass  # TODO

    def test_get_winnerr(self):
        pass  # TODO


class FootballPlayerTest(unittest.TestCase):
    '''Check the default values for Player and Quarterback
    yards=120, touchdowns=5, safety=1,
                 interceptions=0
    '''
    def test_default_player_yards(self):
        player = Player(name='Dude')
        self.assertEqual(player.yards, 120)

    def test_player_yards_set_to(self):
        player = Player(name='OtherDude', yards=150)
        self.assertEqual(player.yards, 150)

    def test_default_qb_interceptions(self):
        qb = Quarterback(name='FancyDude')
        self.assertEqual(qb.interceptions, 4)

    def test_default_qb_completed_passes(self):
        qb = Quarterback()
        self.assertEqual(qb.completed_passes, 20)

    def test_passing_score(self):
        qb = Quarterback()
        self.assertEqual((20 - (2 * 4)), qb.passing_score())
        qb1 = Quarterback(completed_passes= 40, interceptions = 2)
        self.assertEqual((40 - (2 * 2)), qb1.passing_score())

class TeamsTest(unittest.TestCase):
    '''Check lengths of team names, locations, and weeks
    '''
    def test_teams_lengths(self):
        self.assertEqual(len(team_names), 5)
        self.assertEqual(len(locations), 5)
        self.assertEqual(len(weeks), 12)

if __name__ == '__main__':
    unittest.main()