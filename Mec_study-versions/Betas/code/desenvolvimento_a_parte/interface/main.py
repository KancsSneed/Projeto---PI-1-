from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class Tarefas(ScrollView):
    def __init__(self, tarefas,**kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            #self.ids.box.add_widget()
class Tarefa(BoxLayout):
    def __init__(self,tarefas,text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text
class Interface(App):
    def build(self):
        return Tarefas(['Atividade','Fazer compras', 'Buscar o filho','Atividade','Fazer compras', 'Buscar o filho','Atividade','Fazer compras', 'Buscar o filho'])
Interface().run()