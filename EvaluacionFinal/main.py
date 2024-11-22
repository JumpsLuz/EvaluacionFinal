from flask import Flask, render_template, request

app = Flask(__name__)

# Datos de usuarios
users = {
    "juan": "admin",
    "pepe": "user"
}


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None

    if request.method == "POST":
        nombre = request.form.get("nombre")
        edad = int(request.form.get("edad"))
        cantidad = int(request.form.get("cantidad"))

        precio_unitario = 9000
        total_sin_descuento = precio_unitario * cantidad

        descuento = 0
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        total_con_descuento = total_sin_descuento * (1 - descuento)

        total_descuento = total_sin_descuento * descuento

        # Crear mensaje del resultado
        resultado = (
            f"Nombre del cliente : {nombre}<br><br>"
            f"Total sin descuento : ${total_sin_descuento}<br><br>"
            f"El descuento es : ${total_descuento}<br><br>"
            f"El total a pagar es de : ${total_con_descuento}"
        )

    return render_template("ejercicio1.html", resultado=resultado)



@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = None  # Variable para almacenar el mensaje dinámico

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Verificar credenciales
        if username in users and users[username] == password:
            if username == "juan":
                mensaje = f"Bienvenido Administrador {username}"
            else:
                mensaje = f"Bienvenido Usuario {username}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template("ejercicio2.html", mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)
