from curling_league.duplicate_oid_check import DuplicateOid
from curling_league.identified_object import IdentifiedObject


class Competition(IdentifiedObject):

    def __init__(self, oid, teams_playing, match_location, match_datetime):
        super().__init__(oid)
        self._teams_competing = teams_playing
        self.location = match_location
        self.date_time = match_datetime
        self._competition_list = []


    @property
    def teams_competing(self):
        return self._teams_competing

    @teams_competing.setter
    def teams_competing(self, prop):
        self._teams_competing = prop

    def send_email(self, emailer, subject, message):
        team_members_emails = None
        for x in self.teams_competing:
            for y in x.members:
                team_members_emails.append(y)
        emailer.send_plain_email(team_members_emails, subject, message)

    # return a string like the following: "Competition at location on date_time with N teams"
    # (note: date_time may be None in which case just omit the "on date_time" part.
    def __str__(self):
        if self.date_time is None:
            return str("Competition at " + self.location + " with " + self.teams_competing + " teams")
        else:
            return str("Competition at " + self.location + " on " + self.date_time + " with " + self.teams_competing + " teams")
