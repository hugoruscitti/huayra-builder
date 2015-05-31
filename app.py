# -*- encoding: utf-8 -*-
import os
import random
import time

from flask import Flask, render_template, url_for, jsonify, send_file
from celery import Celery

TMP_DIR = "tmp"

app = Flask(__name__)
app.config['SECRET_KEY'] = '-133322-'
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

def create_build_id():
    return str(random.randint(10000, 90000))

@celery.task(bind=True)
def build_package_from_repository(self, user, repo):
    build_id = create_build_id()
    url = "http://github.com/" + user + "/" + repo
    destination_path = "tmp/" + build_id

    def update_step(step, message):
        print "MESSAGE", message
        time.sleep(4)
        meta = {'step': step, 'total': total_steps, 'status': message}
        self.update_state(state='PROGRESS', meta=meta)

    total_steps = 5
    update_step(0, "Iniciando tarea")

    update_step(1, "Clonando el repositorio")
    os.system("git clone %s %s" %(url, destination_path))

    update_step(2, "Iniciando el proyecto")
    os.system("cd %s; make iniciar" %(destination_path))

    update_step(3, "Generando el paquete")
    os.system("cd %s; make generar_paquete" %(destination_path))

    update_step(4, "Borrando directorio clonado")
    os.system("rm -r -f %s" %(destination_path))

    update_step(5, "Tarea completada")


@app.route('/clone/<user>/<repo>')
def clonar(user, repo):
    task = build_package_from_repository.apply_async(args=[user, repo])
    url = "http://localhost:5000" + url_for('buildstatus', task_id=task.id)
    return jsonify({'status_url': url})

@app.route('/buildstatus/<task_id>')
def buildstatus(task_id):
    task = build_package_from_repository.AsyncResult(task_id)

    if task.state == 'PENDING':
        response = {
            'step': 0,
            'total': 5,
            'status': 'Pendiente...'
        }


    if not task.info:
        return jsonify({"state": task.state})


    if task.state != 'FAILURE':
        response = {
            'state': task.state,
            'step': task.info.get('step', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
        }
    return jsonify(response)

@app.route('/')
def index():
    return send_file('client/dist/index.html')

@app.route('/assets/<file>')
def assets(file):
    return send_file('client/dist/assets/' + file)

if __name__ == '__main__':
    app.run(debug=True)
