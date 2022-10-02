import datetime

from flask import render_template, redirect, url_for

from applications import app, db
from .forms import CreateTaskForm
from .models import Task


@app.route('/')
def main():
    tasks = db.session.query(Task).filter(
        Task.date == datetime.date.today().strftime('%Y-%m-%d'),
        Task.is_completed == False
    ).all()
    return render_template('main.html', task_length=len(tasks), tasks=tasks, form=CreateTaskForm())


@app.route('/task/', methods=['post'])
def create_task():
    form = CreateTaskForm()
    task = Task(name=form.task_name.data, date=form.date.data)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('main'))


@app.route('/task/<int:task_id>/', methods=['get'])
def complete_task(task_id):
    task = db.session.query(Task).get(task_id)
    if task:
        task.is_completed = True
        db.session.add(task)
        db.session.commit()
    return redirect(url_for('main'))