from flask import Flask, request
from flask_restful import Resource, Api

from BmiCalculator import BmiCalculator
from RetirementCalculator import RetirementCalculator

app = Flask(__name__)
api = Api(app)

class BmiCalculatorController(Resource):
    def post(self):
        requestParams = request.get_json()
        calculator = BmiCalculator(requestParams["heightFt"], requestParams["heightIn"], requestParams["weight"])
        return {'value': calculator.getBmiVal(), 'category': calculator.getBmiCat()}, 200

class RetirementCalculatorController(Resource):
    def post(self):
        requestParams = request.get_json()
        calculator = RetirementCalculator(requestParams["age"], requestParams["salary"], requestParams["percentage"], requestParams["goal"])
        return {'age': calculator.getFinalAge(), 'goalMet': calculator.getGoalMet()}, 200

api.add_resource(BmiCalculatorController, '/calculator/bmi')
api.add_resource(RetirementCalculatorController, '/calculator/retirement')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

if __name__ == '__main__':
    app.run(debug=False, port=80, host="0.0.0.0")