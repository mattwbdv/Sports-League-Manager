import sys
from PyQt5 import uic, QtWidgets

from curling_league.src.league_database import LeagueDatabase
from curling_league.src.team_member import TeamMember

UI_MainWindow, QTBaseWindow = uic.loadUiType("src/edit_player_dialogue.ui")


class EditPlayerDialogue(QTBaseWindow, UI_MainWindow):
    def __init__(self, team=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.team = team
        self.update_ui()
        self.add_player_button.clicked.connect(self.add_player_clicked)
        self.remove_player.clicked.connect(self.remove_player_clicked)

    def update_ui(self):
        self.player_list_widget.clear()
        for player in self.team.members:
            self.player_list_widget.addItem(str(player))

    def add_player_clicked(self):
        selected_row = self.player_list_widget.currentRow()
        oid = LeagueDatabase.instance().next_oid()
        print(selected_row)
        pass

        if selected_row != -1:
            member_to_remove = self.team.members[selected_row]
            self.team.remove_member(member_to_remove)
            new_name = self.player_name.text()
            new_email = self.player_email.text()
            new_member_to_add = TeamMember(oid, new_name, new_email)
            self.team.add_member(new_member_to_add)
            self.update_ui()
        else:
            name = self.player_name.text()
            email = self.player_email.text()
            # create member object
            member_to_add = TeamMember(oid, name, email)
            # add player to the team in the instance of the league
            self.team.add_member(member_to_add)
            # update the ui
            self.update_ui()

    def remove_player_clicked(self):
        row_to_remove = self.player_list_widget.currentRow()
        player_to_remove = self.team.members[row_to_remove]
        self.team.remove_member(player_to_remove)
        self.update_ui()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = EditPlayerDialogue()
    window.show()
    sys.exit(app.exec_())
