from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# List in python to test the API
employees=[
   {
        'id': 0,
        'lastName': 'Meryem',
        'firstName': 'Bentaleb',
        'emailId': 'meryembent@gmail.com'
    },
    {
        'id': 1,
        'lastName': 'Hassna',
        'firstName': 'hassnaoui',
        'emailId': 'hassnaoui@gmail.com'
    },
    {
        'id': 2,
        'lastName': 'Bouchra',
        'firstName': 'Aliout',
        'emailId': 'Bibouch@gmail.com'
    },
    {
        'id': 3,
        'lastName': 'Ayoub',
        'firstName': 'El Jadil',
        'emailId': 'ayoubel@gmail.com'
    },
    {
        'id': 4,
        'lastName': 'Katherine',
        'firstName': 'Derin',
        'emailId': 'dkatherine@gmail.com'
    }
]

#Method GET on all employees
@app.route('/api/v1/employees', methods=['GET'])
def manage_employees():
    return jsonify(employees)

#Method POST to create user
@app.route('/api/v1/employees', methods=['POST'])
def create_employees():
    new_employee = {
            'id': employees[-1]['id'] + 1,
            'lastName': request.json['lastName'],
            'firstName': request.json['firstName'],
            'emailId': request.json['emailId']
        }
    employees.append(new_employee)
    return jsonify(new_employee), 201


#Method GET employees with ID
@app.route('/api/v1/employees/<int:id>', methods=['GET'])
def get_entry(id):
    # Rechercher l'entrée avec l'ID spécifié
    for entry in employees:
        if entry['id'] == id:
            return jsonify(entry)
    # Si l'entrée n'a pas été trouvée   
    return jsonify({'error': 'L\'entree n\'a pas ete trouvee.'}), 404

#Method DELETE employees with ID
@app.route('/api/v1/employees/<int:id>', methods=['DELETE'])
def delete_entry(id):
    # Find entry in employees with the ID
    for entry in employees:
        if entry['id'] == id:
            employees.remove(entry) 
            return jsonify({'message': 'L\'entree a été supprimee.'})
    # If entry not find
    return jsonify({'error': 'L\'entree n\'a pas ete trouvee.'}), 404

#Method PUT modify emp data with ID
@app.route('/api/v1/employees/<int:id>', methods=['PUT'])
def modify_user(id):
    for entry in employees:
        if entry['id'] == id:
            entry['lastName'] = request.json['lastName']
            entry['firstName'] = request.json['firstName']
            entry['emailId'] = request.json['emailId']
            return jsonify({'message': 'User updated successfully.'}), 200
    return jsonify({'message': 'User not found.'}), 404

if __name__ == '__main__':
    app.run(debug=True)
