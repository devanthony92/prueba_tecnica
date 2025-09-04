📘 Documentación de Prueba Tecnica: API de Productos
🧾 Descripción General
Esta API permite gestionar productos en una base de datos MySQL. Está construida con FastAPI, SQLAlchemy y Pydantic, y permite realizar operaciones CRUD (crear, leer, actualizar, eliminar) sobre productos.

🏗️ Tecnologías Utilizadas

- **FastAPI** – Framework moderno y rápido para construir APIs.
- **SQLAlchemy** – ORM para interactuar con bases de datos relacionales.
- **Pydantic** – Validación de datos basada en modelos.
- **MySQL** – Base de datos relacional.
- **Uvicorn** – Servidor ASGI para ejecutar la aplicación.
- **dotenv** – Manejo de variables de entorno.

📁 Estructura del Proyecto
prueba_tecnica/
├── app/
│ ├── **init**.py
│ ├── main.py
│ ├── models.py
│ ├── schemas.py
│ ├── crud.py
│ ├── database.py
├── .env
├── requirements.txt

⚙️ Configuración Inicial

1. Clona el repositorio:
   https://github.com/devanthony92/prueba_tecnica.git

2. Crea un entorno virtual:
   python -m venv venv
   source venv/bin/activate para mac o linux # o venv\Scripts\activate en Windows

3. Instala las dependencias:
   pip install -r requirements.txt
4. Configura el archivo .env:
   DB_USER=tu_usuario
   DB_PASS=tu_contraseña
   DB_HOST=localhost
   DB_NAME=nombre_base_datos

🚀 Ejecución del Proyecto
Desde el directorio raíz:
uvicorn app.main:app --reload

La documentación interactiva estará disponible en:

- Swagger UI: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

📦 Endpoints Disponibles

**GET/productos/**

- Descripción: Lista todos los productos.
- Parámetros opcionales: skip, limit
- Respuesta: Lista de productos.

  **GET/productos/{id}**

- Descripción: Obtiene un producto por su ID.
- Respuesta: Producto individual o error 404.

  **POST /productos/**

- Descripción: Crea un nuevo producto.
- Body (JSON):
  {
  "nombre": "string (requerido, max 100)",
  "descripcion": "string (opcional, max 255)",
  "precio": "number (requerido, positivo)",
  "categoria": "string (opcional, max 50)"
  }

  **PATCH /productos/{id}**

- Descripción: Actualiza parcialmente un producto.
- Body (JSON): Solo los campos que deseas modificar.

  **DELETE /productos/{id}**

- Descripción: Elimina un producto por ID.
- Respuesta: Mensaje de confirmación o error 404.

🧪 Pruebas con Postman
Puedes importar una colección con todos los endpoints y probarlos localmente. Incluye ejemplos de cuerpo, headers y respuestas esperadas.

📌 Notas Adicionales

- La validación de datos se realiza automáticamente con Pydantic.
- La base de datos se inicializa en el evento startup.
- Los errores se manejan con HTTPException para respuestas claras.

👩‍💻 Autor
Anthony Martinez – Desarrollador backend en formación, apasionado por FastAPI, Python y la mejora continua.
