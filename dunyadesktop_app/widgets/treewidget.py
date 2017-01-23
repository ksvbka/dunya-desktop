import os

from PyQt5.QtWidgets import (QTreeWidget, QTreeWidgetItem, QApplication)
from PyQt5.QtCore import Qt, pyqtSignal

from cultures.makam.utilities import get_filenames_in_dir


DOCS_PATH = os.path.join(os.path.dirname(__file__), '..', 'cultures',
                         'documents')


class FeatureTreeWidget(QTreeWidget):
    item_checked = pyqtSignal(str, str, bool)

    def __init__(self, parent=None):
        QTreeWidget.__init__(self, parent=parent)
        self.feature_dict = {}
        self.is_ready = False

        self._set_tree_widget()
        self.expanded.connect(lambda: self.resizeColumnToContents(0))
        self.itemChanged.connect(self._item_changed)

    def _item_changed(self, item, column):
        if self.is_ready:
            type = item.parent().data(0, 0)
            it = item.data(0, 0)
            check_state = item.checkState(column)
            if check_state==2:
                is_checked = True
            else:
                is_checked = False
            self.item_checked.emit(type, it, is_checked)

    def _set_tree_widget(self):
        header = QTreeWidgetItem(['Features', 'Visualize'])
        self.setHeaderItem(header)
        self.setMinimumWidth(250)

    def get_feature_list(self, docid):
        fullnames, folders, names = get_filenames_in_dir(
            os.path.join(DOCS_PATH, docid),keyword='*.json')

        for name in names:
            f_type = name.split('--')[0].strip()
            f_name = name.split('--')[1].strip().split('.')[0].strip()

            try:
                f_list = self.feature_dict[f_type]
                f_list.append(f_name)
                self.feature_dict[f_type] = f_list
            except KeyError:
                f_list= [f_name]
                self.feature_dict[f_type] = f_list
        self.add_items()

    def add_items(self):
        if self.feature_dict:
            for key in self.feature_dict.keys():
                root = QTreeWidgetItem(self, [key])

                for type in self.feature_dict[key]:
                    feature = QTreeWidgetItem(root, ['Feature Types'])
                    feature.setData(0, Qt.EditRole, type)
                    feature.setCheckState(1, Qt.Unchecked)

        self.resizeColumnToContents(0)
        self.resizeColumnToContents(1)

        self.is_ready = True