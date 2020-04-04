class RetirementCalculator():
    def __init__(self, age, salary, percentage, goal):
        self.currentAge = age
        self.salary = salary
        self.percentage = percentage
        self.savingsGoal = goal

    def getFinalAge(self):
        age = 0
        savings = 0

        while savings < self.savingsGoal:
            savings += self.salary * (self.percentage / 100) * 1.35
            age += 1

        finalAge = self.currentAge + age

        return finalAge

    def getGoalMet(self):
        finalAge = self.getFinalAge()

        if finalAge < 100:
            return True
        else:
            return False
