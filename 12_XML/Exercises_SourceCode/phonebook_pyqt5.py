#! /usr/bin/env python3

'''
A trivially simple phone book manager.
'''

# TODO: Need to write back the data to the file when the application closes, and possibly at regular
# intervals.

__author__ = 'Russel Winder'
__version__ = '1.2'
__date__ = '2014-08-02'
__copyright__ = 'Copyright © 2011, 2013, 2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import sys

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QFormLayout, QLabel,
    QVBoxLayout, QHBoxLayout, QPushButton, QTableView,
    QMessageBox
)
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt

import phonedata


class PhoneDataModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.header = ('Name', 'Number')
        self.backingData = [[name, number] for name, number in phonedata.data.items()]

    def rowCount(self, parent=QModelIndex()):
        return len(phonedata.data)

    def columnCount(self, parent=QModelIndex()):
        return 2

    def data(self, index, role=Qt.DisplayRole):
        return self.backingData[index.row()][index.column()] if role == Qt.DisplayRole else None

    def headerData(self, column, orientation, role):
        return self.header[column] if orientation == Qt.Horizontal and role == Qt.DisplayRole else None


class PhoneFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Phone Book.')
        self.name = QLineEdit()
        self.number = QLineEdit()
        entry = QFormLayout()
        entry.addRow(QLabel('Name'), self.name)
        entry.addRow(QLabel('Number'), self.number)
        buttons = QHBoxLayout()
        button = QPushButton('&Add')
        button.clicked.connect(self._addEntry)
        buttons.addWidget(button)
        button = QPushButton('&Update')
        button.clicked.connect(self._updateEntry)
        buttons.addWidget(button)
        button = QPushButton('&Delete')
        button.clicked.connect(self._deleteEntry)
        buttons.addWidget(button)
        dataDisplay = QTableView()
        dataDisplay.setModel(PhoneDataModel())
        layout = QVBoxLayout()
        layout.addLayout(entry)
        layout.addLayout(buttons)
        layout.addWidget(dataDisplay)
        self.setLayout(layout)
        self.show()

    def _addEntry(self):
        '''
        Process an add button press.  Append the new data from the data entry boxes to the data model,
        but only if there is actually data in the data entry boxes.
        '''
        name = self.name.text()
        number = self.number.text()
        if(name != ''):
            pass
        else:
            QMessageBox.information(self, 'Phonebook: No Name', '''
The name field is empty,
entry cannot be added.
''', QMessageBox.Close)

    def _updateEntry(self):
        '''
        Process an update button press.  Replace the current selected item with the data from the data
        entry text boxes, but only if there is data in the data entry boxes.
        '''
        name = self.name.text()
        number = self.number.text()
        if(name != ''):
            pass
        else:
            QMessageBox.information(self, 'Phonebook: No Name', '''
The name field is empty,
entry cannot be updated.
''', QMessageBox.Close)

    def _deleteEntry(self):
        '''
        Process a delete entry button press.  Delete the currently selected item from the data model and
        clear the data entry boxes.
        '''
        name = self.name.text()
        if name != '':
            pass
        else:
            QMessageBox.information(self, 'Phonebook: No Name', '''
The name field is empty,
entry cannot be deleted.
''', QMessageBox.Close)

if __name__ == '__main__':
    application = QApplication(sys.argv)
    frame = PhoneFrame()
    sys.exit(application.exec_())
