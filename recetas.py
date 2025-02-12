from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Datos de recetas con categorías
recetas = {
    'pure_de_papas': {
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
        'pasos': [...]
    },
    'masa_para_pizza': {
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
        'pasos': [...]
    },
    'albondigas_bolonesa': {
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
        'pasos': [...]
    }
}

@app.route('/api/recetas/<nombre_receta>', methods=['GET'])
def obtener_receta(nombre_receta):
    receta = recetas.get(nombre_receta)
    if receta:
        return jsonify(receta)
    else:
        return jsonify({'mensaje': 'Receta no encontrada'}), 404

@app.route('/api/recetas', methods=['GET'])
def obtener_todas_las_recetas():
    return jsonify(recetas)

@app.route('/api/recetas/categoria/<categoria>', methods=['GET'])
def obtener_recetas_por_categoria(categoria):
    recetas_por_categoria = {nombre: detalles for nombre, detalles in recetas.items() if detalles.get('categoria') == categoria}
    if not recetas_por_categoria:
        return jsonify({'mensaje': 'No hay recetas en esta categoría'}), 404
    return jsonify(recetas_por_categoria)

@app.route('/api/recetas', methods=['POST'])
def agregar_receta():
    nueva_receta = request.get_json()
    nombre = nueva_receta.get('nombre')
    categoria = nueva_receta.get('categoria')
    
    if not categoria:
        return jsonify({'mensaje': 'La receta debe incluir una categoría'}), 400
    
    if nombre in recetas:
        return jsonify({'mensaje': 'Receta ya existente'}), 400
    
    recetas[nombre] = nueva_receta
    return jsonify({'mensaje': 'Receta agregada correctamente'}), 201

if __name__ == '__main__':
    app.run(debug=True)

