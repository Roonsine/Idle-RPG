from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QScrollArea
)

from UI.skill_widget import SkillWidget



class SkillPanel(QWidget):

    def __init__(self, game):

        super().__init__()


        self.game = game


        self.layout = QVBoxLayout() # type: ignore


        self.setLayout(
            self.layout # type: ignore
        )


        self.skills = {}



    def refresh(self):

        if self.game.player is None:
            return


        player_skills = (
            self.game.player.skills
        )


        # Create missing widgets

        for skill_id, skill in player_skills.items():

            if skill_id not in self.skills:

                widget = SkillWidget(
                    skill_id,
                    skill,
                    self.game
                )

                self.skills[skill_id] = widget

                self.layout.addWidget( # type: ignore
                    widget
                )


        # Refresh existing

        for widget in self.skills.values():

            widget.refresh()