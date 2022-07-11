from main import app, db
from flask import render_template, request, redirect
from models.models import *


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
            db.session.add(users)
            db.session.commit()
            return redirect('/about')
        except:
            return 'Помилка! Дані не оновились!'
    else:
        return render_template('update.html', update_data=users)

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
# All data about car
@app.route('/all-car', methods=['GET', 'POST'])
def all_auto():
    all_data = Cars.query.order_by(Cars.user_id).all()
    return render_template('car.html', all_data=all_data)
# Add data about  car
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
# Delete car by id
@app.route('/delete-car/<int:user_id>/del', methods=['GET', 'POST'])
def delete_car_by_id(user_id):
    delete_data_car = Cars.query.get(user_id)
    try:
        db.session.delete(delete_data_car)
        db.session.commit()
        return redirect('/all-car')
    except:
        return "Помилка!"


@app.route('/find', methods=['GET'])
def find_user_by_nickname():
    return render_template('find.html')


@app.route('/search', methods=['GET'])
def search_user_by_nickname():
    try:
        search_user = Users.query.filter(Users.nickname == request.args.get('nickname')).first()
        return render_template('finded.html', word_which_find=search_user)
    except:
        return 'Not found'


# authorization password and email
@app.route('/check', methods=['GET'])
def check_email():
    return render_template('authorization.html')

@app.route('/email', methods=['GET'])
def check_email_and_password():
    try:
        search_data = Users.query.filter(Users.email == request.args.get('email')).first()
        return render_template('/cheking.html', search_data=search_data)
    except:
        return 'No'

