from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window

Window.size = (360, 600)

screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Demo Application'
            left_action_items: [["menu",lambda x: app.navigation_draw()]]
            right_action_items: [["dots-vertical", lambda x: app.navigation_draw()], ["clock", lambda x: app.navigation_draw()]]
            elevation: 11
        MDLabel:
            text: 'Hello World'
            halign: 'center'
        MDBottomAppBar:
            MDToolbar:
                title: 'Help'
                left_action_items: [["coffee",lambda x: app.navigation_draw()]]
                mode: 'end'
                type: 'bottom'
                on_action_button: app.navigation_draw()
"""


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = Builder.load_string(screen_helper)
        return screen

    def navigation_draw(self):
        print("Navigation")


MainApp().run()
