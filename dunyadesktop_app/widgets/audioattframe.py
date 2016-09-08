from PyQt4 import QtGui, QtCore

from combobox import ComboBox

QUERY_ICON = ":/compmusic/icons/magnifying-glass.png"


class AudioAttFrame(QtGui.QFrame):
    def __init__(self):
        QtGui.QFrame.__init__(self)

        self._set_frame_attributes()

        self.gridLayout_filtering = QtGui.QGridLayout(self)
        self._set_gridlayout_filtering()

    def _set_frame_attributes(self):
        size_policy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,
                                        QtGui.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)
        self.setCursor(
            QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.setFrameShape(QtGui.QFrame.StyledPanel)
        self.setFrameShadow(QtGui.QFrame.Raised)
        self.setLineWidth(1)

    def _set_gridlayout_filtering(self):
        self.gridLayout_filtering.setSizeConstraint(
            QtGui.QLayout.SetNoConstraint)
        self.gridLayout_filtering.setMargin(2)
        self.gridLayout_filtering.setSpacing(3)

        # spacer in grid layout of filtering section
        spacer_item = QtGui.QSpacerItem(3, 20, QtGui.QSizePolicy.Fixed,
                                        QtGui.QSizePolicy.Minimum)
        self.gridLayout_filtering.addItem(spacer_item, 0, 1, 1, 1)

        # combo boxes
        # melodic structure
        self.comboBox_melodic = ComboBox(self)
        self.gridLayout_filtering.addWidget(self.comboBox_melodic, 0, 0, 1, 1)

        # form structure
        self.comboBox_form = ComboBox(self)
        self.gridLayout_filtering.addWidget(self.comboBox_form, 0, 2, 1, 1)

        # rhythmic structure
        self.comboBox_rhythm = ComboBox(self)
        self.gridLayout_filtering.addWidget(self.comboBox_rhythm, 0, 4, 1, 1)

        # composer
        self.comboBox_composer = ComboBox(self)
        self.gridLayout_filtering.addWidget(self.comboBox_composer, 1, 0, 1, 1)
        self.comboBox_composer.set_placeholder_text('Composer')

        # performer
        self.comboBox_performer = ComboBox(self)
        self.gridLayout_filtering.addWidget(self.comboBox_performer,
                                            1, 2, 1, 1)
        self.comboBox_performer.set_placeholder_text('Performer')

        # instrument
        self.comboBox_instrument = ComboBox(self)
        self.gridLayout_filtering.addWidget(self.comboBox_instrument,
                                            1, 4, 1, 1)
        self.comboBox_instrument.set_placeholder_text('Instrument')

        spacer_item1 = QtGui.QSpacerItem(3, 20, QtGui.QSizePolicy.Minimum,
                                         QtGui.QSizePolicy.Fixed)
        self.gridLayout_filtering.addItem(spacer_item1, 1, 3, 1, 1)

        spacer_item2 = QtGui.QSpacerItem(3, 20, QtGui.QSizePolicy.Minimum,
                                         QtGui.QSizePolicy.Fixed)
        self.gridLayout_filtering.addItem(spacer_item2, 0, 5, 1, 1)

        # query button and layout
        self.horizontalLayout_query = QtGui.QHBoxLayout()
        self.horizontalLayout_query.setSpacing(0)

        self.toolButton_query = QtGui.QToolButton(self)
        self.toolButton_query.setMinimumSize(QtCore.QSize(50, 50))
        self.toolButton_query.setMaximumSize(QtCore.QSize(60, 60))
        icon_query = QtGui.QIcon()
        icon_query.addPixmap(QtGui.QPixmap(QUERY_ICON),
                             QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_query.setIcon(icon_query)
        self.toolButton_query.setIconSize(QtCore.QSize(25, 25))
        self.horizontalLayout_query.addWidget(self.toolButton_query)
        self.gridLayout_filtering.addLayout(self.horizontalLayout_query, 0, 6,
                                            2, 1)