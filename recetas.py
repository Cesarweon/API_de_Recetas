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
        'imagen_url': 'https://th.bing.com/th/id/OIP.8IIFf7VLJrP5HqfnYnwVAgHaE8?rs=1&pid=ImgDetMain',
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
        'imagen_url': 'data:image/jpeg;base64,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',
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
        'imagen_url': 'https://www.petitchef.es/imgupl/recipe/albondigas-a-la-bolonesa--66042p86387.jpg',
        'reseñas': []
    }
}

@app.route('/', methods=['GET'])
def bienvenida():
    mensaje = """
    <h1>Bienvenido a la API de recetas</h1>
    <p>Descubre deliciosas recetas y comparte tus opiniones.</p>
    <img src="data:image/jpeg;base64,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" alt="Imagen de bienvenida">
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
