import unittest
import datetime

from curling_league import Competition
from curling_league import League
from curling_league import Team
from curling_league import DuplicateOid


class DuplicateOID:
    pass


class CompetitionTests(unittest.TestCase):
    def test_create(self):
        now = datetime.datetime.now()
        t1 = Team(1, "Team 1")
        t2 = Team(2, "Team 2")
        t3 = Team(3, "Team 3")
        c1 = Competition(1, [t1, t2], "Here", None)
        c2 = Competition(2, [t2, t3], "There", now)

        self.assertEqual("Here", c1.location)
        self.assertEqual(1, c1.oid)
        self.assertIsNone(c1.date_time)
        self.assertEqual(2, len(c1.teams_competing))
        self.assertIn(t1, c1.teams_competing)
        self.assertIn(t2, c1.teams_competing)
        self.assertNotIn(t3, c1.teams_competing)

        self.assertEqual("There", c2.location)
        self.assertEqual(2, c2.oid)
        self.assertEqual(now, c2.date_time)
        self.assertEqual(2, len(c2.teams_competing))
        self.assertNotIn(t1, c2.teams_competing)
        self.assertIn(t2, c2.teams_competing)
        self.assertIn(t3, c2.teams_competing)

    def test_adding_competition_duplicate(self):
        c = Competition(1, [], "Local tourney", None)
        c2 = Competition(1, [], "Comp 2", None)
        league = League(13, "AL State Curling League")
        self.assertNotIn(c, league.competitions)
        league.add_competition(c)
        self.assertIn(c, league.competitions)
        with self.assertRaises(DuplicateOid):
            league.add_competition(c2)

    def test_adding_team_duplicate(self):
        c = Competition(1, [], "Sonics", None)
        c2 = Competition(1, [], "Thunder", None)
        league = League(13, "AL State Curling League")
        self.assertNotIn(c, league.teams)
        league.add_team(c)
        self.assertIn(c, league.teams)
        with self.assertRaises(DuplicateOid):
            league.add_team(c2)
