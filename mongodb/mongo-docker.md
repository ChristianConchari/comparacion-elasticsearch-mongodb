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

![Untitled](MongoDB%20con%20Docker%20af44d099f7344594b8d68d66e01e201a/Untitled.png)

Creamos una nueva base de datos y una nueva colección

![Untitled](MongoDB%20con%20Docker%20af44d099f7344594b8d68d66e01e201a/Untitled%201.png)

Cargamos los datos a partir de un documento JSON

![Untitled](MongoDB%20con%20Docker%20af44d099f7344594b8d68d66e01e201a/Untitled%202.png)

La base de datos se presentará de manera visual de la siguiente manera

![Untitled](MongoDB%20con%20Docker%20af44d099f7344594b8d68d66e01e201a/Untitled%203.png)

![Untitled](MongoDB%20con%20Docker%20af44d099f7344594b8d68d66e01e201a/Untitled%204.png)

### Consultas a la base de datos

Ingresando la siguiente consulta

```json
{agencia: "Santa Cruz", $and:[{fecha: {$gte: "2005-01-01"}}, {fecha: {$lte: "2005-12-31"}}]}
```

![Untitled](MongoDB%20con%20Docker%20af44d099f7344594b8d68d66e01e201a/Untitled%205.png)

![Untitled](MongoDB%20con%20Docker%20af44d099f7344594b8d68d66e01e201a/Untitled%206.png)

![Untitled](MongoDB%20con%20Docker%20af44d099f7344594b8d68d66e01e201a/Untitled%207.png)

### Actualización de datos

![Untitled](MongoDB%20con%20Docker%20af44d099f7344594b8d68d66e01e201a/Untitled%208.png)

### Eliminación de datos

![Untitled](MongoDB%20con%20Docker%20af44d099f7344594b8d68d66e01e201a/Untitled%209.png)