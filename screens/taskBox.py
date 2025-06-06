from datetime import timedelta, datetime
from kivymd.uix.card import MDCard
from kivy.lang import Builder

from database import models, crud
from screens.datePicker import DatePicker
from screens.eventBus import EventBus

Builder.load_file("./kv/task_box.kv")

###Factory Pattern used when creating multiple boxes with tasks
class TaskBoxFactory:
    @staticmethod
    def create(task, parent_screen):
        return TaskBox(
            parentScreen=parent_screen,
            taskIdFromDB=task.id,
            text=task.name,
            progress=task.progress,
            completed=task.completed
        )

class TaskBox(MDCard):

    def __init__(self, parentScreen, taskIdFromDB, text, progress=0, completed=False, **kwargs):
        super().__init__(**kwargs)
        self.parentScreen = parentScreen
        self.ids.task_label.text = str(text)
        self.taskID = taskIdFromDB
        self.refresh_from_db()

    def change_task_date(self, *args):
        DatePicker(self.parentScreen, self.taskID)

    def change_date_to_next_day(self):
        date_obj = datetime.strptime(self.parentScreen.acc_date, "%Y-%m-%d").date()
        new_date = date_obj + timedelta(days=1)
        new_date_str = new_date.strftime("%Y-%m-%d")

        crud.update_task_date(self.taskID, new_date_str)
        EventBus.emit("tasks_updated")

    def remove_task(self):
        crud.remove_task(self.taskID)
        EventBus.emit("tasks_updated")

    def check_slider_value(self, value):
        crud.set_task_progress(self.taskID, value)
        print(value)
        self.refresh_from_db()

    def refresh_from_db(self):
        task = crud.get_task_by_id(self.taskID)
        if task:
            self.progress = task.progress
            self.completed = task.completed
            self.ids.task_slider.value = task.progress
            if task.completed:
                self.md_bg_color = (0.6, 1, 0.6, 1)
            else:
                self.md_bg_color = (1,1,1,1)

