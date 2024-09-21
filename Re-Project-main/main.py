from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///HOME.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  

db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    re_password = db.Column(db.String, nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home')
def Home():
    return render_template('index.html')

@app.route('/registr')
def Registr():
    return render_template('registr.html')

@app.route('/sumbit', methods=["POST"])
def Sumbit():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    re_password = request.form['re-password']

    new_data = Data(name=name, email=email, password=password, re_password=re_password)
    db.session.add(new_data)
    db.session.commit()
    return render_template('registr.html')

@app.route('/login', methods=['GET', 'POST'])
def Login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        
        user = Data.query.filter_by(email=email, password=password).first()

        if user:
            
            return redirect(url_for('Home'))
        else:
            
            flash('Email or password is incorrect', 'error')
            return redirect(url_for('Login'))
    return render_template('login.html')

@app.route('/about')
def About():
    return render_template('about.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
    app.run(debug=True)
