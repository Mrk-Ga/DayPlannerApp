from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.screen import MDScreen
from database import models

class Calendar(MDScreen):
    def __init__(self, parentScreen, **kwargs):
        super().__init__(**kwargs)
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save= self.change_acc_date)
        date_dialog.open()
        self.parentScreen = parentScreen

    def change_acc_date(self, instance, date, range):
        self.parentScreen.acc_date = date
        self.parentScreen.refresh_tasks()
        instance.dismiss()