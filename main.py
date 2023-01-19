# Python 3.8 kivy 2.0.0

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder

class LoginPage(Screen):
    pass

class UserPage(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

class MainWindow(MDBoxLayout):
    pass

class WalletApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('walletapp.kv')


if __name__ == "__main__":
    WalletApp().run()