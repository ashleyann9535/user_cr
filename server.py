from flask import Flask, render_template, request, redirect

from user import User
app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)