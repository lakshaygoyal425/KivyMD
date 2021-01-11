from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang.builder import Builder
from helpers import username_helper


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = Screen()
        button = MDRectangleFlatButton(text='SHOW', pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                       on_release=self.show_data)
        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        if self.username.text is "":
            check_string = "Please Enter Username"
        else:
            check_string = self.username.text + 'does not exist'
        close_button = MDFlatButton(text="CLOSE", on_release=self.close_dialog)
        more_button = MDFlatButton(text="MORE")
        self.dialog = MDDialog(title='USERNAME CHECK', text=check_string,
                               size_hint=(0.7, 1),
                               buttons=[close_button, more_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


MainApp().run()
