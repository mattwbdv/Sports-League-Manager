# Python sports league manager! 

This is a sports league manager that can be used with the provided UI or as a headless API to manage a sports league via email or some other interface. 

##The interface follows the following spec: 
### Main window shows list of leagues in the current database. Has load/save menu items and/or buttons that raise Qt5 file dialogs to select the file to load/save. Has buttons to:
• Delete a league

• Add a league (the league name can be input directly in this window)

• Edit a league

### League editor shows list of teams in the league being edited. Has import/export menu items or buttons that raise Qt5 dialogs to select files for import/exports.  Has buttons to:

• Delete a team

• Add a team (the team name can be input directly in this window)

• Edit a team

###Team editor shows list of team members in the team being edited. Has buttons to

• Delete a member

• Add a member (the member's name and email can be input directly in this window)

• Update a member (the member's name and email can be input directly in this window)