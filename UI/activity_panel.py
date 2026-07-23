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

        self.selected_zone = None

        self.widgets = []

        self.main_layout = QVBoxLayout()

        self.setLayout(
            self.main_layout
        )


        self.title = QLabel(
            "Activities"
        )

        self.main_layout.addWidget(
            self.title
        )


        self.create_actions()



    def set_skill(self, skill_id):

        if skill_id == self.current_skill:
            return


        self.current_skill = skill_id

        self.selected_zone = None

        self.refresh()



    def refresh(self):

        self.clear_widgets()

        self.create_actions()



    def clear_widgets(self):

        for widget in self.widgets:

            self.main_layout.removeWidget(
                widget
            )

            widget.deleteLater()


        self.widgets.clear()



    def create_actions(self):

        activity = (
            self.game.activity_registry.get(
                self.current_skill
            )
        )


        if activity is None:

            self.create_empty_message()

            return



        objects = activity["provider"]()


        activity_type = activity.get(
            "type",
            "direct"
        )


        if activity_type == "grouped":

            self.create_grouped_activity(
                objects,
                activity["icon"],
                self.current_skill
            )


        else:

            self.create_direct_activity(
                objects,
                activity["icon"],
                self.current_skill
            )



    # ------------------------------------------------
    # Direct Activities
    # Woodcutting / Mining
    # ------------------------------------------------

    def create_direct_activity(
        self,
        objects,
        icon,
        skill_id
    ):


        for object_id, obj in objects.items():

            player_level = (
                self.game.player.skills[skill_id].level
            )


            locked = (
                hasattr(obj, "level_required")
                and player_level < obj.level_required
            )


            text = (
                f"{icon} {obj.name}"
            )


            if locked:

                text += (
                    f" 🔒 Lv {obj.level_required}"
                )


            button = QPushButton(
                text
            )


            button.setEnabled(
                not locked
            )


            button.clicked.connect(
                lambda checked=False,
                target_id=object_id:
                self.action_selected.emit(
                    skill_id,
                    target_id
                )
            )


            self.add_widget(
                button
            )



    # ------------------------------------------------
    # Grouped Activities
    # Fishing
    # ------------------------------------------------

    def create_grouped_activity(
        self,
        objects,
        icon,
        skill_id
    ):

        player_level = (
            self.game.player.skills[skill_id].level
        )

        # Create one button for each fishing zone
        for zone_id, spot in objects.items():

            button = self.create_locked_button(
                text=f"{icon} {spot.name}",
                required_level=spot.level_required,
                player_level=player_level,
                callback=lambda checked=False, zone=spot:
                    self.select_zone(zone)
            )

            self.add_widget(button)

        # Show the selected zone's fish underneath
        if self.selected_zone is not None:

            self.create_fish_buttons(
                skill_id
            )


    def select_zone(
        self,
        zone
    ):

        self.selected_zone = zone


        self.remove_fish_widgets()


        self.create_fish_buttons(
            self.current_skill
        )



    def create_fish_buttons(
        self,
        skill_id
    ):

        player_level = (
            self.game.player.skills[skill_id].level
        )

        if self.selected_zone is None:
            return

        label = QLabel(
            f"Fish at {self.selected_zone.name}:"
        )

        label.is_fish_widget = True # type: ignore

        self.add_widget(label)

        for entry in self.selected_zone.fish:

            fish = self.game.data.fish.get(
                entry.fish_id
            )

            button = self.create_locked_button(
                text=f"🐟 {fish.name}",
                required_level=fish.level_required,
                player_level=player_level,
                callback=lambda checked=False,
                zone_id=self.selected_zone.id,
                fish_id=fish.id:
                    self.action_selected.emit(
                        skill_id,
                        f"{zone_id}:{fish_id}"
                    )
            )

            button.is_fish_widget = True # type: ignore

            self.add_widget(button)

    def create_locked_button(
        self,
        text,
        required_level,
        player_level,
        callback=None
    ):

        locked = (
            player_level < required_level
        )

        if locked:
            text += f" 🔒 Lv {required_level}"

        button = QPushButton(text)

        button.setEnabled(
            not locked
        )

        if not locked and callback is not None:
            button.clicked.connect(callback)

        return button

    def remove_fish_widgets(self):

        for widget in self.widgets[:]:


            if getattr(
                widget,
                "is_fish_widget",
                False
            ):


                self.main_layout.removeWidget(
                    widget
                )


                widget.deleteLater()


                self.widgets.remove(
                    widget
                )



    # ------------------------------------------------
    # Helpers
    # ------------------------------------------------

    def add_widget(
        self,
        widget
    ):

        self.widgets.append(
            widget
        )

        self.main_layout.addWidget(
            widget
        )



    def create_empty_message(self):

        label = QLabel(
            "No activities available."
        )


        self.add_widget(
            label
        )