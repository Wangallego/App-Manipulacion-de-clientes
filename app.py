from flask import Flask, render_template,request,redirect, url_for,session
from model import get_all_users, insert_user,update_user,user,delete_user,get_db_connection
from flask import jsonify
from flask_httpauth import HTTPBasicAuth

# Initialize the application

app = Flask(__name__)
auth = HTTPBasicAuth()
from werkzeug.exceptions import NotFound

@app.route('/api/login')
@auth.login_required
def get_response():
	return jsonify('You are authorized to see this message')

@auth.verify_password
def authenticate(username, password):
    if username and password:
        if username == 'roy' and password == 'roy':
            return True
        else:
            return False
    return False
    
#Obtener el listado de clientes

@app.route("/api/clientes", methods=["GET", "POST"])

def api_clientes():
    if request.method == "GET":
        clientes = get_all_users()
        return jsonify([cliente.__dict__ for cliente in clientes]), 200, {
            "Content-Type": "application/json"
        }
    if request.method == "POST":
        try:
            
            nombre = request.json["nombre"]
            direccion = request.json["direccion"]
            ciudad = request.json["ciudad"]
            pais = request.json["pais"]
            telefono = request.json["telefono"]
            email = request.json["email"]
            insert_user(nombre, direccion, ciudad, pais, telefono, email)

            return jsonify({"message": "Cliente creado exitosamente"}), 201,  {
               "Content-type":"application/json" 
            }
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Método no permitido"}), 405

@app.route("/api/clientes/<int:id>", methods=["GET", "PUT","DELETE"])
@auth.login_required
def datos_clientes(id):
    cliente = user(id)
    if request.method == "GET":
        if cliente:
            return jsonify(cliente), 200
        else:
            return jsonify({"error": "Cliente no encontrado"}), 404

    elif request.method == "PUT":
        try:
            nombre = request.json["nombre"]
            direccion = request.json["direccion"]
            ciudad = request.json["ciudad"]
            pais = request.json["pais"]
            telefono = request.json["telefono"]
            email = request.json["email"]

            # Se pasa el parámetro 'id' a la función update_user
            update_user(id, nombre, direccion, ciudad, pais, telefono, email)

            return jsonify({"message": "Cliente modificado exitosamente"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    elif request.method == "DELETE":
        try:
            # Se pasa el parámetro 'id' a la función update_user
            delete_user(id)

            return jsonify({"message": "Cliente eliminado exitosamente"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Método no permitido"}), 405

@app.route("/api/clientes/login", methods=["GET", "POST"])
def registroUsuario():
    if request.method == "POST":
        pass


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404



@app.route('/', methods = ['POST','GET'])
def show_user_list():
    clientes = get_all_users()
    return render_template('user_list.html', clientes=clientes)


@app.route('/add_user', methods=['POST','GET'])
def add_user():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        direccion = request.form.get('direccion')
        ciudad = request.form.get('ciudad')
        pais = request.form.get('pais')
        telefono = request.form.get('telefono')
        email = request.form.get('email')

        insert_user(nombre, direccion, ciudad, pais,  telefono, email)
        clientes = get_all_users()

        # Redirect to the main page after adding the user
        return redirect(url_for('show_user_list', clientes = clientes))

    return render_template('add_user.html')


@app.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    if request.method == 'POST':
        # Handle the delete request
        if 'delete' in request.form:
            delete_user(user_id)
            return redirect(url_for('show_user_list'))
        
        # Handle the update request
        nombre = request.form.get('nombre')
        direccion = request.form.get('direccion')
        ciudad = request.form.get('ciudad')
        pais = request.form.get('pais')
        telefono = request.form.get('telefono')
        email = request.form.get('email')

        update_user(user_id, nombre, direccion, ciudad, pais, telefono, email)
        return redirect(url_for('show_user_list'))

    user_id, nombre, direccion, ciudad, pais, telefono = user(user_id)
    return render_template('edit_user.html', user_id=user_id, nombre=nombre, direccion=direccion, ciudad=ciudad, pais=pais, telefono=telefono)



if __name__ == '__main__':
    app.run(debug=True, port=5000)
