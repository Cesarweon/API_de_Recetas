from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos de recetas
recetas = {
    'pure_de_papas': {
        'nombre': 'Puré de Papas',
        'descripcion': 'Sencilla y relativamente económica de hacer. Alcanza para 5 personas o más.',
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
            'Poner a fuego alto, en abundante agua fría, de 800 gramos a 1 kilo de papas peladas junto a dos cucharadas bien cargadas de sal de grano.',
            'Una vez que rompa hervor, baja a fuego bajo y cocina durante 30 minutos o hasta que las papas estén bien tiernas. Colar y retirar el exceso de líquido.',
            'Mezcla en una olla a fuego bajo 250 ml de leche, 25 gr de mantequilla, 2 dientes de ajo, pimienta (al gusto) y nuez moscada (al gusto).',
            'Calienta hasta que la mantequilla se derrita y deja infusionar a fuego bajo por 5 minutos o hasta que esté bien caliente. La leche no debe hervir.',
            'En la misma olla o en un bowl aparte, mezcla las papas ya coladas y la infusión.',
            'Machaca bien las papas hasta tener un puré untable. De ser necesario, volver al fuego unos minutos para calentarse de nuevo.'
        ]
    },
    'masa_para_pizza': {
        'nombre': 'Masa para Pizza',
        'descripcion': 'Masa para una pizza pequeña (1 a 2 personas).',
        'ingredientes': [
            '200 gramos de harina de trigo',
            '120 mililitros / media taza de agua',
            '3 gramos de levadura',
            'Una cucharadita de sal',
            'Aceite'
        ],
        'pasos': [
            'En un bowl coloca 200 gr de harina y haz un hueco en el centro.',
            'En el hueco agrega 120 ml de agua, 3 gr de levadura y disuélvelo en el agua.',
            'En los bordes de la harina esparce una cucharadita de sal y en el agua un chorrito de aceite.',
            'Mezcla todo y una vez integrado empieza a amasar durante 10 minutos.',
            'Después de los 10 minutos deja reposar la masa en un recipiente con tapa previamente engrasado durante 1 hora y media / 90 minutos (Cuanto más tiempo mejor).',
            'Saca la masa, dale forma y está lista para hacer la pizza.'
        ]
    },
    'albondigas_bolonesa': {
        'nombre': 'Albóndigas Boloñesa',
        'descripcion': 'Por si quieres solo comer carne. Suficiente para ±3 personas.',
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
            'En un bowl condimenta la carne molida con el condimento de tu gusto.',
            'Agrega el cuarto de taza de pan molido y el huevo, mezcla hasta que se integren bien.',
            'En un sartén a fuego bajo, pon a derretir un buen pedazo de mantequilla. Cuando se derrita, agrega ajo picado y romero hasta que se combinen los olores. Saca el ajo y romero.',
            'Agrega las albóndigas al sartén y báñalas con la mantequilla con ajo y romero. Cocínalas hasta que estén listas.',
            'En ese mismo sartén o en uno más hondo a fuego medio, pon el puré de tomate y las albóndigas hasta que el puré burbujee. Si tu puré es comprado, puedes condimentarlo (si no lo está).'
        ]
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
    # Supongamos que añadimos una categoría a cada receta en el diccionario
    recetas_por_categoria = {nombre: detalles for nombre, detalles in recetas.items() if detalles.get('categoria') == categoria}
    return jsonify(recetas_por_categoria)

@app.route('/api/recetas', methods=['POST'])
def agregar_receta():
    nueva_receta = request.get_json()
    nombre = nueva_receta.get('nombre')
    if nombre in recetas:
        return jsonify({'mensaje': 'Receta ya existente'}), 400

    recetas[nombre] = nueva_receta
    return jsonify({'mensaje': 'Receta agregada correctamente'}), 201

if __name__ == '__main__':
    app.run(debug=True)
