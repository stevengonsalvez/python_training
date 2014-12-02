#! /usr/bin/env python3
# -*- coding: utf-8; -*-

'''
A trivially simple phone book manager.
'''

# TODO: Need to write back the data to the file when the application closes, and possibly at regular
# intervals.

__author__ = 'Russel Winder'
__version__ = '1.1'
__date__ = '2012-05-07'
__copyright__ = 'Copyright © 2012 Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import sys

from gi.repository import Gtk

import phonedata


class PhoneFrame(Gtk.Window):
    def __init__(self):
        super(PhoneFrame, self).__init__()
        self.set_title('Phone Book')
        self.connect('delete-event', Gtk.main_quit)
        self.nameEntry = Gtk.Entry(max_length=30)
        self.numberEntry = Gtk.Entry(max_length=30)
        data = Gtk.Table(2, 2, True)
        data.attach(Gtk.Label('Name'), 0, 1, 0, 1, ypadding=5)
        data.attach(self.nameEntry, 1, 2, 0, 1, ypadding=5)
        data.attach(Gtk.Label('Number'), 0, 1, 1, 2, ypadding=5)
        data.attach(self.numberEntry, 1, 2, 1, 2, ypadding=5)
        buttons = Gtk.HButtonBox()
        button = Gtk.Button('Add')
        button.connect('clicked', self._addEntry)
        buttons.pack_start(button, True, True, 0)
        button = Gtk.Button('Update')
        button.connect('clicked', self._updateEntry)
        buttons.pack_start(button, True, True, 0)
        button = Gtk.Button('Delete')
        button.connect('clicked', self._deleteEntry)
        buttons.pack_start(button, True, True, 0)
        model = Gtk.ListStore(str, str)
        model.set_sort_column_id(0, Gtk.SortType.DESCENDING)
        for name, number in phonedata.data.items():
            model.append((name, number))
        self.view = Gtk.TreeView(model)
        nameColumn = Gtk.TreeViewColumn('Name')
        nameCellRenderer = Gtk.CellRendererText()
        nameColumn.pack_start(nameCellRenderer, False)
        nameColumn.add_attribute(nameCellRenderer, 'text', 0)
        numberColumn = Gtk.TreeViewColumn('Number')
        numberCellRenderer = Gtk.CellRendererText()
        numberColumn.pack_start(numberCellRenderer, False)
        numberColumn.add_attribute(numberCellRenderer, 'text', 1)
        self.view.append_column(nameColumn)
        self.view.append_column(numberColumn)
        self.view.connect('cursor-changed', self._setSelected)
        ui = Gtk.VBox(False, 15, border_width=10)
        ui.pack_start(data, True, True, 0)
        ui.pack_start(buttons, True, True, 0)
        ui.pack_start(self.view, True, True, 0)
        self.add(ui)
        self.show_all()

    def _setSelected(self, view):
        model, iterator = view.get_selection().get_selected()
        self.nameEntry.set_text(model.get_value(iterator, 0))
        self.numberEntry.set_text(model.get_value(iterator, 1))

    def __displayDialog(self, type, message):
        dialog = Gtk.MessageDialog(self, type=type, buttons=Gtk.ButtonsType.CLOSE, message_format=message)
        dialog.connect('response', lambda d, response: d.destroy())
        dialog.show()

    def __searchFor(self, name):
        model, iterator = self.view.get_selection().get_selected()
        if iterator is not None:
            assert model.get(iterator, 0) == name
            found = True
        else:
            iterator = model.get_iter_first()
            found = model.get(iterator, 0)[0] == name
            while not found:
                iterator = model.iter_next(iterator)
                if iterator is None:
                    break
                found = model.get(iterator, 0)[0] == name
        return found, model, iterator

    def _addEntry(self, event):
        '''
        Process an add button press.  Append the new data from the data entry boxes to the data model,
        but only if there is actually data in the data entry boxes.
        '''
        name = self.nameEntry.get_text()
        number = self.numberEntry.get_text()
        if(name != ''):
            found, model, iterator = self.__searchFor(name)
            if found:
                self.__displayDialog(Gtk.MessageType.ERROR, '''
The name
{}
is already in the phonebook,
it cannot be added again.
'''.format(name))
            else:
                model.append((name, number))
        else:
            self.__displayDialog(Gtk.MessageType.WARNING, '''
The name field is empty,
no entry to be added.
''')

    def _updateEntry(self, event):
        '''
        Process an update button press.  Replace the current selected item with the data from the data
        entry text boxes, but only if there is data in the data entry boxes.
        '''
        name = self.nameEntry.get_text()
        number = self.numberEntry.get_text()
        if(name != ''):
            found, model, iterator = self.__searchFor(name)
            if found:
                model.set_value(iterator, 1, number)
            else:
                self.__displayDialog(Gtk.MessageType.WARNING, '''
The name
{}
was not found so could
not be updated.
'''.format(name))
        else:
            self.__displayDialog(Gtk.MessageType.WARNING, '''
The name field is empty,
no entry to be updated.
''')

    def _deleteEntry(self, event):
        '''
        Process a delete entry button press.  Delete the currently selected item from the data model and
        clear the data entry boxes.
        '''
        # The following sequence really ought to be an atomic operation!
        name = self.nameEntry.get_text()
        model, iterator = self.view.get_selection().get_selected()
        if name != '':
            found, model, iterator = self.__searchFor(name)
            if found:
                model.remove(iterator)
                self.nameEntry.set_text('')
                self.numberEntry.set_text('')
            else:
                self.__displayDialog(Gtk.MessageType.WARNING, '''
The name
{}
was not found so could
not be deleted.
'''.format(name))
        else:
            self.__displayDialog(Gtk.MessageType.WARNING, '''
The name field is empty,
no entry to be deleted.
''')


if __name__ == '__main__':
    PhoneFrame()
    sys.exit(Gtk.main())
