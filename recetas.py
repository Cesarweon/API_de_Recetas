from flask import Flask, request, jsonify
import json

app = Flask(__name__)

recetas = {
    'Puré de papas': {
        'nombre': 'Puré de Papas',
        'descripcion': 'Sencilla y relativamente económica de hacer. Alcanza para 5 personas o más.',
        'categoria': 'Guarnición',
        'ingredientes': [
            '800 gramos a 1 kilo de papas',
            'Agua',
            'Sal',
            '250 mililitros de leche',
            '25 gramos de mantequilla',
            '2 dientes de ajo',
            'Pimienta',
            'Nuez moscada (opcional)'
        ],
        'pasos': [
            'En una olla poner a fuego alto, en abundante agua fría sal y las papas peladas.',
            'Dejar hervir durante 30 minutos o hasta que las papas estén blandas.',
            'Colar las papas y retirar el exceso de agua.',
            'Pon en la misma olla donde estaban las papas a fuego bajo, mezcla la leche, mantequilla, los dientes de ajo, un poco de pimienta y nuez moscada.',
            'Una vez caliente un poco la infusion anterior retira los dientes de ajo, agrega las papas y machacalas hasta obtener un puré untable.',
            'Sirve caliente.',

        ]
    },
    'Masa para pizza': {
        'nombre': 'Masa para Pizza',
        'descripcion': 'Masa para una pizza pequeña (1 a 2 personas).',
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
        'Tapala y dejala reposar durante 90 hora.',
        'Extiende la masa y ponle los ingredientes que prefieras.',
        ]
    },
    'Albondigas boloñesa': {
        'nombre': 'Albóndigas Boloñesa',
        'descripcion': 'Por si quieres solo comer carne. Suficiente para ±3 personas.',
        'categoria': 'Plato Fuerte',
        'ingredientes': [
            '½ kilo de carne molida',
            '¼ de taza de pan molido',
            'Condimentos a gusto (sal, pimienta, ajo en polvo, orégano y albahaca en polvo)',
            '1 huevo',
            '1 barra de mantequilla',
            'Ramas de romero',
            'Ajo picado',
            'Salsa o puré de tomate casero o comprado (250 gr)'
        ],
        'pasos': [
        'Condimenta la carne molida y mezclala con el pan molido y el huevo.',
        'Forma las albóndigas y fríelas en la mantequilla con el ajo y romero.',
        'Cocina las albondigas en el puré de tomate a fuego medio hasta que burbujee.',
        'Sirvelas solas o con pasta.',
        
        ]
    }
}

@app.route('/api/recetas/<nombre_receta>', methods=['GET'])
def obtener_receta(nombre_receta):
    receta = recetas.get(nombre_receta)
    if receta:
        return app.response_class(
            response=json.dumps(receta, indent=4, sort_keys=True, ensure_ascii=False),
            mimetype='application/json'
        )
    else:
        return jsonify({'mensaje': 'Receta no encontrada'}), 404

@app.route('/api/recetas', methods=['GET'])
def obtener_todas_las_recetas():
    return app.response_class(
        response=json.dumps(recetas, indent=4, sort_keys=True, ensure_ascii=False),
        mimetype='application/json'
    )

@app.route('/api/recetas/categoria/<categoria>', methods=['GET'])
def obtener_recetas_por_categoria(categoria):
    recetas_por_categoria = {nombre: detalles for nombre, detalles in recetas.items() if detalles.get('categoria') == categoria}
    if not recetas_por_categoria:
        return app.response_class(
            response=json.dumps({'mensaje': 'No hay recetas en esta categoría'}, indent=4, sort_keys=True, ensure_ascii=False),
            mimetype='application/json'
        )
    return app.response_class(
        response=json.dumps(recetas_por_categoria, indent=4, sort_keys=True, ensure_ascii=False),
        mimetype='application/json'
    )

@app.route('/api/recetas', methods=['POST'])
def agregar_receta():
    nueva_receta = request.get_json()
    nombre = nueva_receta.get('nombre')
    if not nueva_receta.get('categoria'):
        return jsonify({'mensaje': 'La receta debe incluir una categoría'}), 400
    if nombre in recetas:
        return jsonify({'mensaje': 'Receta ya existente'}), 400

    recetas[nombre] = nueva_receta
    return jsonify({'mensaje': 'Receta agregada correctamente'}), 201

if __name__ == '__main__':
    app.run(debug=True)
