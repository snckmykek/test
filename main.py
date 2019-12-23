# __version__ = "0.0.1"
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MainBoxLayout(BoxLayout):

    def __init__(self, **kwargs):
        super(MainBoxLayout, self).__init__(**kwargs)


class MainScreenApp(App):

    def __init__(self, **kwargs):
        super(MainScreenApp, self).__init__(**kwargs)

    def build(self):
        box = MainBoxLayout()
        box.add_widget(Button(text='1', color=(0, 1, 0, 1)))
        box.add_widget(Button(text='2'))
        box.add_widget(Button(text='3'))
        return box


if __name__ == "__main__":
    MainScreenApp().run()
