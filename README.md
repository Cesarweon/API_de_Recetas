# API_de_Recetas
# Documentación de la API de Recetas

## Descripción

Esta API permite gestionar recetas de cocina, proporcionando información detallada sobre ingredientes, pasos de preparación, imágenes y reseñas. Se pueden obtener recetas específicas, listar todas las recetas disponibles, buscar por categoría y agregar nuevas recetas o reseñas.

## Endpoints

### 1️⃣ Bienvenida
**Endpoint:** `/`  
**Método:** `GET`  
**Descripción:** Muestra una página de bienvenida con información sobre la API.

#### Ejemplo de solicitud:
```bash
curl -X GET https://api-de-recetas-b2269421c5fe.herokuapp.com/
```

---

### 2️⃣ Obtener todas las recetas
**Endpoint:** `/api/recetas`  
**Método:** `GET`  
**Descripción:** Devuelve una lista con todas las recetas disponibles en la base de datos.

#### Ejemplo de solicitud:
```bash
curl -X GET https://api-de-recetas-b2269421c5fe.herokuapp.com/api/recetas
```

---

### 3️⃣ Obtener una receta por su nombre
**Endpoint:** `/api/recetas/<nombre_receta>`  
**Método:** `GET`  
**Descripción:** Devuelve la información de una receta específica si existe en la base de datos.

#### Ejemplo de solicitud:
```bash
curl -X GET https://api-de-recetas-b2269421c5fe.herokuapp.com/api/recetas/Puré%20de%20papas
```

---

### 4️⃣ Obtener recetas por categoría
**Endpoint:** `/api/recetas/categoria/<categoria>`  
**Método:** `GET`  
**Descripción:** Devuelve todas las recetas que pertenecen a la categoría especificada.

#### Ejemplo de solicitud:
```bash
curl -X GET https://api-de-recetas-b2269421c5fe.herokuapp.com/api/recetas/categoria/Guarnición
```

---

### 5️⃣ Agregar una nueva receta
**Endpoint:** `/api/recetas`  
**Método:** `POST`  
**Descripción:** Agrega una nueva receta a la base de datos.

#### Ejemplo de solicitud:
```bash
curl -X POST https://api-de-recetas-b2269421c5fe.herokuapp.com/api/recetas \
     -H "Content-Type: application/json" \
     -d '{
           "nombre": "Tacos al Pastor",
           "descripcion": "Receta de tacos al pastor deliciosa.",
           "categoria": "Plato Fuerte",
           "ingredientes": ["Carne de cerdo", "Piña", "Tortillas", "Cilantro", "Cebolla"],
           "pasos": ["Cocinar la carne", "Preparar las tortillas", "Servir con cilantro y cebolla"],
           "imagen_url": "https://ejemplo.com/tacos.jpg",
           "reseñas": []
         }'
```

---

### 6️⃣ Agregar una reseña a una receta
**Endpoint:** `/api/recetas/<nombre_receta>/reseñas`  
**Método:** `POST`  
**Descripción:** Permite agregar una reseña a una receta existente.

#### Ejemplo de solicitud:
```bash
curl -X POST https://api-de-recetas-b2269421c5fe.herokuapp.com/api/recetas/Puré%20de%20papas/reseñas \
     -H "Content-Type: application/json" \
     -d '{
           "usuario": "Juan Pérez",
           "comentario": "Delicioso y fácil de hacer!",
           "puntuación": 5
         }'
```

#### Ejemplo de respuesta:
```json
{
    "mensaje": "Reseña agregada correctamente"
}
```

Si la receta no existe:
```json
{
    "mensaje": "Receta no encontrada"
}
```

---






