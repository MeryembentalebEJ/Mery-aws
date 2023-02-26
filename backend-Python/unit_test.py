import unittest
from app import app, employees

class TestAPI(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_get_all_employees(self):
        response = self.client.get('/api/v1/employees')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), len(employees))

    def test_get_employee_id(self):
        id_to_get = 3 
        response = self.client.get(f"/api/v1/employees/{id_to_get}")
        self.assertEqual(response.status_code, 200)

    def test_create_employee(self):
        employee = {
            'id': employees[-1]['id'] + 1,
            'lastName': 'Test',
            'firstName': 'Employee',
            'emailId': 'test.employee@example.com'
        }
        response = self.client.post('/api/v1/employees', json=employee)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, employee)
        self.assertEqual(len(employees), len(employees))

    def test_modify_employee(self):
        employee = employees[0]
        modified_employee = {
            'lastName': 'Test',
            'firstName': 'Employee',
            'emailId': 'test.employee@example.com'
        }
        response = self.client.put(f"/api/v1/employees/{employee['id']}", json=modified_employee)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'User updated successfully.'})
        employee = next((x for x in employees if x['id'] == employee['id']), None)
        self.assertEqual(employee['lastName'], 'Test')
        self.assertEqual(employee['firstName'], 'Employee')
        self.assertEqual(employee['emailId'], 'test.employee@example.com')

    def test_delete_employee(self):
        id_to_delete = 1  # Replace with an ID that exists in your employees list
        
        # Make a DELETE request to the API endpoint
        response = self.client.delete(f'/api/v1/employees/{id_to_delete}')
        
        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check that the entry with the specified ID was removed from the employees list
        for entry in employees:
            self.assertNotEqual(entry['id'], id_to_delete)

#closing open files or network connections, resetting global variables, or deleting temporary files.
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()