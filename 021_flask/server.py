from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<user_name>&<user_surname>/')
def user(user_name, user_surname):
    return f'Hello {user_name} {user_surname}'


@app.route('/admin')
def admin():
    return redirect(url_for('user', user_name='Roman', user_surname='Smith'))


if __name__ == "__main__":
    app.run(debug=True)
