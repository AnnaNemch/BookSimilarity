import os

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

from libs.navigationdrawer import NavigationDrawer
from kivymd.theming import ThemeManager

from features import BookList, MainScreenManagement, BookScreenManagement
from config import KV_DIR
from ui import StartScreen, SearchBookScreen, AddBookScreen, SearchAuthorScreen, SearchTopicScreen, AboutScreen


class Navigator(NavigationDrawer):
    title = StringProperty('Navigation')


class BookStoreApp(App, MainScreenManagement, BookList, BookScreenManagement):
    theme_cls = ThemeManager()
    nav_drawer = ObjectProperty()

    def build(self):
        self.load_all_view_files(KV_DIR)

        self.main_screen = StartScreen()
        self.nav_drawer = Navigator()

        self.main_screen_manager = self.main_screen.ids.main_manager

        # setting up menu links

        self.screens = [SearchBookScreen(name="search_book"),
                        AddBookScreen(name="add_book"),
                        SearchAuthorScreen(name="search_author"),
                        SearchTopicScreen(name="search_topic"),
                        AboutScreen(name="about")]

        btn = Button(text="suka")
        # self.screens[0].add_widget(btn)
        self.main_screen_manager.add_widget(self.screens[0])
        self.main_screen_manager.add_widget(self.screens[1])
        self.main_screen_manager.add_widget(self.screens[2])
        self.main_screen_manager.add_widget(self.screens[3])
        self.main_screen_manager.add_widget(self.screens[4])
        # self.book_screen_manager = self.root.ids.book_manager
        # self.book_screen_manager = self.main_screen.ids.book_manager

        return self.main_screen

    def load_all_view_files(self, directory_kv_files):
        for kv_file in os.listdir(directory_kv_files):
            kv_file = os.path.join(directory_kv_files, kv_file)
            if os.path.isfile(kv_file):
                with open(kv_file) as kv:
                    Builder.load_string(kv.read())


    def add_screens(self, name_screen, screen_manager, new_screen):
        screen = Screen(name=name_screen)
        screen.add_widget(new_screen)
        screen_manager.add_widget(screen)
        screen_manager.current = name_screen

    # Navigation menu links
    def show_about(self, *args):
        self.root.ids.main_manager.current = "about"
        return True

    def show_search_book(self, *args):
        self.root.ids.main_manager.current = "search_book"
        return True

    def show_add_book(self, *args):
        self.root.ids.main_manager.current = "add_book"
        return True

    def show_search_author(self, *args):
        self.root.ids.main_manager.current = "search_author"
        return True

    def show_search_topic(self, *args):
        self.root.ids.main_manager.current = "search_topic"
        return True


BookStoreApp().run()
