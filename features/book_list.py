import os
import types

from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from ui import Lists, RightButton, card, BookListScreen
import kivymd.snackbar as Snackbar
from ui.dialogs import file_dialog


class BookList(object):
    def navigate_to_book(self, book_id=''):
        if book_id == '':
            return
        mgr = self.root.ids.main_manager
        similar_books = self.screens[0].ids.similar_books

        if not hasattr(self, 'scr'):
            self.scr = Screen(name="test")
            mgr.add_widget(self.scr)

        grid = GridLayout(cols=1)
        grid.id = "mygrid"

        grid.add_widget(Button(text='My first button'))
        grid.add_widget(Button(text='My first button'))
        self.scr.add_widget(grid)
        mgr.current = "test"
        print('navigated')

    def show_book_list(self):

        # some search of books
        books_id = [i for i in range(0, 4)] # some users list
        # //

        self.screens[0].ids.similar_books.clear_widgets()

        for val in books_id:
            label = Button(text=str(val), font_size=14)
            label.background_color = self.theme_cls.primary_dark
            label.on_press = lambda *args: self.navigate_to_book(str(val), *args)

            self.screens[0].ids.similar_books.add_widget(label)

        print('book_search')
        # mgr = self.root.ids.main_manager
        # similar_books = self.root.ids.search_book.ids.similar_books
        #
        # scr = Screen(name="test")
        #
        # grid = GridLayout(cols=1)
        # grid.id = "mygrid"
        # similar_books.add_widget(scr)
        #
        # grid.add_widget(Button(text='My first button'))
        # grid.add_widget(Button(text='My first button'))
        # scr.add_widget(grid)
        # # self.root.ids.main_manager.current = "test"
        # print('added')

    # def _event_book_item(self, *args):


    # def _show_book_info(self, name_contact):


