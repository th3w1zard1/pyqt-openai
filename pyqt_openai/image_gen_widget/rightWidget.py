import requests

from qtpy.QtGui import QFont, QPixmap
from qtpy.QtWidgets import QWidget, QLabel, QGridLayout, QStackedWidget, QSplitter
from qtpy.QtCore import Qt

from pyqt_openai.image_gen_widget.explorerWidget import ExplorerWidget
from pyqt_openai.image_gen_widget.thumbnailView import ThumbnailView


class RightWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__currentImageView = ThumbnailView()
        self.__currentImageView.setFilename('Billy Eillish.png')
        self.__explorerWidget = ExplorerWidget()

        imageWidget = QSplitter()
        imageWidget.setOrientation(Qt.Vertical)
        imageWidget.addWidget(self.__currentImageView)
        imageWidget.addWidget(self.__explorerWidget)
        imageWidget.setSizes([700, 300])
        imageWidget.setChildrenCollapsible(False)
        imageWidget.setHandleWidth(2)
        imageWidget.setStyleSheet(
            '''
            QSplitter::handle:vertical
            {
                background: #CCC;
                height: 1px;
            }
            ''')

        homeWidget = QLabel('Home')
        homeWidget.setAlignment(Qt.AlignCenter)
        homeWidget.setFont(QFont('Arial', 32))

        self.__mainWidget = QStackedWidget()
        self.__mainWidget.addWidget(imageWidget)
        self.__mainWidget.addWidget(homeWidget)

        lay = QGridLayout()
        lay.addWidget(self.__mainWidget)
        lay.setContentsMargins(0, 0, 0, 0)
        self.setLayout(lay)

    def showResult(self, url):
        self.__mainWidget.setCurrentIndex(1)
        self.showImage(url)

    def showImage(self, image_url):
        self.__currentImageView.setUrl(image_url)

    def getExplorerWidget(self):
        return self.__explorerWidget