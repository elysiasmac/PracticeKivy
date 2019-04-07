import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget


class Container(Widget):
    pass


class Lyber(App):
    def build(self):
        return Container()


if __name__ == "__main__":
    Lyber().run()
