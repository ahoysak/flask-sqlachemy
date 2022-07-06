from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysqlaqwqer2@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    first_name = db.Column(db.String(15))
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(15))
    email = db.Column(db.String(15))
    password = db.Column(db.String(15))
    nickname = db.Column(db.String(20))
    text = db.Column(db.String(20))

class Cars(db.Model):
    brand = db.Column(db.String(20))
    type = db.Column(db.String(20))
    number = db.Column(db.Integer)
    user_id = db.Column(db.Integer, primary_key=True)

@app.route('/')
def first_page():
    return render_template('firstpage.html')
# Добавлення юзерів
@app.route('/add', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nickname = request.form['nickname']
        text = request.form['text']
        id = request.form['id']
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']

        users = Users(nickname=nickname, text=text, id=id, email=email, first_name=first_name, last_name=last_name, password=password)
        try:
            db.session.add(users)
            db.session.commit()
            db.session.flush()
            return redirect('/about')
        except:
            return 'Помилка! Дані не добавились!'
    else:
        return render_template('index.html')
# вивід даних про юзерів
@app.route('/about', methods=['GET', 'POST'])
def all_data_users():
    all_data = Users.query.order_by(Users.id).all()
    return render_template('/shows.html', all_data=all_data)


# видалення користувача по ІД
@app.route('/delete/<int:id>/del', methods=['GET', 'POST'])
def delete_data_by_id(id):
    delete_data = Users.query.get_or_404(id)
    try:
        db.session.delete(delete_data)
        db.session.commit()
        return redirect('/about')
    except:
        return 'Помилка! Дані не видалились!'

# оновлення даних по ІД
@app.route('/update/<int:id>/up', methods=['GET', 'POST'])
def update_data_by_id(id):
    users = Users.query.get(id)
    if request.method == 'POST':
        users.nickname = request.form['nickname']
        users.text = request.form['text']
        users.email = request.form['email']
        users.first_name = request.form['first_name']
        users.last_name = request.form['last_name']
        users.password = request.form['password']

        try:
            db.session.commit()
            return redirect('/about')
        except:
            return 'Помилка! Дані не оновились!'
    else:
        return render_template('update.html', update_data=users)
# Оновленя машини по ІД
@app.route('/update-car/<int:user_id>/up', methods=['GET', 'POST'])
def update_cars_by_id(user_id):
    cars = Cars.query.get(user_id)
    if request.method == 'POST':
        cars.brand = request.form['brand']
        cars.type = request.form['type']
        cars.number = request.form['number']

        try:
            db.session.commit()
            return redirect('/all-car')
        except:
            return 'Помилка'
    else:
        return render_template('updatecar.html', update_data_car=cars)

# Дані про машини
@app.route('/all-car', methods=['GET', 'POST'])
def all_auto():
    all_data = Cars.query.order_by(Cars.user_id).all()
    return render_template('car.html', all_data=all_data)
# Добавлення даних про машину
@app.route('/add-car', methods=['GET', 'POST'])
def add_new_car():
    if request.method == 'POST':
        brand = request.form['brand']
        type = request.form['type']
        number = request.form['number']
        user_id = request.form['user_id']

        cars = Cars(brand=brand, type=type, number=number, user_id=user_id)
        try:
            db.session.add(cars)
            db.session.commit()
            db.session.flush()
            return redirect('/all-car')
        except:
            return 'Помилка! Дані не добавились!'
    else:
        return render_template('addcar.html')
# Видалення машини по ІД
@app.route('/delete-car/<int:user_id>/del', methods=['GET', 'POST'])
def delete_car_by_id(user_id):
    delete_data_car = Cars.query.get(user_id)
    try:
        db.session.delete(delete_data_car)
        db.session.commit()
        return redirect('/all-car')
    except:
        return "Помилка!"


# # ПОШУК ПО НІКУ
# @app.route('/search', methods=['GET'])
# def show_user():
#     file = open('users.json', 'r')
#     users = json.loads(file.read())
#     file.close()
#     nickname = request.args.get('nickname')
#     for user in users:
#         if user['nickname'] == nickname:
#             return render_template('/finded.html', searched=user)
#     return 'Error'
#
# @app.route('/find', methods=['GET'])
# def find():
#     return render_template('find.html')
# # ПЕРЕВІРКА ПО ЕМАЙЛУ І ПАРОЛЮ
# @app.route('/email', methods=['GET'])
# def show_command():
#     file = open('users.json', 'r')
#     users = json.loads(file.read())
#     file.close()
#     password = request.args.get('password')
#     email = request.args.get('email')
#     for user in users:
#         if user['password'] == password and user['email'] == email:
#             return render_template('/cheking.html')
#     return 'Error'
#
# @app.route('/check', methods=['GET'])
# def check_email():
#     return render_template('authorization.html')
#
#

# #РЕДАГУВАННЯ АВТО
# @app.route('/update-car/<int:user_id>/up', methods=['GET'])
# def remove_cars(user_id):
#     file = open('cars.json', 'r')
#     users = json.loads(file.read())
#     file.close()
#     try:
#         for user in users:
#             if user['user_id'] == str(user_id):
#                 return render_template('updatecar.html', user=user)
#     except:
#         return 'Error'
#
# @app.route('/update-car/<int:user_id>/save', methods=['POST'])
# def save_cars(user_id):
#     file = open('cars.json', 'r')
#     users = json.loads(file.read())
#     file.close()
#     for user in users:
#         if user['user_id'] == str(user_id):
#             user['brand'] = request.form.get('brand')
#             user['type'] = request.form.get('type')
#             user['number'] = request.form.get('number')
#     with open('cars.json', 'w') as file:
#         file.write(json.dumps(users))
#         return redirect('/all-car')
# # # ПОКАЗ АВТО
# @app.route('/same/<int:id>/id', methods=['POST', 'GET'])
# def check_id_auto_user(id):
#     file = open('cars.json', 'r')
#     cars = json.loads(file.read())
#     file.close()
#     user_cars = []
#     try:
#         for car in cars:
#             if str(id) == car['user_id']:
#                 user_cars.append(car)
#         return render_template('sameid.html', cars=user_cars)
#     except:
#         return 'Error'




if __name__ == '__main__':
    app.run(debug=True)






