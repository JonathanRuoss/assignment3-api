class BmiCalculator():
    def __init__(self, heightFt, heightIn, weight):
        self.heightFt = heightFt
        self.heightIn = heightIn
        self.weightLbs = weight
    
    def getBmiVal(self):
        heightImp = (self.heightFt * 12) + self.heightIn
        heightMet = heightImp * 0.025
        weightKgs = self.weightLbs * 0.45

        bmiVal = weightKgs / (heightMet**2)
        bmiVal = round(bmiVal, 1)

        return bmiVal

    def getBmiCat(self):
        bmiVal = self.getBmiVal()

        if bmiVal < 18.5:
            bmiCat = "Underweight"
        elif 18.5 <= bmiVal and bmiVal < 25:
            bmiCat = "Normal weight"
        elif 25 <= bmiVal and bmiVal < 30:
            bmiCat = "Overweight"
        elif 30 <= bmiVal:
            bmiCat = "Obese"

        return bmiCat