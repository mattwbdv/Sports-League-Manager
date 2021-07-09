import pickle
import csv
from pathlib import Path
from curling_league.src.team_member import TeamMember
from curling_league.src.team import Team


class LeagueDatabase:
    _sole_instance = None

    @classmethod
    def instance(cls):
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance

    def __init__(self):
        self._leagues = []
        self._last_oid = 0

    @classmethod
    def load(cls, file_name):
        try:
            with open(file_name, mode="rb") as f:
                cls._sole_instance = pickle.load(f)
        except FileNotFoundError or Exception:
            print("This file was not found, attempting to read from backup.")
            with open(file_name+".backup", mode="rb") as f:
                cls._sole_instance = pickle.load(f)
            print("Backup may have worked!")

    @property
    def leagues(self):
        return self._leagues

    def add_league(self, league):
        self._leagues.append(league)

    def remove_league(self, league):
        self._leagues.remove(league)

    def next_oid(self):
        self._last_oid += 1
        return self._last_oid

    def save(self, file_name):
        p = Path(file_name)
        if p.exists():
            p.rename(file_name+".backup")
        with open(file_name, mode="wb") as f:
            pickle.dump(self._sole_instance, f)

    def export_league(self, league, file_name):
        with open(file_name, 'w', newline='') as f:
            field_names = ['Team name', 'Member name', 'Member email']
            writer = csv.DictWriter(f, field_names)
            writer.writeheader()
            for team in league.teams:
                for member in team.members:
                    writer.writerow({'Team name': team.name,
                                     'Member name': member.name,
                                     'Member email': member.email})

    def import_league(self, new_league, file_name):
        imported_league = {}
        i = 0
        try:
            with open(file_name, mode='r') as f:
                reader = csv.reader(f)
                for rows in reader:
                    # Filter out the title (first) row
                    if i == 0:
                        i += 1
                    # Evaluate each row and add to a dictionary with team name as key
                    else:
                        teamname = rows[0]
                        membername = rows[1]
                        email = rows[2]

                        # Create a team member object with the player data
                        player = TeamMember(self.next_oid(), membername, email)

                        # Only add team members to a new team key if it doesn't already exist
                        if teamname not in imported_league:
                            imported_league.update({teamname: [player]})
                        else:
                            imported_league.get(teamname).append(player)

            oid = self.next_oid()

            # Go through each team in the dictionary and add to the new league
            for team in imported_league.keys():
                oid = self.next_oid()
                new_team = Team(oid, team)
                team_member_array = imported_league.get(team)

                # Go through each member of the team and add to the new team
                for player in team_member_array:
                    new_team.add_member(player)

                # Add the team to the new league
                new_league.add_team(new_team)

            # Add the league to the database
            self.add_league(new_league)

        # Catch errors
        except FileExistsError:
            print("Error loading the file")

