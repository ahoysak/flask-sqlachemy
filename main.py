from flask import Flask, render_template, request, redirect

import json

app = Flask(__name__)
@app.route('/')
def first_page():
    return render_template('firstpage.html')

@app.route('/add', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('user_name')
        text_msg = request.form.get('text_msg')
        id = request.form.get('id')
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password = request.form.get('password')
        print(name)
        print(text_msg)
        print(id)
        print(email)
        print(first_name)
        print(last_name)
        print(password)
        with open('users.json') as f:
            data = json.load(f)

        if name != '' and text_msg != '' and id != '' and email != '' and first_name != '' and last_name != '' and password != '':
            name_text = {"nickname": name, "text": text_msg, "id": id, "email": email, "first_name": first_name, "last_name": last_name, "password": password}
            print(name_text)
            data.append(name_text)
            with open('users.json', 'w') as f:
                json.dump(data, f)

        with open('users.json') as f:
            data = json.load(f)

        return render_template('index.html', data=data)
    else:
        return render_template('index.html')
# всі команди
@app.route('/about', methods=['GET', 'POST'])
def go_user():
    with open('users.json') as f:
        data = json.load(f)
    return render_template('shows.html', data=data)
# видалення
@app.route('/delete/<int:id>/del', methods=['GET', 'POST'])
def delete_users(id):
    try:
        if request.method == 'GET':
            file = open('users.json', 'r')
            users = json.loads(file.read())
            file.close()
            counter = 0
            for user in users:
                if user['id'] == str(id):
                    break
                counter = counter + 1
            del users[counter]
            with open('users.json', 'w') as file:
                file.write(json.dumps(users))
        return redirect('/about')
    except:
        return ' ne tak'
# редагування
@app.route('/update/<int:id>/up', methods=['GET'])
def update_user_page(id):
    file = open('users.json', 'r')
    users = json.loads(file.read())
    file.close()
    for user in users:
        if user['id'] == str(id):
            return render_template('update.html', user=user)

@app.route('/update/<int:id>/save', methods=['POST'])
def save_user(id):
    file = open('users.json', 'r')
    users = json.loads(file.read())
    file.close()
    for user in users:
        if user['id'] == str(id):
            user['nickname'] = request.form.get('nickname')
            user['text'] = request.form.get('text')
            user['email'] = request.form.get('email')
            user['first_name'] = request.form.get('first_name')
            user['last_name'] = request.form.get('last_name')
            user['password'] = request.form.get('password')
    with open('users.json', 'w') as file:
        file.write(json.dumps(users))
    return redirect('/about')
# ПОШУК ПО НІКУ
@app.route('/search', methods=['GET'])
def show_user():
    file = open('users.json', 'r')
    users = json.loads(file.read())
    file.close()
    nickname = request.args.get('nickname')
    for user in users:
        if user['nickname'] == nickname:
            return render_template('/finded.html', searched=user)
    return 'Error'

@app.route('/find', methods=['GET'])
def find():
    return render_template('find.html')
# ПЕРЕВІРКА ПО ЕМАЙЛУ І ПАРОЛЮ
@app.route('/email', methods=['GET'])
def show_command():
    file = open('users.json', 'r')
    users = json.loads(file.read())
    file.close()
    password = request.args.get('password')
    email = request.args.get('email')
    for user in users:
        if user['password'] == password and user['email'] == email:
            return render_template('/cheking.html')
    return 'Error'

@app.route('/check', methods=['GET'])
def check_email():
    return render_template('authorization.html')


# ВСІ МАШИНИ
@app.route('/all-car', methods=['GET'])
def all_auto():
    with open('cars.json') as f:
        data = json.load(f)
    return render_template('car.html', data=data)
# ДОДАВАННЯ АВТО
@app.route('/add-car', methods=['GET', 'POST'])
def add_new_car():
    if request.method == 'POST':
        name = request.form.get('brand')
        type_car = request.form.get('type')
        number_car = request.form.get('number')
        id_for_user = request.form.get('user_id')
        print(name)
        print(type_car)
        print(number_car)
        print(id_for_user)
        with open('cars.json') as f:
            data = json.load(f)

        if name != '' and type_car != '' and number_car != '' and id_for_user != '':
            write_data = {"brand": name, "type": type_car, "number": number_car, "user_id": id_for_user}
            print(write_data)
            data.append(write_data)
            with open('cars.json', 'w') as f:
                json.dump(data, f)

        with open('cars.json') as f:
            data = json.load(f)

        return render_template('addcar.html', data=data)
    else:
        return render_template('addcar.html')
# ВИДАЛЕННЯ АВТО
@app.route('/delete-car/<int:user_id>/del', methods=['GET', 'POST'])
def delete_car(user_id):
    try:
        if request.method == 'GET':
            file = open('cars.json', 'r')
            users = json.loads(file.read())
            file.close()
            counter = 0
            for user in users:
                if user['user_id'] == str(user_id):
                    break
                counter = counter + 1
            del users[counter]
            with open('cars.json', 'w') as file:
                file.write(json.dumps(users))

        return redirect('/')
    except:
        return ' ne tak'
#РЕДАГУВАННЯ АВТО
@app.route('/update-car/<int:user_id>/up', methods=['GET'])
def remove_cars(user_id):
    file = open('cars.json', 'r')
    users = json.loads(file.read())
    file.close()
    try:
        for user in users:
            if user['user_id'] == str(user_id):
                return render_template('updatecar.html', user=user)
    except:
        return 'Error'

@app.route('/update-car/<int:user_id>/save', methods=['POST'])
def save_cars(user_id):
    file = open('cars.json', 'r')
    users = json.loads(file.read())
    file.close()
    for user in users:
        if user['user_id'] == str(user_id):
            user['brand'] = request.form.get('brand')
            user['type'] = request.form.get('type')
            user['number'] = request.form.get('number')
    with open('cars.json', 'w') as file:
        file.write(json.dumps(users))
        return redirect('/all-car')
# # ПОКАЗ АВТО
@app.route('/same/<int:id>/id', methods=['POST', 'GET'])
def check_id_auto_user(id):
    file = open('cars.json', 'r')
    cars = json.loads(file.read())
    file.close()
    user_cars = []
    try:
        for car in cars:
            if str(id) == car['user_id']:
                user_cars.append(car)
        return render_template('sameid.html', cars=user_cars)
    except:
        return 'Error'




if __name__ == '__main__':
    app.run(debug=True)






