# MongoDB con Docker

# Instalación

Para instalar MongoDB a partir de una imagen de Docker, recurrimos a la imagen oficial.

[mongo - Official Image | Docker Hub](https://hub.docker.com/_/mongo)

```bash
sudo docker pull mongo
```

Iniciamos el contenedor tomando en cuenta persistencia de datos

```bash
sudo docker run --name mongo-python -p 27017:27017 -d -v ~/Documents/mongo-python:/data/db mongo
```

Para iniciar la consola interactiva corremos el siguiente comando

```bash
mongo localhost:27017
```

# Manejo de datos con MongoDB Compass

### Carga de datos

Se establece conexión con la base de datos

![Untitled](https://github.com/ChristianConchari/comparacion-elasticsearch-mongodb/blob/master/imagenes-de-soporte/conexion-mongo.png)

Creamos una nueva base de datos y una nueva colección

![Untitled](https://github.com/ChristianConchari/comparacion-elasticsearch-mongodb/blob/master/imagenes-de-soporte/nueva-coleccion-mongo.png)

Cargamos los datos a partir de un documento JSON

![Untitled](https://github.com/ChristianConchari/comparacion-elasticsearch-mongodb/blob/master/imagenes-de-soporte/cargar-json-mongo.png)

La base de datos se presentará de manera visual de la siguiente manera

![Untitled](https://github.com/ChristianConchari/comparacion-elasticsearch-mongodb/blob/master/imagenes-de-soporte/coleccion-mongo.png)

![Untitled](https://github.com/ChristianConchari/comparacion-elasticsearch-mongodb/blob/master/imagenes-de-soporte/tabla-mongo.png)

### Consultas a la base de datos

Ingresando la siguiente consulta

```json
{agencia: "Santa Cruz", $and:[{fecha: {$gte: "2005-01-01"}}, {fecha: {$lte: "2005-12-31"}}]}
```

![Untitled](https://github.com/ChristianConchari/comparacion-elasticsearch-mongodb/blob/master/imagenes-de-soporte/busqueda-mongo.png)

![Untitled](https://github.com/ChristianConchari/comparacion-elasticsearch-mongodb/blob/master/imagenes-de-soporte/stats-mongo.png)

![Untitled](https://github.com/ChristianConchari/comparacion-elasticsearch-mongodb/blob/master/imagenes-de-soporte/time-mongo.png)

### Actualización de datos

![Untitled](https://github.com/ChristianConchari/comparacion-elasticsearch-mongodb/blob/master/imagenes-de-soporte/edit-mongo.png)

### Eliminación de datos

![Untitled](https://github.com/ChristianConchari/comparacion-elasticsearch-mongodb/blob/master/imagenes-de-soporte/delete-mongo.png)
