from flask import Flask
from flask_restful import Resource, Api, abort, reqparse

app = Flask(__name__)
api = Api(app)

employee_data = {
    "Employees": [
        {
            "userId": 1,
            "jobTitle": "Developer",
            "firstName": "Kris",
            "lastName": "Lee",
        },
        {
            "userId": 2,
            "jobTitle": "Developer",
            "firstName": "David",
            "lastName": "Rome",
        },
        {
            "userId": 3,
            "jobTitle": "Program Directory",
            "firstName": "Tin",
            "lastName": "Jonson",
        }
    ]
}

parser = reqparse.RequestParser()
parser.add_argument('jobTitle', type=str,
                    help="JobTitle of the employee is required", required=True)
parser.add_argument('firstName', type=str,
                    help="firstName of the employee is required", required=True)
parser.add_argument('lastName', type=str,
                    help="lastName of the employee is required", required=True)

def abort_if_employee_not_exist(employee):
    if not employee:
        return abort(404, message='Employee not exist...')

class EmployeeApi(Resource):
    def get(self, employee_id):
        employee = [e for e in employee_data["Employees"] if e['userId'] == employee_id]
        abort_if_employee_not_exist(employee)

        return employee
    
    def delete(self, employee_id):
        for i, e in enumerate(employee_data["Employees"]):
            if e['userId'] == employee_id:
                abort_if_employee_not_exist(e)
                del employee_data["Employees"][i]
                return {}

class EmployeeList(Resource):
    def get(self):
        return employee_data["Employees"]

    def post(self):
        args = parser.parse_args()
        employee_id = int(len(employee_data["Employees"])+1)
        new_employee = {
            "userId": employee_id,
            "jobTitle": args['jobTitle'],
            "firstName": args['firstName'],
            "lastName": args['lastName']
        }
        employee_data["Employees"].append(new_employee)
        return new_employee


api.add_resource(EmployeeList, '/employees')
api.add_resource(EmployeeApi, '/employees/<int:employee_id>')

if __name__ == '__main__':
    app.run(debug=True)
