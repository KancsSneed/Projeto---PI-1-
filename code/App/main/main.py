from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        button1 = Button(text='Button1')
        label1 = Label(text='Label 1')
        box.add_widget(button1)
        box.add_widget(label1)
        return box

TestApp().run()