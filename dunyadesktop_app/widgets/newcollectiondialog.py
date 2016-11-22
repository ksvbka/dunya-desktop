import sys
import os

from PyQt4 import QtGui, QtCore

import dunyadesktop_app.utilities.database as database

CSS_PATH = os.path.join(os.path.dirname(__file__), '..', 'ui_files', 'css',
                        'newcollectiondialog.css')


class NewCollectionDialog(QtGui.QDialog):
    """The dialog which pops up when the user clicks the combobox"""
    new_collection_added = QtCore.pyqtSignal()

    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent)
        self._set_dialog()

        layout = QtGui.QGridLayout(self)
        layout.setContentsMargins(0, 2, 0, 1)
        layout.setHorizontalSpacing(0)
        layout.setVerticalSpacing(2)

        self.coll_edit = QtGui.QLineEdit(self)
        self.coll_edit.setMaximumSize(QtCore.QSize(16777215, 40))
        layout.addWidget(self.coll_edit, 1, 0, 1, 1)

        self.desc_edit = QtGui.QTextEdit(self)
        self._set_desc_edit()
        layout.addWidget(self.desc_edit, 3, 0, 1, 1)

        self.label_name = QtGui.QLabel(self)
        self.label_name.setText('Name')
        layout.addWidget(self.label_name, 0, 0, 1, 1)

        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setStandardButtons(
            QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        layout.addWidget(self.buttonBox, 7, 0, 1, 1)

        self.label_description = QtGui.QLabel(self)
        self.label_description.setText('Description')
        layout.addWidget(self.label_description, 2, 0, 1, 1)

        self._set_css(self, CSS_PATH)

        self.buttonBox.rejected.connect(self.clicked_cancel)
        self.buttonBox.accepted.connect(self.clicked_ok)

    def _set_dialog(self):
        self.setWindowTitle('New Collection')
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,
                                       QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(350, 250))
        self.setMaximumSize(QtCore.QSize(350, 250))

    def _set_desc_edit(self):
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
                                       QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.desc_edit.sizePolicy().hasHeightForWidth())
        self.desc_edit.setSizePolicy(sizePolicy)
        self.desc_edit.setMinimumSize(QtCore.QSize(0, 140))
        self.desc_edit.setMaximumSize(QtCore.QSize(16777215, 150))

    @staticmethod
    def _set_css(obj, css_path):
        with open(css_path) as f:
            css = f.read()
        obj.setStyleSheet(css)

    def clicked_cancel(self):
        """Closes the window"""
        self.close()

    def clicked_ok(self):
        conn, c = database.connect()
        user_input = str(self.coll_edit.text())

        status = False
        if user_input:
            status = database.add_collection(conn, c, user_input)

        if status:
            self.close()
            self.new_collection_added.emit()
            self.parent().update_collection_widget()
        else:
            msg_box = QtGui.QMessageBox()
            msg_box.setText('Given collection name is not valid!')
            msg_box.setWindowTitle('')
            self._set_css(msg_box, CSS_PATH)
            msg_box.exec_()

'''
app = QtGui.QApplication(sys.argv)
mainwindow_makam = NewCollectionDialog()
mainwindow_makam.show()
app.exec_()
'''