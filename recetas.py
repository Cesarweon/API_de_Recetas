from flask import Flask, request, jsonify
import json

app = Flask(__name__)

recetas = {
    'Puré de papas': {
        'nombre': 'Puré de papas',
        'descripcion': 'Sencilla y relativamente económica de hacer. Suficiente para 5 personas.',
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
        'descripcion': 'Masa para una pizza pequeña (para 1 o 2 personas).',
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
        'imagen_url': 'https://www.solopostres.com/wp-content/uploads/2017/08/Como-Hacer-Masa-de-Pizza-Basica-01.jpg',
        'reseñas': []
    },
    'Albondigas boloñesa': {
        'nombre': 'Albondigas boloñesa',
        'descripcion': 'Por si solo quieres comer carne. Suficiente para 3 personas.',
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
    },
    'Helltaker Pancakes': {
    'nombre': 'Helltaker Pancakes',
    'descripcion': 'Pancakes vistos en Helltaker.',
    'categoria': 'Desayuno',
    'ingredientes': [
        '1 Huevo',
        '1 taza de leche',
        '1 taza de harina'
    ],
    'pasos': [
        'Mezcla todos los ingredientes en un recipiente y revuelvelo como si tu vida dependiera de ello.',
        'En un sarten caliente aplica un poco de aceite suficiente un solo pancake (repitelo cada vez que hagas otro).',
        'Coloca un poco de la mezcla en el sarten cocinalo por 1 minuto dale la vuelta y cocinalo por otros 40 segundos (repitelo por cada pancake).',
        'Rellenalo de lo que quieras (Nutella, mermelada de fresa, platano, etc).'
    ],
    'imagen_url': '',
    'reseñas': []
    },
    'Awaria Pudding Pies': {
    'nombre': 'Awaria Pudding Pies',
    'descripcion': 'Deliciosos pastelillos rellenos de pudin.',
    'categoria': 'Postre',
    'ingredientes': [
        'Masa del pastelillo:',
        '250 gramos de harina',
        '60 gramos de azucar glass',
        '125 gramos de mantequilla',
        '3 yemas de huevo',
        '',
        'Pudin:',
        '2 yemas de huevo',
        '200 mililitros de leche',
        '25 gramos de mantequilla',
        '15 gramos de azúcar vainillada o azucar de vainilla',
        '1 cucharada de harina',
        '1 cucharada de fécula de papa'
    ],
    'pasos': [
        'Masa del pastelillo:',
        'Combina todos los ingredientes en un recipiente y haz la masa a mano.',
        'Divide la masa en dos y ambas partes guardalas en el refrigerador en lo que haces el pudin.',
        '',
        'Pudin:',
        'En otro recipiente mezcla ⅓ de la leche con la harina, la fécula y las yemas de huevo (para evitar que la harina forme grumos pasala por un colador para hacerla más fina).',
        'Cocina los remanentes ⅔ de leche con la azucar vainillada.',
        'Cuando la azúcar se integre mientras sigues revolviendo, agrega la mezcla de harina anteriormente hecha, después agrega la mantequilla. Esta mezcla estara lista cuando la mantequilla se derrita y integre. Dejala enfriar por ahora.',
        'Saca la masa del refrigerador y estirala una mitad la usaremos para la base del pastelillo y la otra para cerrarlos por arriba.',
        'Con un molde o un vaso vacío corta porciones del mismo tamaño y colocalas presionando en un molde de cupcakes.',
        'Rellena los moldes con masa con cucharadas completas de pudin después cierralo con más masa, pon tu dedo pulgar en los bordes del molde para eliminar excesos de masa.',
        'Junta todos los pastelillos que hayas hecho y hornealos a 180 grados C° por 25 minutos.',
        'Los pastelillos estaran listos cuando se vean un poco más oscuros. Espera a que se enfrien un poco antes de desmoldarlos.'
    ],
    'imagen_url': '',
    'reseñas': []
    }
}

@app.route('/', methods=['GET'])
def bienvenida():
    mensaje = """
    <html>
        <head>
            <title>Bienvenido a la API de recetas</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                }
                h1 {
                    color: #333;
                }
                p {
                    color: #666;
                    font-size: 18px;
                }
                img {
                    max-width: 100%;
                    height: auto;
                }
            </style>
        </head>
        <body>
            <h1>Bienvenido a la API de recetas</h1>
            <p>Descubre deliciosas recetas y comparte tus opiniones.</p>
            <img src="https://us.123rf.com/450wm/yupiramos/yupiramos2006/yupiramos200607954/148663350-abra-el-dise%C3%B1o-del-icono-del-estilo-de-la-l%C3%ADnea-del-libro-de-recetas-tema-de-la-comida-y-de-la.jpg" alt="Imagen de bienvenida">
        </body>
    </html>
    """
    return mensaje

@app.route('/api/recetas/<nombre_receta>', methods=['GET'])
def obtener_receta(nombre_receta):
    nombre_receta = nombre_receta.replace('-', ' ')
    receta = recetas.get(nombre_receta)
    if receta:
        return app.response_class(
            response=json.dumps(receta, indent=4, ensure_ascii=False),
            mimetype='application/json'
        )
    else:
        return jsonify({'mensaje': 'Receta no encontrada'}), 404

@app.route('/api/recetas/<nombre_receta>/reseñas', methods=['POST'])
def agregar_reseña(nombre_receta):
    nombre_receta = nombre_receta.replace('-', ' ')
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
    return app.response_class(
        response=json.dumps(recetas, indent=4, ensure_ascii=False),
        mimetype='application/json'
    )

@app.route('/api/recetas/categoria/<categoria>', methods=['GET'])
def obtener_recetas_por_categoria(categoria):
    recetas_por_categoria = {nombre: detalles for nombre, detalles in recetas.items() if detalles.get('categoria') == categoria}
    if not recetas_por_categoria:
        return jsonify({'mensaje': 'No hay recetas en esta categoria'}), 404
    return app.response_class(
        response=json.dumps(recetas_por_categoria, indent=4, ensure_ascii=False),
        mimetype='application/json'
    )

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
