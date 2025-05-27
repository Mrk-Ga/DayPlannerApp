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

from screens.DatePicker import DatePicker

Builder.load_file("kv/task_box.kv")

class TaskBox(MDCard):

    def __init__(self, parentScreen, taskIdFromDB, text, **kwargs):
        super().__init__(**kwargs)
        self.parentScreen = parentScreen
        self.ids.task_label.text = str(text)
        self.taskID = taskIdFromDB

    def change_task_date(self, *args):
        DatePicker(self.parentScreen, self.taskID)


    def check_slider_value(self, value):
        if value == 100:
            print('task completed!')