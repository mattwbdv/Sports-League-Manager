import unittest
from pathlib import Path


from curling_league import LeagueDatabase
from curling_league import League
from curling_league import Team
from curling_league import TeamMember

class LeagueDatabaseTests(unittest.TestCase):
    def export_league_test(self):
        db = LeagueDatabase.instance()
        league = League(1, "Some league")
        t1 = Team(1, "t1")
        t2 = Team(2, "t2")
        t3 = Team(3, "t3")
        all_teams = [t1, t2, t3]
        league.add_team(t1)
        league.add_team(t2)
        league.add_team(t3)
        tm1 = TeamMember(1, "Fred", "fred")
        tm2 = TeamMember(2, "Barney", "barney")
        tm3 = TeamMember(3, "Wilma", "wilma")
        tm4 = TeamMember(4, "Betty", "betty")
        tm5 = TeamMember(5, "Pebbles", "pebbles")
        tm6 = TeamMember(6, "Bamm-Bamm", "bam-bam")
        tm7 = TeamMember(7, "Dino", "dino")
        tm8 = TeamMember(8, "Mr. Slate", "mrslate")
        t1.add_member(tm1)
        t1.add_member(tm2)
        t2.add_member(tm3)
        t2.add_member(tm4)
        t2.add_member(tm5)
        t3.add_member(tm6)
        t3.add_member(tm7)
        t3.add_member(tm8)
        db.export_league(league, "test.csv")

    def test_removing_league(self):
        db = LeagueDatabase.instance()
        db.save("test")
        db.save("test")
        Path("test").unlink()
        LeagueDatabase.load("test")

    def test_import_export(self):
        db = LeagueDatabase.instance()
        new_league = db.import_league("Test league", "Teams.csv")
        # Test adding the league to a CSV to ensure accuracy
        db.export_league(new_league, "Teams2.csv")

