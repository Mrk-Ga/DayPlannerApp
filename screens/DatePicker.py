from datetime import datetime

from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbar
from kivy.metrics import dp
import database.models as models



class DatePicker(MDScreen):

    def __init__(self, parentScreen, taskID, **kwargs):
        super().__init__(**kwargs)
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save= self.update_task_date)
        date_dialog.open()
        self.taskID = taskID
        self.parentScreen = parentScreen

    def update_task_date(self, instance, date, range):

        models.update_task_date(self.taskID, date.strftime("%Y-%m-%d"))
        self.parentScreen.refresh_tasks()
        instance.dismiss()





