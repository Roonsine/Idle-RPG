from collections import deque

from PySide6.QtCore import QTimer

from UI.notification import Notification


class NotificationManager:

    def __init__(self, parent):

        self.parent = parent

        self.notifications = []

    def show(
    self,
    icon,
    title,
    message,
    color="#d4af37"
    ):

        popup = Notification(
            icon,
            title,
            message,
            color
        )

        popup.setParent(
            self.parent
        )

        self.notifications.append(
            popup
        )

        self.reposition()

        popup.show()

        popup.animate_in(
            popup.pos()
        )

        QTimer.singleShot(
            3000,
            lambda p=popup: self.remove(p)
        )

    def remove(self, popup):

        popup.animate_out()

        if popup in self.notifications:
            self.notifications.remove(
                popup
            )

        self.reposition()

    def reposition(self):

        margin = 20

        spacing = 12

        y = margin

        for popup in self.notifications:

            popup.adjustSize()

            popup.move(
                self.parent.width()
                - popup.width()
                - margin,
                y
            )

            y += popup.height() + spacing