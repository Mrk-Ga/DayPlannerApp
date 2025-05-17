from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.slider import MDSlider
from kivymd.uix.list import IRightBodyTouch, OneLineListItem

from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivymd.uix.slider import MDSlider
from kivy.lang import Builder
from kivy.metrics import dp

Builder.load_file("kv/task_box.kv")

class TaskBox(MDCard):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.ids.task_label.text = str(text)

    def cofnij_ekran(self, *args):
        print("Kliknięto strzałkę!")