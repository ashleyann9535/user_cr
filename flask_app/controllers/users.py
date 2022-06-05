from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

#Create
@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/create_user', methods=["POST"])
def create_user():
#Make dictionary from form data using same variable names from form
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
#pass form data into save class method in users
    User.save(data)
    return redirect('/users')


#Read
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def read_all():
# call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template('read_all.html', all_users = users)

@app.route('/view/<int:id>')
def view(id):
    user = User.view_one(id)
    return render_template('view.html', id = id, user = user)


#Update
@app.route('/edit/<int:id>')
def edit(id):
    user = User.view_one(id)
    return render_template('edit.html', id = id, user = user)

@app.route('/update/<int:id>', methods = ['POST'])
def update(id):
    data = {
        'id': id,
        'first_name': request.form['fname'],
        'last_name': request.form['lname'],
        'email': request.form['email']
    }
    User.update(data)

    num = data['id']
    return redirect(f'/view/{num}')


#Delete
@app.route('/delete/<int:id>')
def delete_user(id):
    User.delete_user(id)
    return redirect('/users')
