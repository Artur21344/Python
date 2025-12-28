class StepCounter:
    daily_norm = 4000

    def __init__(self, name, steps):
        self.name = name
        self.steps = steps

    @staticmethod
    def check_norm(steps):
        return steps >= StepCounter.daily_norm

    def __add__(self, other):
        return self.steps + other.steps

    def __str__(self):
        return f"Користувач: {self.name}, кроки: {self.steps}"


day1 = StepCounter("Артур", 7500)
day2 = StepCounter("Артур", 4200)

print(day1)
print(day2)

total_steps = day1 + day2
print("Загальна кількість кроків:", total_steps)

print(StepCounter.check_norm(total_steps))
