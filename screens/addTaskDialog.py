from datetime import datetime, timedelta

from kivy.factory import Factory
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog

from database import models, crud
from screens.eventBus import EventBus

Builder.load_file("./kv/add_task_dialog.kv")

# class with content of MDDialog, defined in .kv file
class AddTaskContent(MDBoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.parentDialog = None


class AddTaskDialog:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.dates_to_add_tasks = [self.parent_screen.acc_date]

        self.dialog = Factory.AddTaskDialogUI(MDDialog) #building with kv file
        self.content = self.dialog.ids.task_content #access to dialog content
        self.content.parentDialog = self

    def open(self):
        self.dialog.open()

    def close(self, *args):
        self.dialog.dismiss()


    #adding task to parentScreen
    def add_task(self, *args):
        text = self.content.ids.task_input.text.strip()

        if text:
            for date in self.dates_to_add_tasks:
                task = models.Task(name=text, date=date)
                crud.add_task_to_db(task)
                self.close()
                EventBus.emit("tasks_updated")

    #adding task for same day in 4 weeks time
    def add_weekly_task(self, *args):
        dates = []
        date_obj = datetime.strptime(self.parent_screen.acc_date, "%Y-%m-%d").date()

        for weeks in range(0, 31, 7):
            new_date = date_obj + timedelta(days=weeks)
            new_date_str = new_date.strftime("%Y-%m-%d")
            dates.append(new_date_str)

        self.dates_to_add_tasks = dates
