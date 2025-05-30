from datetime import datetime, timedelta

from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import partial
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout

from database import models
from screens import HomeScreen
from screens.TaskBox import TaskBox

class AddTaskContent(MDBoxLayout):

    def __init__(self, parentDialog, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parentDialog = parentDialog

    def add_weekly_task(self, *args):
        print("adding weekly task")
        dates = []
        date_obj = datetime.strptime(self.parentDialog.parent_screen.acc_date, "%Y-%m-%d").date()

        for weeks in range(0, 31, 7):
            new_date = date_obj + timedelta(days=weeks)
            new_date_str = new_date.strftime("%Y-%m-%d")
            dates.append(new_date_str)


        self.parentDialog.dates_to_add_tasks = dates


Builder.load_file("kv/add_task_dialog.kv")

class AddTaskDialog:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.content = AddTaskContent(self)

        self.dates_to_add_tasks = [self.parent_screen.acc_date]



        #this must be declarated here in code, because .kv file couldn't handle it...
        self.dialog = MDDialog(
            title="Dodaj zadanie",
            type="custom",
            auto_dismiss=False,
            content_cls=self.content,
            buttons=[
                Factory.MDFlatButton(text="Anuluj", on_release=self.close),
                Factory.MDFlatButton(text="Dodaj",
                on_release=self.add_task)
            ]
        )

    def open(self):
        self.dialog.open()

    def close(self, *args):
        self.dialog.dismiss()


    def add_task(self, *args):
        text = self.content.ids.task_input.text.strip()

        if text:
            for date in self.dates_to_add_tasks:
                task = models.Task(name=text, date=date)
                models.add_task_to_db(task)
                self.close()
                self.parent_screen.refresh_tasks()