from flask import Flask, jsonify, request
from db_connections.connections import session
from models.table import School_table

app = Flask(__name__)


# Give all schools
@app.route('/get_all_schools_list', methods=['GET'])
def get_all_schools_list():
    schools = session.query(School_table).all()
    schools_list = [
        {'id': school.id, 'name': school.name, 'rank': school.rank, 'fees': school.fees} for school in schools]
    return jsonify({'data': schools_list})


# Get a specific school
@app.route('/get_particular_school', methods=['GET'])
def get_particular_school():
    data = []
    result = request.args.get('id')
    schools = session.query(School_table).filter(School_table.id == result).all()
    if schools:
        schools_list = [
            {'id': school.id, 'name': school.name, 'rank': school.rank, 'fees': school.fees} for school in schools]
        return jsonify({'data': schools_list})
    else:
        return jsonify({'message': 'School not found'}), 404


# Insert a new school
@app.route('/add_school', methods=['POST'])
def add_school():
    new_school_data = request.get_json()
    new_school = School_table(
        id=new_school_data['id'],
        name=new_school_data['name'],
        rank=new_school_data['rank'],
        fees=new_school_data['fees']

    )
    session.add(new_school)
    session.commit()
    return jsonify({'message': 'New School added successfully'})


# Update an existing school
@app.route('/update_school', methods=['PATCH'])
def update_school():
    user_data = request.get_json()
    session.query(School_table).filter(School_table.id == user_data.get('id')).update(user_data)

    session.commit()
    return jsonify({'message': 'School details updated successfully'})


# Delete a school
@app.route('/delete_school', methods=['DELETE'])
def delete_school():
    data = request.get_json()
    school = session.query(School_table).filter(School_table.id == data.get('id')).delete()
    session.commit()
    return jsonify({'message': 'School deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
