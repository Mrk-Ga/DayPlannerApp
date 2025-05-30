from datetime import timedelta, datetime

from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.slider import MDSlider

from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivymd.uix.slider import MDSlider
from kivy.lang import Builder
from kivy.metrics import dp

from database import models
from screens.DatePicker import DatePicker

Builder.load_file("kv/task_box.kv")

class TaskBox(MDCard):

    def __init__(self, parentScreen, taskIdFromDB, text, progress=0, completed=False, **kwargs):
        super().__init__(**kwargs)
        self.parentScreen = parentScreen
        self.ids.task_label.text = str(text)
        self.taskID = taskIdFromDB
        self.progress = progress
        self.completed = completed

        if completed:
            self.md_bg_color = (0, 0.5, 0, 1)  # np. zielony
        self.ids.task_slider.value = progress

    def change_task_date(self, *args):
        DatePicker(self.parentScreen, self.taskID)

    def change_date_to_next_day(self):
        print("zmieniam: ", type(self.parentScreen.acc_date))
        date_obj = datetime.strptime(self.parentScreen.acc_date, "%Y-%m-%d").date()
        new_date = date_obj + timedelta(days=1)
        new_date_str = new_date.strftime("%Y-%m-%d")

        models.update_task_date(self.taskID, new_date_str)
        self.parentScreen.refresh_tasks()

    def remove_task(self):
        models.remove_task(self.taskID)
        self.parentScreen.refresh_tasks()

    def check_slider_value(self, value):
        models.set_task_progress(self.taskID, value)

        if value == 100:
            print("Task completed!")
            self.md_bg_color = (0, 0.5, 0, 1)  # np. zielony
            models.set_task_if_completed(self.taskID, True)
        else:
            self.md_bg_color = (1, 1, 1, 1)  # np. zielony
            models.set_task_if_completed(self.taskID, False)
