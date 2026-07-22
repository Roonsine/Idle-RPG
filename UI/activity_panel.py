from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
)


class ActivityPanel(QWidget):

    action_selected = Signal(str, str)

    def __init__(self, game):
        super().__init__()

        self.game = game

        self.current_skill = "woodcutting"

        self.widgets = []

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.title = QLabel("Activities")
        self.main_layout.addWidget(self.title)

        self.create_actions()


    def set_skill(self, skill_id):
        """
        Changes the displayed skill.
        """

        if skill_id == self.current_skill:
            return

        self.current_skill = skill_id
        self.refresh()


    def refresh(self):
        """
        Rebuilds activity buttons.
        """

        self.clear_widgets()
        self.create_actions()


    def clear_widgets(self):

        for widget in self.widgets:
            self.main_layout.removeWidget(widget)
            widget.deleteLater()

        self.widgets.clear()


    def create_actions(self):
        """
        Gets activities from ActivityRegistry.
        """

        provider = self.game.activity_registry.get(
            self.current_skill
        )

        if provider is None:
            self.create_empty_message()
            return


        objects = provider()


        try:
            skill = self.game.data.skills.get(
                self.current_skill
            )

        except KeyError:
            self.create_empty_message()
            return


        self.create_buttons(
            objects,
            skill.icon,
            self.current_skill
        )


    def create_buttons(
        self,
        objects,
        icon,
        skill_id
    ):

        for object_id, obj in objects.items():

            button = QPushButton(
                f"{icon} {obj.name}"
            )


            button.clicked.connect(
                lambda checked=False,
                target_id=object_id:
                self.action_selected.emit(
                    skill_id,
                    target_id
                )
            )


            self.widgets.append(button)
            self.main_layout.addWidget(button)


    def create_empty_message(self):

        label = QLabel(
            "No activities available."
        )

        self.widgets.append(label)
        self.main_layout.addWidget(label)