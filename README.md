#Reto CIID

Kevin Alcántara


##Preparativos

Acceder al repositorio de app-flask con:

```
cd app-flask
```

Luego, iniciar el entonro virtual con 

```
source env/binactivate
```

Y utilizar el archivo para instalar las dependencias necesarias con: 

```
pip install requirements.txt
```

##Ejecución
Ya con el entorno virtual activado, usar el comando

```
python app.py
```

Para Windows ó 

```
python3 app.py
```

Para SO basados en Unix.

##Rutas

Con las siguientes rutas, una vez corriendo el servidor de manera local, es posible probarlo con una herramienta como POSTMAN para ver su funcionamiento

### Rutas de la API Startups

#### 1. Obtener todas las startups
- **Ruta**: `/api/startups/read`
- **Método**: `GET`
- **Descripción**: Devuelve todas las startups almacenadas en la base de datos.

---

#### 2. Obtener una startup por ID
- **Ruta**: `/api/startups/read/<int:idStartup>`
- **Método**: `GET`
- **Descripción**: Devuelve una startup específica identificada por `idStartup`.

---

#### 3. Crear una nueva startup
- **Ruta**: `/api/startups/create`
- **Método**: `POST`
- **Descripción**: Crea una nueva startup. Los datos deben enviarse en el cuerpo de la solicitud como JSON.

---

#### 4. Búsqueda por nombre
- **Ruta**: `/api/startups/read/name/<string:nombre>`
- **Método**: `GET`
- **Descripción**: Busca startups cuyo nombre contenga la cadena `nombre`.

---

#### 5. Búsqueda por ubicación
- **Ruta**: `/api/startups/read/location/<string:ubicacion>`
- **Método**: `GET`
- **Descripción**: Busca startups que se encuentren en la ubicación proporcionada.

---

#### 6. Búsqueda por categoría
- **Ruta**: `/api/startups/read/category/<string:categoria>`
- **Método**: `GET`
- **Descripción**: Busca startups que pertenezcan a la categoría proporcionada.

---

#### 7. Actualizar una startup por ID
- **Ruta**: `/api/startups/update/<int:idStartup>`
- **Método**: `PUT`
- **Descripción**: Actualiza la información de una startup específica.

---

#### 8. Eliminar una startup por ID
- **Ruta**: `/api/startups/delete/<int:idStartup>`
- **Método**: `DELETE`
- **Descripción**: Elimina una startup específica.

---

### Rutas de la API Technologies

####1. Obtener todas las tecnologías
- **Ruta**: `/api/technologies/read`
- **Método**: `GET`
- **Descripción**: Devuelve todas las tecnologías almacenadas en la base de datos.

---

#### 2. Obtener una tecnología por ID
- **Ruta**: `/api/technologies/read/<int:idTechnologie>`
- **Método**: `GET`
- **Descripción**: Devuelve una tecnología específica identificada por `idTechnologie`.

---

#### 3. Crear una nueva tecnología
- **Ruta**: `/api/technologies/create`
- **Método**: `POST`
- **Descripción**: Crea una nueva tecnología. Los datos deben enviarse en el cuerpo de la solicitud como JSON.

---

#### 4. Búsqueda por nombre
- **Ruta**: `/api/technologies/read/name/<string:nombre>`
- **Método**: `GET`
- **Descripción**: Busca tecnologías cuyo nombre contenga la cadena `nombre`.

---

#### 5. Búsqueda por sector
- **Ruta**: `/api/technologies/read/sector/<string:sector>`
- **Método**: `GET`
- **Descripción**: Busca tecnologías que pertenezcan al sector proporcionado.

---

#### 6. Búsqueda por descripción
- **Ruta**: `/api/technologies/read/description/<string:descripcion>`
- **Método**: `GET`
- **Descripción**: Busca tecnologías que tengan la descripción proporcionada.

---

#### 7. Búsqueda por estado de adopción
- **Ruta**: `/api/technologies/read/adoption-state/<string:estadoAdopcion>`
- **Método**: `GET`
- **Descripción**: Busca tecnologías que tengan el estado de adopción proporcionado.

---

#### 8. Actualizar una tecnología por ID
- **Ruta**: `/api/technologies/update/<int:idTechnologie>`
- **Método**: `PUT`
- **Descripción**: Actualiza la información de una tecnología específica.

---

#### 9. Eliminar una tecnología por ID
- **Ruta**: `/api/technologies/delete/<int:idTechnologie>`
- **Método**: `DELETE`
- **Descripción**: Elimina una tecnología específica.

---



