from flask import Flask, jsonify, request
from flask.views import MethodView
from common.ma import ma

app = Flask(__name__)

class EmployeeSchema(ma.Schema):
    jobTitle = ma.Str(required=True)
    firstName = ma.Str(required=True)
    lastName = ma.Str(required=True)

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


class EmployeeAPI(MethodView):
    def get(self, employee_id):
        if employee_id is None:
            # return a list of employees
            return jsonify(employee_data)
        elif employee_id <= 0:
            return {'message': 'employees_id must greater 1.'}
        else:
            # user_id always greater 1
            for e in employee_data['Employees']:
                if e['userId'] == employee_id:
                    return e

    def post(self):
        # create a new employee
        json_data = request.get_json(force=True)
        print(json_data)
        result = EmployeeSchema().load(json_data)

        if len(result.errors) > 0:
            return result.errors, 433
        
        employee = {
            'jobTitle': result['jobTitle'],
            'firstName': result['firstName'],
            'lastName': result['lastName']
        }

        employee_data['Employees'].append(employee)
        
        return {'message': 'Add Success'}

    def delete(self):
        pass

    def put(self):
        pass



employee_view = EmployeeAPI.as_view('employee_api')
app.add_url_rule('/employees/', defaults={'employee_id': None},
                 view_func=employee_view, methods=['GET',])
app.add_url_rule('/employees/', view_func=employee_view, methods=['POST',])
app.add_url_rule('/employees/<int:employee_id>', view_func=employee_view,
                 methods=['GET', 'PUT', 'DELETE'])


if __name__ == '__main__':
    app.run(debug=True)
