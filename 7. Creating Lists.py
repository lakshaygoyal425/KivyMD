from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem, ThreeLineListItem
from kivy.uix.scrollview import ScrollView


class MainApp(MDApp):
    def build(self):
        screen = Screen()
        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)
        for i in range(1, 21):
            items = ThreeLineListItem(text='Item ' + str(i), secondary_text='Hello World',
                                    tertiary_text='Third Text')
            list_view.add_widget(items)

        screen.add_widget(scroll)
        return screen


MainApp().run()
