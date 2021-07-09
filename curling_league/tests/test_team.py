import unittest

from curling_league import Team
from curling_league import TeamMember
from curling_league import DuplicateEmail


class TeamTests(unittest.TestCase):
    def test_create(self):
        name = "Curl Jam"
        oid = 10
        t = Team(oid, name)
        self.assertEqual(name, t.name)
        self.assertEqual(oid, t.oid)

    def test_adding_adds_to_members(self):
        t = Team(1, "Flintstones")
        tm1 = TeamMember(5, "f", "f")
        tm2 = TeamMember(6, "g", "g")
        t.add_member(tm1)
        self.assertIn(tm1, t.members)
        self.assertNotIn(tm2, t.members)
        t.add_member(tm2)
        self.assertIn(tm1, t.members)
        self.assertIn(tm2, t.members)

    def test_removing_removes_from_members(self):
        t = Team(1, "Flintstones")
        tm1 = TeamMember(5, "f", "f")
        tm2 = TeamMember(6, "g", "g")
        t.add_member(tm1)
        t.add_member(tm2)
        t.remove_member(tm1)
        self.assertNotIn(tm1, t.members)
        self.assertIn(tm2, t.members)

    def test_adding_team_duplicate(self):
        c = Team(1, "Sonics")
        player1 = TeamMember(13, "Steve", "steve@mac.com")
        player2 = TeamMember(13, "Steve", "steve@mac.com")
        c.add_member(player1)
        with self.assertRaises(DuplicateEmail):
            c.add_member(player2)