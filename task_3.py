import datetime
import random
class DateFormatError(Exception):
    pass


class Stage:
    def __init__(self,cost, begin, end, description):
        self.cost = cost
        self.begin = self.true_date(begin)
        self.end = self.true_date(end)
        self.status = "запланирован"
        self.description = description
        self.next_stage = None
        self.prev_stage = None


    def true_date(self, date):
        try:
            return datetime.datetime.strptime(date, "%d.%m.%Y")
        except:
            raise DateFormatError("Неправильный формат даты")

    def next(self):
        if self.next_stage:
            self.status = "выполнен"
            self.next_stage.status = "осуществляется"
            return self.next_stage
        return None

    def prev(self):
        if self.prev_stage:
            self.status = "запланирован"
            self.prev_stage.status = "осуществляется"
            return self.prev_stage
        return None

    def start(self):
        self.status = "осуществляется"

    def stop(self):
        self.status = "выполнен"

    def reject(self):
        self.status = "забракован"

class Project(Stage):
    pass

class Foundation(Stage):
   pass

class Walls(Stage):
    pass

class Roof(Stage):
   pass

class Finishing(Stage):
    pass

class Construction:
    def __init__(self):
        self.stages = []
        self.setup_stages()

    def setup_stages(self):
        stages = [
            Project(10000, "01.01.2025", "10.01.2025", "Проектирование"),
            Foundation(20000, "11.01.2025", "20.01.2025", "Заливка Фундамент"),
            Walls(30000, "21.01.2025", "30.01.2025", "Возведение стен"),
            Roof(15000, "31.01.2025", "10.02.2025", "Крыша"),
            Finishing(25000, "11.02.2025", "20.02.2025", "Отделочные работы")
        ]
        for i in range(len(stages) - 1):
            stages[i].next_stage = stages[i + 1]
            stages[i + 1].prev_stage = stages[i]
        self.stages = stages

    def run(self):
        current_stage = self.stages[0]
        current_stage.start()
        while current_stage:
            if random.random() < 0.15:
                current_stage.reject()
                if current_stage.prev_stage:
                    current_stage = current_stage.prev()
                else:
                    return "Стройка отменена"
            else:
                current_stage.stop()
                current_stage = current_stage.next()
        return "Стройка завершена успешно"

def simulate_construction(runs=1000):
    success_count = 0
    for _ in range(runs):
        construction = Construction()
        if construction.run() == "Стройка завершена успешно":
            success_count += 1
    success_rate = (success_count / runs) * 100
    print(f"Вероятность успешного завершения: {success_rate:}%")
simulate_construction()





