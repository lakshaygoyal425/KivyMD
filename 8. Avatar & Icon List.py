from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, ThreeLineListItem, ThreeLineIconListItem, ThreeLineAvatarListItem
from kivymd.uix.list import IconLeftWidget, ImageLeftWidget
from kivy.uix.scrollview import ScrollView


class MainApp(MDApp):
    def build(self):
        screen = Screen()
        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)
        for i in range(1, 21):
            image = ImageLeftWidget(source="logo.jpeg")
            items = ThreeLineAvatarListItem(text='Item ' + str(i), secondary_text='Hello World',
                                            tertiary_text='Third Text')
            items.add_widget(image)
            list_view.add_widget(items)

        screen.add_widget(scroll)
        return screen


MainApp().run()
