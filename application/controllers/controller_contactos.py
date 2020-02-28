from application import app
from flask import Flask, jsonify#importamos los modulos necesarios
from flask import render_template, request, redirect, url_for, flash, session
from application.models.model_contactos import Contactos
from application.config.mongodb import ConexionMongo
from application.config.routes import urls

model = Contactos()

mdb = ConexionMongo().connect_mongo()
# mdb = con_mongo.connect_mongo() 


#route index
@app.route(urls['index'], methods = ['GET'])
def index():
    session['user'] = True
    if session['user']:
        collection = mdb["amigos"]
        data = { "contactos" : model.get_contactos(), "amigos": collection.find() } 
        return render_template('index.html', data = data)
    else:
        return redirect(url_for('login'))



@app.route(urls['add.user'] , methods = ['POST']) #indicamos que la ruta va recibir parametros por post
def add():
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            telefono = request.form['telefono']
            email = request.form['email']
            """ print (nombre)
            print (telefono)
            print (email) """
            model.add_contacto(nombre, telefono, email)
            flash('Contacto guardado!')
            return redirect(url_for('index'))#redireciona al mismo index
        except:
            flash('¡Ah ocurrido un error!')
            return redirect(url_for('index'))#redireciona al mismo index
        

@app.route(urls['delete.user'] , methods = ['GET'])
def delete(id):
    res = model.delete_contactos(id)
    if res == 1:
        flash('Contacto Eliminado...')
    else:
        flash('Ah ocurrido un error...')
    return redirect(url_for('index'))

# actualizacion de contactos en espera de peticiones post y get para renderizar la vista con sus datos
@app.route(urls['update.user'] , methods = ['POST', 'GET'])
def update(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        email = request.form['email']
        res = model.update_contacto(id, nombre, telefono, email)
        if res == 1:
            flash('Contacto Actualizado...')
            return redirect(url_for('index'))
        else:
            flash('Error al actualizar...')
            return redirect(url_for('index'))
    elif request.method == 'GET':
        contacto = model.get_by_id(id)
        print(contacto)
        return render_template('edit.html', contacto = contacto[0])

    