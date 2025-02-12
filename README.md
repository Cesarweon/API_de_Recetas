# API_de_Recetas
## Descripción

Esta API permite gestionar recetas de cocina, proporcionando información detallada sobre ingredientes y pasos de preparación. Se pueden obtener recetas específicas, listar todas las recetas disponibles y agregar nuevas recetas.
https://api-de-recetas-b2269421c5fe.herokuapp.com/api/recetas
## Endpoints

### 1. Obtener una receta por su nombre

**Endpoint:** `/api/recetas/<nombre_receta>`\
**Método:** `GET`\
**Descripción:** Devuelve la información de una receta específica si existe en la base de datos.

#### Ejemplo de solicitud:

```bash
GET /api/recetas/pure_de_papas
```

#### Ejemplo de respuesta:

```json
{
    "nombre": "Puré de Papas",
    "descripcion": "Sencilla y relativamente económica de hacer. Alcanza para 5 personas o más.",
    "categoria": "Guarnición",
    "ingredientes": [
        "800 gramos a 1 kilo de papas",
        "Agua",
        "Sal",
        "250 mililitros de leche",
        "25 gramos de mantequilla",
        "2 dientes de ajo",
        "Pimienta",
        "Nuez moscada (opcional)"
    ],
    "pasos": [
        "Poner a fuego alto, en abundante agua fría, de 800 gramos a 1 kilo de papas peladas junto a dos cucharadas bien cargadas de sal de grano.",
        "Una vez que rompa hervor, baja a fuego bajo y cocina durante 30 minutos o hasta que las papas estén bien tiernas. Colar y retirar el exceso de líquido.",
        "Mezcla en una olla a fuego bajo 250 ml de leche, 25 gr de mantequilla, 2 dientes de ajo, pimienta (al gusto) y nuez moscada (al gusto).",
        "Calienta hasta que la mantequilla se derrita y deja infusionar a fuego bajo por 5 minutos o hasta que esté bien caliente. La leche no debe hervir.",
        "En la misma olla o en un bowl aparte, mezcla las papas ya coladas y la infusión.",
        "Machaca bien las papas hasta tener un puré untable. De ser necesario, volver al fuego unos minutos para calentarse de nuevo."
    ]
}
```

### 2. Obtener todas las recetas

**Endpoint:** `/api/recetas`\
**Método:** `GET`\
**Descripción:** Devuelve una lista con todas las recetas disponibles en la base de datos.

#### Ejemplo de solicitud:

```bash
GET /api/recetas
```

#### Ejemplo de respuesta:

```json
{
    "pure_de_papas": { ... },
    "masa_para_pizza": { ... },
    "albondigas_bolonesa": { ... }
}
```

### 3. Obtener recetas por categoría

**Endpoint:** `/api/recetas/categoria/<categoria>`\
**Método:** `GET`\
**Descripción:** Devuelve todas las recetas que pertenecen a la categoría especificada.

#### Ejemplo de solicitud:

```bash
GET /api/recetas/categoria/Guarnición
```

#### Ejemplo de respuesta:

```json
{
    "pure_de_papas": {
        "nombre": "Puré de Papas",
        "descripcion": "Sencilla y relativamente económica de hacer.",
        "categoria": "Guarnición",
        "ingredientes": [...],
        "pasos": [...]
    }
}
```

### 4. Agregar una nueva receta

**Endpoint:** `/api/recetas`\
**Método:** `POST`\
**Descripción:** Agrega una nueva receta a la base de datos.

#### Ejemplo de solicitud:

```bash
POST /api/recetas
Content-Type: application/json

{
    "nombre": "Tacos de Bistec",
    "descripcion": "Receta sencilla y deliciosa para preparar tacos de bistec.",
    "categoria": "Plato Fuerte",
    "ingredientes": ["Tortillas de maíz", "Bistec de res", "Cebolla", "Cilantro", "Limón", "Salsa"],
    "pasos": [
        "Cortar el bistec en trozos pequeños y sazonar con sal y pimienta.",
        "Calentar un sartén a fuego alto y cocinar el bistec hasta que esté bien dorado.",
        "Calentar las tortillas y servir el bistec con cebolla, cilantro y salsa al gusto."
    ]
}
```

#### Ejemplo de respuesta:

```json
{
    "mensaje": "Receta agregada correctamente"
}
```

Si la receta ya existe:

```json
{
    "mensaje": "Receta ya existente"
}
```

---



