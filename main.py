# Python 3.8 kivy 2.0.0
# Критически важно, чтобы название kv файла не совпадало с walletapp
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivymd.uix.card import MDCard

class ElementCard(MDCard):
    def show_qr(self):
        app = MDApp.get_running_app()
        result_widget = app.root.ids.user_page.ids.screen_1
        background = app.root.ids.user_page
        app.disable_navigation(2, 3, True)
        background.opacity = 0.1
        qr_page = QrPage()
        result_widget.add_widget(qr_page)

class QrPage(MDCard):
    def hide_qr(self):
        app = MDApp.get_running_app()
        result_widget = app.root.ids.user_page.ids.screen_1
        app.disable_navigation(2, 3, False)
        result_widget.remove_widget(self)
        background = app.root.ids.user_page
        background.opacity = 1
        

class LoginPage(Screen):
    pass

class UserPage(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

class WalletApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('alfawalletapp.kv')

    def add_card(self):
        app = MDApp.get_running_app()
        result_widget = app.root.ids.user_page.ids.card_list
        result_widget.add_widget(ElementCard())

    def disable_navigation(self, page1, page2, status):
        app = MDApp.get_running_app()
        if status == True:
            if (page1, page2) == (2, 3):
                app.root.ids.user_page.ids.navigation_bottom_2.disabled = True
                app.root.ids.user_page.ids.navigation_bottom_3.disabled = True
        else:
            if (page1, page2) == (2, 3):
                app.root.ids.user_page.ids.navigation_bottom_2.disabled = False
                app.root.ids.user_page.ids.navigation_bottom_3.disabled = False

if __name__ == "__main__":
    WalletApp().run()