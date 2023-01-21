# Python 3.8 kivy 2.0.0
# Критически важно, чтобы название kv файла не совпадало с walletapp
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivymd.uix.card import MDCard
from kivy.core.window import Window
import barcode
# import pyvips

Window.size = (360, 800)

class ElementCard(MDCard):
    def show_qr(self):
        app = MDApp.get_running_app()
        result_widget = app.root.ids.user_page.ids.screen_1
        background = app.root.ids.user_page
        app.disable_cards(True)
        app.disable_navigation(2, 3, True)
        background.opacity = 0.1
        qr_page = QrPage()
        result_widget.add_widget(qr_page)

class QrPage(MDCard):
    def hide_qr(self):
        app = MDApp.get_running_app()
        result_widget = app.root.ids.user_page.ids.screen_1
        app.disable_cards(False)
        app.disable_navigation(2, 3, False)
        result_widget.remove_widget(self)
        background = app.root.ids.user_page
        background.opacity = 1

class ShopAddPage(MDCard):
    def hide_ShopAddPage(self):
        app = MDApp.get_running_app()
        result_widget = app.root.ids.user_page.ids.screen_2
        app.root.ids.user_page.ids.shop_screen.disabled = False
        app.disable_navigation(1, 3, False)
        result_widget.remove_widget(self)
        background = app.root.ids.user_page
        background.opacity = 1

class SettingsPage(MDCard):
    def hide_SettingsPage(self):
        app = MDApp.get_running_app()
        result_widget = app.root.ids.user_page.ids.screen_3
        app.root.ids.user_page.ids.settings_screen.disabled = False
        app.disable_navigation(1, 2, False)
        result_widget.remove_widget(self)
        background = app.root.ids.user_page
        background.opacity = 1

class ElementShop(MDCard):
    def show_card_adding(self):
        app = MDApp.get_running_app()
        result_widget = app.root.ids.user_page.ids.screen_2
        background = app.root.ids.user_page
        app.root.ids.user_page.ids.shop_screen.disabled = True
        app.disable_navigation(1, 3, True)
        background.opacity = 0.1
        qr_page = ShopAddPage()
        result_widget.add_widget(qr_page)

class LoginPage(Screen):
    pass
class RegistrationPage(Screen):
    pass
class UserPage(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

class WalletApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Red"
        return Builder.load_file('alfawalletapp.kv')

    def add_card(self):
        app = MDApp.get_running_app()
        result_widget = app.root.ids.user_page.ids.card_list
        result_widget.add_widget(ElementCard())

    def disable_navigation(self, page1, page2, status):
        app = MDApp.get_running_app()
        if status == True:
            if (page1, page2) == (1, 2):
                app.root.ids.user_page.ids.navigation_bottom_1.disabled = True
                app.root.ids.user_page.ids.navigation_bottom_2.disabled = True
            elif (page1, page2) == (2, 3):
                app.root.ids.user_page.ids.navigation_bottom_2.disabled = True
                app.root.ids.user_page.ids.navigation_bottom_3.disabled = True
            elif (page1, page2) == (1, 3):
                app.root.ids.user_page.ids.navigation_bottom_1.disabled = True
                app.root.ids.user_page.ids.navigation_bottom_3.disabled = True
        else:
            if (page1, page2) == (1, 2):
                app.root.ids.user_page.ids.navigation_bottom_1.disabled = False
                app.root.ids.user_page.ids.navigation_bottom_2.disabled = False
            elif (page1, page2) == (2, 3):
                app.root.ids.user_page.ids.navigation_bottom_2.disabled = False
                app.root.ids.user_page.ids.navigation_bottom_3.disabled = False
            elif (page1, page2) == (1, 3):
                app.root.ids.user_page.ids.navigation_bottom_1.disabled = False
                app.root.ids.user_page.ids.navigation_bottom_3.disabled = False

    def disable_cards(self, status):
        app = MDApp.get_running_app()
        if status == True:
            app.root.ids.user_page.ids.card_list.disabled = True
        else:
            app.root.ids.user_page.ids.card_list.disabled = False

    def show_SettingsPage(self):
        app = MDApp.get_running_app()
        result_widget = app.root.ids.user_page.ids.screen_3
        background = app.root.ids.user_page
        app.root.ids.user_page.ids.settings_screen.disabled = True
        app.disable_navigation(1, 2, True)
        background.opacity = 0.1
        settings_page = SettingsPage()
        result_widget.add_widget(settings_page)
    def qr_creator(self, number_barcode):
        barcode.PROVIDED_BARCODES
        ['code128', 'code39', 'ean', 'ean13', 'ean14', 'ean8', 'gs1', 'gs1_128', 'gtin', 'isbn', 'isbn10', 'isbn13', 'issn', 'itf', 'jan', 'pzn', 'upc', 'upca']
        if len(number_barcode) == 13:
            EAN = barcode.get_barcode_class('ean13')
            my_ean = EAN(number_barcode)
            save_name = my_ean.save('ean_barcode')
        if len(number_barcode) == 14:
            EAN = barcode.get_barcode_class('ean14')
            my_ean = EAN(number_barcode)
            save_name = my_ean.save('ean_barcode')
        # image = pyvips.Image.new_from_file("ean_barcode.svg", dpi=300)
        # image.write_to_file("x.jpg")


if __name__ == "__main__":
    WalletApp().run()