import os

from qtpy.QtGui import QPainter
from qtpy.QtSvg import QSvgRenderer
from qtpy.QtWidgets import QLabel

from pyqt_openai import SRC_DIR


class SvgLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__renderer = ''

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.__renderer:
            self.__renderer.render(painter)
        return super().paintEvent(event)

    def setSvgFile(self, filename: str):
        filename = os.path.join(SRC_DIR, filename)
        self.__renderer = QSvgRenderer(filename)
        self.resize(self.__renderer.defaultSize())
        length = max(self.sizeHint().width(), self.sizeHint().height())
        self.setFixedSize(length, length)