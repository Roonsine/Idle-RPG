from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QProgressBar,

)

from PySide6.QtCore import Qt


class SkillWidget(QFrame):
    """
    Displays one player skill.
    """


    def __init__(
        self,
        skill_id,
        skill,
        game
    ):

        super().__init__()


        self.skill_id = skill_id

        self.skill = skill

        self.game = game


        self.setup_ui()

        self.refresh()



    def setup_ui(self):

        self.setFrameStyle(
            QFrame.Shape.Box
        )
        self.setStyleSheet(
            """
            QWidget {
                background-color: #222;
                border-radius: 8px;
                padding: 8px;
            }

            QLabel {
                color: white;
                font-size: 14px;
            }

            QProgressBar {
                height: 18px;
                border-radius: 6px;
                background:#111;
            }

            QProgressBar::chunk {
                background: #4CAF50;
                border-radius: 8px;
            }
            """
        )


        layout = QVBoxLayout()

        self.setLayout(
            layout
        )


        # Skill name

        self.name_label = QLabel()

        self.name_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )


        layout.addWidget(
            self.name_label
        )


        # Level

        self.level_label = QLabel()

        layout.addWidget(
            self.level_label
        )


        # XP bar

        self.progress_bar = QProgressBar()

        self.progress_bar.setRange(
            0,
            100
        )

        self.progress_bar.setTextVisible(
            False
        )
        self.progress_percent = QLabel()

        layout.addWidget(
            self.progress_percent
        )


        layout.addWidget(
            self.progress_bar
        )


        # XP text

        self.xp_label = QLabel()

        layout.addWidget(
            self.xp_label
        )


        # Unlock text

        self.unlock_label = QLabel()

        layout.addWidget(
            self.unlock_label
        )



    def refresh(self):

        skill = self.skill


        display_name = (
            self.skill_id
            .replace("_", " ")
            .title()
        )


        self.name_label.setText(
            f"⚒ {display_name}"
        )


        self.level_label.setText(
            f"Level {skill.level}"
        )


        current_xp = skill.xp


        required_xp = self.xp_required(
            skill.level
        )


        if skill.level >= 99:

            progress = 100

            current_xp = 0

            required_xp = 0


        else:

            progress = int(
                (
                    current_xp /
                    required_xp
                )
                *
                100
            )


        self.progress_bar.setValue(
            progress
        )


        self.progress_percent.setText(
            f"{progress}%"
        )


        if skill.level >= 99:

            self.xp_label.setText(
                "MAX LEVEL"
            )

        else:

            self.xp_label.setText(
                f"{current_xp} / {required_xp} XP"
            )


        self.update_unlock()



    def xp_required(
        self,
        level
    ):

        """
        Temporary XP curve.

        Replace later with Engine/xp.py
        """

        return level * level * 100



    def update_unlock(self):

        """
        Shows the next available unlock.
        """


        if self.skill_id == "woodcutting":

            self.check_tree_unlock()


        elif self.skill_id == "mining":

            self.check_mining_unlock()


        else:

            self.unlock_label.setText(
                ""
            )



    def check_tree_unlock(self):

        current = self.skill.level


        for tree_id in self.game.data.trees:

            tree = self.game.data.trees.get(
                tree_id
            )


            if tree.level_required > current:

                self.unlock_label.setText(
                    f"Next unlock:\n"
                    f"🌳 {tree.name} "
                    f"(Level {tree.level_required})"
                )

                return



        self.unlock_label.setText(
            "All trees unlocked!"
        )



    def check_mining_unlock(self):

        current = self.skill.level


        for rock_id in self.game.data.rocks:

            rock = self.game.data.rocks.get(
                rock_id
            )


            if rock.level_required > current:

                self.unlock_label.setText(
                    f"Next unlock:\n"
                    f"⛏ {rock.name} "
                    f"(Level {rock.level_required})"
                )

                return


        self.unlock_label.setText(
            "All rocks unlocked!"
        )