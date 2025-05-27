from datetime import datetime

from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from database import models
from screens.AddTaskDialog import AddTaskDialog


Builder.load_file("kv/home_screen.kv")

class HomeScreen(MDScreen):
    dialog = None

    def on_kv_post(self, base_widget):

        self.acc_date = self.set_accuall_date()
        self.ids.header.title = f"Dziś: {self.acc_date}"
        models.read_tasks_from_db_by_date(self, self.acc_date)


    def open_add_task_dialog(self):
        if not self.dialog:
            self.dialog = AddTaskDialog(self)
        self.dialog.open()

    def refresh_tasks(self):
        self.ids.task_list.clear_widgets()
        models.read_tasks_from_db_by_date(self, self.acc_date)


    def set_accuall_date(self):
        date = datetime.now().strftime("%Y-%m-%d")
        return date




