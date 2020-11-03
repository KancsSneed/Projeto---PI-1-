from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Adicionador(BoxLayout):
    pass

class Interface(App):
    def build(self):
        return Adicionador()

Interface().run()