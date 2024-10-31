from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout, QScrollArea

from pyqt_openai import CONTEXT_DELIMITER, LARGE_LABEL_PARAM, MEDIUM_LABEL_PARAM


class G4FImageHome(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()

    def __initUi(self):
        # TODO LANGUAGE
        title = QLabel("Welcome to GPT4Free\n" + "Image Generation Page !", self)
        title.setFont(QFont(*LARGE_LABEL_PARAM))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        description = QLabel(
            "Generate images for free with the power of G4F." + CONTEXT_DELIMITER
        )

        description.setFont(QFont(*MEDIUM_LABEL_PARAM))
        description.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # TODO v1.7.0 "how does this work?" or "What is GPT4Free?" link (maybe)

        lay = QVBoxLayout()
        lay.addWidget(title)
        lay.addWidget(description)
        lay.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(lay)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)
        self.setWidget(mainWidget)
        self.setWidgetResizable(True)
