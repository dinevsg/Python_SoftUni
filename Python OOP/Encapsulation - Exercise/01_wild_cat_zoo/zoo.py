from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        is_capacity = self.__animal_capacity > len(self.animals)
        is_budget = self.__budget >= price
        if is_budget and is_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif is_capacity and not is_budget:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        if self.__budget >= sum(w.salary for w in self.workers):
            self.__budget -= sum(w.salary for w in self.workers)
            return f"You payed your workers. They are happy. "\
                   f"Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        if self.__budget >= sum(a.money_for_care for a in self.animals):
            self.__budget -= sum(a.money_for_care for a in self.animals)
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]

        res = f"You have {len(self.animals)} animals\n"

        res += f"----- {len(lions)} Lions:\n"
        for li in lions:
            res += f"{li}\n"

        res += f"----- {len(tigers)} Tigers:\n"
        for ti in tigers:
            res += f"{ti}\n"

        res += f"----- {len(cheetahs)} Cheetahs:\n"
        for ch in cheetahs:
            res += f"{ch}\n"

        return res[:-1]

    def workers_status(self):
        keepers = [a for a in self.workers if a.__class__.__name__ == "Keeper"]
        caretakers = [a for a in self.workers if a.__class__.__name__ == "Caretaker"]
        vets = [a for a in self.workers if a.__class__.__name__ == "Vet"]

        res = f"You have {len(self.workers)} workers\n"

        res += f"----- {len(keepers)} Keepers:\n"
        for ke in keepers:
            res += f"{ke}\n"

        res += f"----- {len(caretakers)} Caretakers:\n"
        for ca in caretakers:
            res += f"{ca}\n"

        res += f"----- {len(vets)} Vets:\n"
        for ve in vets:
            res += f"{ve}\n"

        return res[:-1]
