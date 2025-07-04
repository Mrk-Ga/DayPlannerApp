from datetime import datetime, timedelta

from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from database import crud
from screens.addTaskDialog import AddTaskDialog
from screens.calendar import Calendar
from screens.eventBus import EventBus
from screens.taskBox import TaskBoxFactory

Builder.load_file("./kv/home_screen.kv")

class HomeScreen(MDScreen):
    dialog = None

    def on_kv_post(self, base_widget):  #start screen with today date and tasks
        EventBus.subscribe("tasks_updated", self.refresh_tasks)
        self.acc_date = datetime.now().strftime("%Y-%m-%d")
        self.ids.headerTitle.text = f"Dzień: {self.acc_date}"
        EventBus.emit("tasks_updated")


    def open_add_task_dialog(self): #opening dialog to add task
        if not self.dialog:
            self.dialog = AddTaskDialog(self)
        self.dialog.open()

    def open_month_calendar(self): #opening month calendar to change acc day
        Calendar(self)

    def open_today_tasks(self): #back to today day and tasks
        self.acc_date = datetime.now().strftime("%Y-%m-%d")
        self.ids.headerTitle.text = f"Dzień: {self.acc_date}"
        EventBus.emit("tasks_updated")

    #method used to change days with arrows at homeScreen topAppBar
    def change_date(self,days):
        date_obj = datetime.strptime(self.acc_date, "%Y-%m-%d").date()

        new_date = date_obj + timedelta(days=days)
        new_date_str = new_date.strftime("%Y-%m-%d")
        self.acc_date = new_date_str
        self.ids.headerTitle.text = f"Dzień: {self.acc_date}"
        EventBus.emit("tasks_updated")


    def refresh_tasks(self):    #refreshing tasks refered to acc_date (change by running)
        self.ids.task_list.clear_widgets()
        for task in crud.get_tasks_by_date(self.acc_date):
            taskBox= TaskBoxFactory.create(task, self)

            self.ids.task_list.add_widget(taskBox)





