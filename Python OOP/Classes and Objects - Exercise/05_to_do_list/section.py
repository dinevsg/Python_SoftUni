from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.cleaned = 0

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        try:
            task = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        task.completed = True

        return f"Completed task {task_name}"
        # if task_name not in self.tasks:
        #     return f"Could not find task with the name {task_name.name}"
        #
        # task_name.completed = True
        # return f"Completed task {task_name.name}"

    def clean_section(self):
        for t in self.tasks:
            if task.completed:
                self.cleaned += 1
                self.tasks.remove(t)

        return f"Cleared {self.cleaned} tasks."

        # tasks_count = len(self.tasks)
        #
        # self.tasks.clear()
        #
        # return f"Cleared {tasks_count} tasks."
        # origin = len(self.tasks)
        # for t in self.tasks.copy():
        #     if t.completed:
        #         self.tasks.remove(t)
        #
        # return f"Cleared {origin - len(self.tasks)} tasks."

    def view_section(self):
        prr = "\n".join([t.details() for t in self.tasks])
        return f"Section {self.name}:\n" + \
               f"{prr}"


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.complete_task("Make bed"))
print(section.clean_section())
print(section.view_section())






