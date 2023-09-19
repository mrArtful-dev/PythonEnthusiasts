from flask import Flask, redirect, url_for, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import hashlib

app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(hours=2)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:G173!ksdNNa295Asdg13@localhost/pyenthusiasts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class Users(db.Model):
    user_id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    password = db.Column('password', db.String(100))
    email = db.Column('email', db.String(100))

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        name = request.form['user-name']
        password = hashlib.md5(request.form['user-password'].encode()).hexdigest()
        user_in_db = Users.query.filter_by(name=name).first()
        if user_in_db:
            if password == user_in_db.password:
                session['user_name'] = name
                session['email'] = user_in_db.email
                return redirect(url_for('user', user_name=name, user_email=user_in_db.email))
            else:
                return redirect(url_for('login'))
        else:
            new_user = Users(name, password, '')
            db.session.add(new_user)
            db.session.commit()
            session['user_name'] = name
            session['email'] = ''
            return redirect(url_for('user', user_name=name))
    else:
        if 'user_name' in session:
            return redirect(url_for('user', user_name=session['user_name'], user_email=session['email']))
        else:
            return render_template('login.html')


@app.route('/user')
def user():
    if 'user_name' in session:
        name = session['user_name']
        return render_template('user.html', user_name=name)
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user_name', None)
    return redirect(url_for('login'))


@app.route('/admin')
def admin():
    return redirect(url_for('user', user_name='Roman', user_surname='Smith'))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
