from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QScrollArea
)

from UI.skill_widget import SkillWidget


class SkillPanel(QWidget):

    def __init__(self, game):

        super().__init__()

        self.game = game

        self.skills = {}

        #
        # Main layout
        #

        self._main_layout = QVBoxLayout()
        self._main_layout.setContentsMargins(5, 5, 5, 5)
        self._main_layout.setSpacing(6)

        self.setLayout(self._main_layout)

        #
        # Character Header
        #

        self.title_label = QLabel("<b>Character</b>")
        self._main_layout.addWidget(self.title_label)

        self.name_label = QLabel()
        self._main_layout.addWidget(self.name_label)

        self.combat_label = QLabel()
        self._main_layout.addWidget(self.combat_label)

        self.total_level_label = QLabel()
        self._main_layout.addWidget(self.total_level_label)

        divider = QLabel("────────────────────")
        self._main_layout.addWidget(divider)

        #
        # Scroll Area
        #

        self._scroll = QScrollArea()
        self._scroll.setWidgetResizable(True)
        self._scroll.setHorizontalScrollBarPolicy(
            self._scroll.horizontalScrollBarPolicy().ScrollBarAlwaysOff
        )

        self._main_layout.addWidget(self._scroll)

        #
        # Container inside the scroll area
        #

        self.scroll_widget = QWidget()

        self.skills_layout = QVBoxLayout()
        self.skills_layout.setContentsMargins(0, 0, 0, 0)
        self.skills_layout.setSpacing(2)

        self.scroll_widget.setLayout(self.skills_layout)

        self._scroll.setWidget(self.scroll_widget)

    def refresh(self):

        if self.game.player is None:
            return

        player = self.game.player

        #
        # Character Summary
        #

        self.name_label.setText(
            f"Player: {player.name}"
        )

        total_level = sum(
            skill.level
            for skill in player.skills.values()
        )

        combat_skill = player.skills.get("combat")

        combat_level = (
            combat_skill.level
            if combat_skill
            else 0
        )

        self.combat_label.setText(
            f"Combat Level: {combat_level}"
        )

        self.total_level_label.setText(
            f"Total Level: {total_level}"
        )

        #
        # Create missing skill widgets
        #

        for skill_id, skill in player.skills.items():

            if skill_id not in self.skills:

                widget = SkillWidget(
                    skill_id,
                    skill,
                    self.game
                )

                self.skills[skill_id] = widget

                self.skills_layout.addWidget(widget)

        #
        # Refresh existing widgets
        #

        for widget in self.skills.values():
            widget.refresh()

        #
        # Push everything to the top
        #

        self.skills_layout.addStretch()