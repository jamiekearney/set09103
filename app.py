from flask import Flask, render_template, request, redirect,  url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/40442397/todotest/todo.db'

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)

@app.route('/',)
def index():
    incomplete = Todo.query.filter_by(complete=False).all()
    complete = Todo.query.filter_by(complete=True).all()
    return render_template('index.html', incomplete=incomplete, complete=complete)    

@app.route('/add', methods=['POST'])
def add():
    todo = Todo(text=request.form['todoitem'], complete=False)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/complete/<id>')
def complete(id):
#Query for the todo
    todo = Todo.query.filter_by(id=int(id)).first()
    #update the flag to true
    todo.complete = True
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/delete', methods=['POST','DELETE'])
def delete():
    todo = Todo(text=request.form['todoitem'], complete=True)
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for('index'))

#class Journal(db.Model):
   # id = db.Entry(db.Integer, prim

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
