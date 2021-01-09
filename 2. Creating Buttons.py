from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton


class MainApp(MDApp):
    def build(self):
        screen = Screen()
        btn_flat = MDRectangleFlatButton(text='Hello World', pos_hint={'center_x':0.5, 'center_y':0.5})
        icon_btn = MDIconButton(icon='android', pos_hint={'center_x':0.5, 'center_y':0.5})
        screen.add_widget(icon_btn)
        return screen


MainApp().run()
