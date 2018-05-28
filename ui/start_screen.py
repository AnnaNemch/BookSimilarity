from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager


class StartScreen(ScreenManager):
    events_callback = ObjectProperty(lambda: None)
