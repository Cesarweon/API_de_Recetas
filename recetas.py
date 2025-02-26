from flask import Flask, request, jsonify
import json

app = Flask(__name__)

recetas = {
    'Puré de papas': {
        'nombre': 'Puré de papas',
        'descripccion': 'Sencilla y relativamente económica de hacer. Suficiente para 5 personas.',
        'categoria': 'Guarnición',
        'ingredientes': [
            '800 gramos a 1 kilo de papas',
            'Agua',
            'Sal',
            '250 mililitros de leche',
            '25 gramos de mantequilla',
            '2 dientes de ajo',
            'Pimienta',
            'Nuez moscada (Opcional)'
        ],
        'pasos': [
            'En una olla a fuego alto, en abundante agua fría con sal, pon las papas peladas.',
            'Dejar hervir durante 30 minutos o hasta que las papas estén blandas.',
            'Poner en la misma olla donde estaban las papas a fuego bajo, leche, mantequilla, 2 dientes de ajo, un poco de pimienta y nuez moscada.',
            'Una vez caliente un poco la infusión anterior retira los dientes de ajo, agrega las papas y machacalas hasta obtener un puré untable.',
            'Sirve caliente.',
        ],
        'imagen_url': 'https://github.com/Cesarweon/Imagenes-de-pryectos/blob/main/Api-de-recetas/Pure%20de%20papa.jpg',
        'reseñas': []
    },
    'Masa para pizza': {
        'nombre': 'Masa para pizza',
        'descripccion': 'Masa para una pizza pequeña (para 1 o 2 personas).',
        'categoria': 'Panificados',
        'ingredientes': [
            '200 gramos de harina de trigo',
            '120 mililitros / media taza de agua',
            '3 gramos de levadura',
            'Una cucharadita de sal',
            'Aceite'
        ],
        'pasos': [
            'Coloca la harina en un bowl y haz un hueco en el centro.',
            'Agrega el agua, levadura, sal y un chorrito de aceite.',
            'Mezcla y amasa durante 10 minutos.',
            'Tapala y deja reposar la masa durante 90 minutos.',
            'Extiende la masa y ponle los ingredientes que desees.',
        ],
        'imagen_url': 'https://github.com/Cesarweon/Imagenes-de-pryectos/blob/main/Api-de-recetas/Masa%20para%20pizza.JPG',
        'reseñas': []
    },
    'Albondigas boloñes': {
        'nombre': 'Albondigas boloñesa',
        'descripccion': 'Por si solo quieres comer carne. Suficiente para 3 personas.',
        'categoria': 'Plato fuerte',
        'ingredientes': [
            '½ kilo de carne molida',
            '¼ de taza de pan molido',
            'Condimentos para la carne al gusto',
            '1 huevo',
            '1 barra de mantequilla',
            'Romero',
            'Ajo picado',
            'Salsa o puré de tomate (250 gramos)'
        ],
        'pasos': [
            'Condimenta la carne molida y mezclala con el pan molido y el huevo.',
            'Forma bolitas con la mezcla anterior y fríelas en un sartén con la mantequilla, ajo picado y un poco de romero.',
            'Cocina las albóndigas en el puré de tomate a fuego medio hasta que burbujee.',
            'Sírvelas solas o con pasta.',
        ],
        'imagen_url': 'https://github.com/Cesarweon/Imagenes-de-pryectos/blob/main/Api-de-recetas/Albondigas%20bolo%C3%B1esa.jpg',
        'reseñas': []
    }
}

@app.route('/', methods=['GET'])
def bienvenida():
    mensaje = """
<h1>Bienvenido a la API de recetas</h1>
<p>Descubre deliciosas recetas y comparte tus opiniones.</p>
<img src="https://github.com/Cesarweon/Imagenes-de-pryectos/blob/main/Api-de-recetas/Bienvenida.jpg" alt="Imagen de bienvenida">
"""
    return mensaje

@app.route('/api/recetas/<nombre_receta>', methods=['GET'])
def obtener_receta(nombre_receta):
    receta = recetas.get(nombre_receta)
    if receta:
        return jsonify(receta)
    else:
        return jsonify({'mensaje': 'Receta no encontrada'}), 404

@app.route('/api/recetas/<nombre_receta>/reseñas', methods=['POST'])
def agregar_reseña(nombre_receta):
    receta = recetas.get(nombre_receta)
    if not receta:
        return jsonify({'mensaje': 'Receta no encontrada'}), 404
    
    nueva_reseña = request.get_json()
    if 'reseñas' not in receta:
        receta['reseñas'] = []
    receta['reseñas'].append(nueva_reseña)
    return jsonify({'mensaje': 'Reseña agregada correctamente'}), 201

@app.route('/api/recetas', methods=['GET'])
def obtener_todas_las_recetas():
    return jsonify(recetas)

@app.route('/api/recetas/categoria/<categoria>', methods=['GET'])
def obtener_recetas_por_categoria(categoria):
    recetas_por_categoria = {nombre: detalles for nombre, detalles in recetas.items() if detalles.get('categoria') == categoria}
    if not recetas_por_categoria:
        return jsonify({'mensaje': 'No hay recetas en esta categoria'}), 404
    return jsonify(recetas_por_categoria)

@app.route('/api/recetas', methods=['POST'])
def agregar_receta():
    nueva_receta = request.get_json()
    nombre = nueva_receta.get('nombre')
    categoria = nueva_receta.get('categoria')

    if not categoria:
        return jsonify({'mensaje': 'La receta debe incluir una categoria'}), 400

    if nombre in recetas:
        return jsonify({'mensaje': 'Receta ya existente'}), 400 
    
    recetas[nombre] = nueva_receta
    return jsonify({'mensaje': 'Receta agregada correctamente'}), 201

if __name__ == '__main__':
    app.run(debug=True)
