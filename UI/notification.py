from PySide6.QtCore import (
    Qt,
    QPoint,
    QEasingCurve,
    QPropertyAnimation
)

from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QHBoxLayout,
    QVBoxLayout
)


class Notification(QFrame):

    def __init__(
        self,
        icon,
        title,
        message,
        color
    ):

        super().__init__()

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.Tool
        )

        self.setAttribute(
            Qt.WidgetAttribute.WA_ShowWithoutActivating
        )

        self.setWindowOpacity(0)

        self.setObjectName("notification")

        layout = QHBoxLayout(self)

        icon_label = QLabel(icon)
        icon_label.setStyleSheet(
            "font-size:28px;"
        )

        text = QVBoxLayout()

        title_label = QLabel(title)
        title_label.setObjectName("title")

        message_label = QLabel(message)

        text.addWidget(title_label)
        text.addWidget(message_label)

        layout.addWidget(icon_label)
        layout.addLayout(text)

        self.setStyleSheet(f"""
        QFrame#notification {{
            background-color:#2f3136;
            border:2px solid {color};
            border-radius:10px;
            color:white;
            padding:8px;
        }}

        QLabel#title {{
            font-size:16px;
            font-weight:bold;
        }}
        """)

        self.adjustSize()

    def animate_in(self, end_pos):

        start = QPoint(
            end_pos.x() + 60,
            end_pos.y()
        )

        self.move(start)

        self.slide = QPropertyAnimation(
            self,
            b"pos"
        )

        self.slide.setDuration(300)

        self.slide.setStartValue(start)

        self.slide.setEndValue(end_pos)

        self.slide.setEasingCurve(
            QEasingCurve.Type.OutCubic
        )

        self.slide.start()


        self.fade = QPropertyAnimation(
            self,
            b"windowOpacity"
        )

        self.fade.setDuration(300)

        self.fade.setStartValue(0)

        self.fade.setEndValue(1)

        self.fade.start()

    def animate_out(self):

        self.fade = QPropertyAnimation(
            self,
            b"windowOpacity"
        )

        self.fade.setDuration(350)

        self.fade.setStartValue(1)

        self.fade.setEndValue(0)

        self.fade.finished.connect(
            self.close
        )

        self.fade.start()