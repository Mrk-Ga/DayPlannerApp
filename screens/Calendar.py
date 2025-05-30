from kivymd.uix.pickers import MDModalDatePicker
from kivymd.uix.screen import MDScreen
from database import models
#from kivymd.uix.pickers import MDModalDatePicker
import kivymd.uix.pickers

class Calendar(MDScreen):
    def __init__(self, parentScreen, **kwargs):
        super().__init__(**kwargs)
        date_dialog = MDModalDatePicker()
        date_dialog.bind(on_ok= self.change_acc_date)
        date_dialog.bind(on_cancel= date_dialog.dismiss)
        date_dialog.open()
        self.parentScreen = parentScreen

    def change_acc_date(self, instance):
        print(instance.get_date()[0])
        self.parentScreen.ids.headerTitle.text = f"Dzień: {instance.get_date()[0].strftime("%Y-%m-%d")}"
        self.parentScreen.acc_date = instance.get_date()[0].strftime("%Y-%m-%d")
        self.parentScreen.refresh_tasks()
        instance.dismiss()
