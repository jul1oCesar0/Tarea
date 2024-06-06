from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return (
        "<center>"
        "<head>"
        '<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">'
        "<title>Julio Cesar Salazar Hernandez 9 A</title>"
        "</head>"
        '<body class="bg-gray-300">'
        "<div class='container mx-auto p-4 mt-20'>"
        "<h1 class='text-2xl font-bold mb-4'>Julio Cesar Salazar Hernandez 9 A</h1>"
        '<img src="https://www.educaciontrespuntocero.com/wp-content/uploads/2020/04/mejores-bancos-de-imagenes-gratis.jpg" alt="Mi imagen" class="w-64 mb-4">'
        '<form id="myForm" action="/submit" method="post" class="mb-4">'
        '<label for="name" class="mr-2 font-bold">Escribe tu nombre:</label>'
        '<input type="text" id="name" name="name" class="border rounded px-2 py-1">'
        '<input type="submit" value="Enviar" class="bg-blue-500 text-white px-2 py-2 ml-4 rounded cursor-pointer">'
        "</form>"
        "</div>"
        "</center>"
        '<script>'
        'document.getElementById("myForm").addEventListener("submit", function(event) { '
        'event.preventDefault(); ' # Evitar que se envíe el formulario
        'var name = document.getElementById("name").value; '
        'alert("¡Hola, " + name + "!"); '
        '});'
        '</script>'
    )

if __name__ == '__main__':
    app.run(debug=True)
