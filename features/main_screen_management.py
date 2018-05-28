from kivy.uix.screenmanager import ScreenManager

from ui import SearchBookScreen, AddBookScreen, SearchAuthorScreen, SearchTopicScreen, AboutScreen


class MainScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(MainScreenManagement, self).__init__(**kwargs)
