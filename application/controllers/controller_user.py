from application import app
from flask import render_template, request, redirect , url_for, flash
from application.config.routes import urls



@app.route(urls['login'], methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':

        
        email = request.form['email']
        password = request.form['pass']
        mensaje = "el correo {0} y contraseña {1} son estos".format(email, password)
        flash(mensaje, 'danger')
        return redirect(url_for('login', info = 'info'))
