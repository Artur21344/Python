class StepCounter:
    daily_norm = 10000

    def __init__(self, name, steps):
        self.name = name
        self.steps = steps

    @staticmethod
    def check_norm(steps):
        return steps > StepCounter.daily_norm

    def __str__(self):
        return f"Користувач: {self.name}, кроки за день: {self.steps}"


user = StepCounter("Олена", 12000)

print(user)
print("Ціль досягнута" if StepCounter.check_norm(user.steps) else "Ціль не досягнута")