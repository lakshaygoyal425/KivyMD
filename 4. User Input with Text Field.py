from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder

username_helper = """
MDTextField:
    hint_text: "Enter Username"
    helper_text: "Or Click on Forgot Username"
    helper_text_mode: "on_focus"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x: None
    width: 300
"""


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = Screen()
        username = Builder.load_string(username_helper)
        screen.add_widget(username)
        return screen


MainApp().run()
