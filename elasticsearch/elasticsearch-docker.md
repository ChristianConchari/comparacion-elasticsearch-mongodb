# Elasticsearch

# ELK con Docker y certificados de seguridad

### Iniciando Elasticsearch con Docker

Descargamos la imagen de Elasticsearch en su última versión a la fecha

```bash
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.4.3
```

Creamos una red de Docker para conectar Kibana y Elasticsearch posteriormente

```bash
docker network create elastic
```

<aside>
💡 En caso de existir errores de memoria en la máquina host, se debe ejecutar el siguiente comando:
sudo sysctl -**w** vm.max_map_count=262144

</aside>

Corremos la imagen de elastic search

```bash
docker run --name es01 --net elastic -p 9200:9200 -p 9300:9300 -it docker.elastic.co/elasticsearch/elasticsearch:8.4.3
```

En la terminal debería mostrarse un mensaje con información similar a la siguiente

```
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-> Elasticsearch security features have been automatically configured!
-> Authentication is enabled and cluster connections are encrypted.

->  Password for the elastic user (reset with `bin/elasticsearch-reset-password -u elastic`):
  H4OSFhfIWDGiSNJzhoLK

->  HTTP CA certificate SHA-256 fingerprint:
  5e80c98430adab43b3506eee2267cfede0049f1c7880d59e3f0933a6902459dd

->  Configure Kibana to use this cluster:
* Run Kibana and click the configuration link in the terminal when Kibana starts.
* Copy the following enrollment token and paste it into Kibana in your browser (valid for the next 30 minutes):
  eyJ2ZXIiOiI4LjQuMyIsImFkciI6WyIxNzIuMjEuMC4yOjkyMDAiXSwiZmdyIjoiNWU4MGM5ODQzMGFkYWI0M2IzNTA2ZWVlMjI2N2NmZWRlMDA0OWYxYzc4ODBkNTllM2YwOTMzYTY5MDI0NTlkZCIsImtleSI6IldIdndJSVFCSE4yeDZDWVR3dXZ4OjNmbUU1RDEtVEh1QlRHU0VNby1wU1EifQ==

-> Configure other nodes to join this cluster:
* Copy the following enrollment token and start new Elasticsearch nodes with `bin/elasticsearch --enrollment-token <token>` (valid for the next 30 minutes):
  eyJ2ZXIiOiI4LjQuMyIsImFkciI6WyIxNzIuMjEuMC4yOjkyMDAiXSwiZmdyIjoiNWU4MGM5ODQzMGFkYWI0M2IzNTA2ZWVlMjI2N2NmZWRlMDA0OWYxYzc4ODBkNTllM2YwOTMzYTY5MDI0NTlkZCIsImtleSI6IlZudndJSVFCSE4yeDZDWVR3dXZ4Okp3b0pCUlBQVEs2V2FGWThJT0NCbWcifQ==

  If you're running in Docker, copy the enrollment token and run:
  `docker run -e "ENROLLMENT_TOKEN=<token>" docker.elastic.co/elasticsearch/elasticsearch:8.4.3`
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

Copiamos los certificados de seguridad del contenedor a la máquina local

```bash
docker cp es01:/usr/share/elasticsearch/config/certs/http_ca.crt .
```

Para verificar la correcta iniciación de la base de datos

```bash
curl --cacert http_ca.crt -u elastic https://localhost:9200
```

Dado que los tokens de enrrolamiento se reinician cada 30 minutos, eventualmente puede ser necesario establecer unos nuevos, ya sea para registrar un nodo nuevo o para conectar con kibana

```bash
docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana
```

### Iniciando Kibana con Docker

Ejecutamos el siguiente comando para correr la imagen de Kibana de Docker con la configuración normal.

```bash
sudo docker run --name kibana-02 --net elastic -p 5601:5601 docker.elastic.co/kibana/kibana:8.4.3
```

Al finalizar la preparación del contenedor se mostrará en terminal un mensaje similar al siguiente:

![Untitled](https://github.com/ChristianConchari/comparacion-elasticsearch-mongodb/blob/master/imagenes-de-soporte/consola-kibana.png)

Este mensaje nos indica el puerto donde tendremos corriendo el servicio de Kibana.  La interfaz gráfica corriendo en el navegador nos pedirá 

![Untitled](https://github.com/ChristianConchari/comparacion-elasticsearch-mongodb/blob/master/imagenes-de-soporte/kibana-cred.png)

![Untitled](https://github.com/ChristianConchari/comparacion-elasticsearch-mongodb/blob/master/imagenes-de-soporte/kibana-login.png)

# ELK con Docker sin certificados de seguridad

Utilizaremos el siguiente archivo de configuración `docker-compose.yml` para iniciar el contendor

```docker
version: '3'
services:
  elasticsearch:
    container_name: es01
    image: docker.elastic.co/elasticsearch/elasticsearch:8.4.3
    environment: ['ES_JAVA_OPTS=-Xms2g -Xmx2g','bootstrap.memory_lock=true','discovery.type=single-node','xpack.security.enabled=false', 'xpack.security.enrollment.enabled=false']
    ports:
      - 9200:9200
    networks:
      - elastic
    ulimits:
      memlock:
        soft: -1
        hard: -1
      nofile:
        soft: 65536
        hard: 65536

  kibana:
    image: docker.elastic.co/kibana/kibana:8.4.3
    container_name: kib01
    environment:
      XPACK_APM_SERVICEMAPENABLED: "true"
      XPACK_ENCRYPTEDSAVEDOBJECTS_ENCRYPTIONKEY: aaaaaaaa-c4d3-4a0a-8290-2abcb83ab3aa

    ports:
      - 5601:5601
    networks:
      - elastic

networks:
  elastic:
```

Ejecutamos el siguiente comando

```docker
docker compose up
```

![Untitled](https://github.com/ChristianConchari/comparacion-elasticsearch-mongodb/blob/master/imagenes-de-soporte/elastic-docker-compose.png)

En terminal deberían mostrarse mensajes similares

# Manejo de datos con Kibana

Ya corriendo Elasticsearch mediante docker, podemos utilizar Kibana como interfaz gráfica para interactuar con la base de datos.

### Carga de datos

Se cargará un archivo JSON, que contiene 50,000  objetos JSON separados por salto de línea.

![Untitled](https://github.com/ChristianConchari/comparacion-elasticsearch-mongodb/blob/master/imagenes-de-soporte/elastic-json.png)

![Untitled](https://github.com/ChristianConchari/comparacion-elasticsearch-mongodb/blob/master/imagenes-de-soporte/elastic-files.png)

### Consultas a la base de datos

Ejecutamos en consola

```jsx
GET /extracto_cuenta/_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "agencia": "La Paz" } },
        {"range" : {
          "fecha": { "gte" : "2000-01-01", "lte" : "2020-12-31" }}
        }
      ]
    }
  }
}
```

Obtenemos

```json
{
  "took": 892,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 1624,
      "relation": "eq"
    },
    "max_score": 3.1915112,
    "hits": [
      {
        "_index": "extracto_cuenta",
        "_id": "ruh5C4QBpbZ7TzuGbeWA",
        "_score": 3.1915112,
        "_source": {
          "descripcion": "Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem.",
          "fecha": "2011-11-18",
          "monto": 2424.99,
          "notes": "Sed ante. Vivamus tortor. Duis mattis egestas metus.",
          "@timestamp": "2011-11-18T00:00:00.000-04:00",
          "hora": "2:55:57",
          "saldo": 4708121.76,
          "agencia": "La Paz"
        }
      },
      {
        "_index": "extracto_cuenta",
        "_id": "ueh5C4QBpbZ7TzuGbeWA",
        "_score": 3.1915112,
        "_source": {
          "descripcion": null,
          "fecha": "2009-08-26",
          "monto": 500.9,
          "notes": "Aliquam quis turpis eget elit sodales scelerisque. Mauris sit amet eros. Suspendisse accumsan tortor quis turpis.",
          "@timestamp": "2009-08-26T00:00:00.000-04:00",
          "hora": "16:03:10",
          "saldo": 2980720.29,
          "agencia": "La Paz"
        }
      },
      {
        "_index": "extracto_cuenta",
        "_id": "xOh5C4QBpbZ7TzuGbeWA",
        "_score": 3.1915112,
        "_source": {
          "descripcion": "In est risus, auctor sed, tristique in, tempus sit amet, sem.",
          "fecha": "2015-03-31",
          "monto": 3670.93,
          "notes": null,
          "@timestamp": "2015-03-31T00:00:00.000-04:00",
          "hora": "19:55:27",
          "saldo": 1445541.16,
          "agencia": "La Paz"
        }
      },
      {
        "_index": "extracto_cuenta",
        "_id": "4Oh5C4QBpbZ7TzuGbeWA",
        "_score": 3.1915112,
        "_source": {
          "descripcion": "Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem.",
          "fecha": "2012-07-14",
          "monto": 2177,
          "notes": "Maecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra diam vitae quam. Suspendisse potenti.",
          "@timestamp": "2012-07-14T00:00:00.000-04:00",
          "hora": "12:12:56",
          "saldo": 4430576.59,
          "agencia": "La Paz"
        }
      },
      {
        "_index": "extracto_cuenta",
        "_id": "8-h5C4QBpbZ7TzuGbeWB",
        "_score": 3.1915112,
        "_source": {
          "descripcion": null,
          "fecha": "2006-04-13",
          "monto": 1414.92,
          "notes": null,
          "@timestamp": "2006-04-13T00:00:00.000-04:00",
          "hora": "18:32:29",
          "saldo": 411060.42,
          "agencia": "La Paz"
        }
      },
      {
        "_index": "extracto_cuenta",
        "_id": "-eh5C4QBpbZ7TzuGbeWB",
        "_score": 3.1915112,
        "_source": {
          "descripcion": "Vivamus in felis eu sapien cursus vestibulum.",
          "fecha": "2020-09-25",
          "monto": 232.46,
          "notes": "Aenean lectus. Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum.",
          "@timestamp": "2020-09-25T00:00:00.000-04:00",
          "hora": "19:13:55",
          "saldo": 4525304,
          "agencia": "La Paz"
        }
      },
      {
        "_index": "extracto_cuenta",
        "_id": "aeh5C4QBpbZ7TzuGbeaB",
        "_score": 3.1915112,
        "_source": {
          "descripcion": "Curabitur convallis.",
          "fecha": "2013-06-19",
          "monto": 2982.96,
          "notes": "Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem.",
          "@timestamp": "2013-06-19T00:00:00.000-04:00",
          "hora": "10:23:42",
          "saldo": 7307727,
          "agencia": "La Paz"
        }
      },
      {
        "_index": "extracto_cuenta",
        "_id": "cuh5C4QBpbZ7TzuGbeaB",
        "_score": 3.1915112,
        "_source": {
          "descripcion": "Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci.",
          "fecha": "2004-09-03",
          "monto": 3256.61,
          "notes": "Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.",
          "@timestamp": "2004-09-03T00:00:00.000-04:00",
          "hora": "13:46:20",
          "saldo": 8877107,
          "agencia": "La Paz"
        }
      },
      {
        "_index": "extracto_cuenta",
        "_id": "oOh5C4QBpbZ7TzuGbeaB",
        "_score": 3.1915112,
        "_source": {
          "descripcion": "In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem.",
          "fecha": "2015-01-07",
          "monto": 2635.95,
          "notes": "Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
          "@timestamp": "2015-01-07T00:00:00.000-04:00",
          "hora": "3:10:18",
          "saldo": 9880479,
          "agencia": "La Paz"
        }
      },
      {
        "_index": "extracto_cuenta",
        "_id": "rOh5C4QBpbZ7TzuGbeaB",
        "_score": 3.1915112,
        "_source": {
          "descripcion": "Nulla ac enim.",
          "fecha": "2001-10-11",
          "monto": 1283.36,
          "notes": "Maecenas ut massa quis augue luctus tincidunt. Nulla mollis molestie lorem. Quisque ut erat.",
          "@timestamp": "2001-10-11T00:00:00.000-04:00",
          "hora": "2:50:03",
          "saldo": 5206383.25,
          "agencia": "La Paz"
        }
      }
    ]
  }
}
```

![Untitled](https://github.com/ChristianConchari/comparacion-elasticsearch-mongodb/blob/master/imagenes-de-soporte/elastic-busqueda.png)

### Insertamos objetos en la base de datos

Ejecutamos en consola

```json
POST extracto_cuenta/_doc
{
  "fecha": "2003-02-13",
  "monto": 13.4,
  "notes": "DEB.CTA.P/C.INTERNET",
  "@timestamp": "2009-08-26T00:00:00.000-04:00",
  "hora": "19:49:10",
  "saldo": 130.50,
  "agencia": "La Paz"
}
```

Obtenemos

```json
{
  "_index": "extracto_cuenta",
  "_id": "dOlxDIQBpbZ7TzuGW5pl",
  "_version": 1,
  "result": "created",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 50000,
  "_primary_term": 1
}
```

### Actualizamos objetos en la base de datos

Ejecutamos en consola

```json
POST extracto_cuenta/_update/dOlxDIQBpbZ7TzuGW5pl
{
  "script" : {
    "source": "ctx._source.monto = 350.20"
  }
}
```

Obtenemos

```json
{
  "_index": "extracto_cuenta",
  "_id": "dOlxDIQBpbZ7TzuGW5pl",
  "_version": 2,
  "result": "updated",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 50001,
  "_primary_term": 1
}
```

### Actualizamos a través de búsqueda

Ejecutamos en consola

```json
POST extracto_cuenta/_update_by_query
{
  
  "script": {
    "source": "ctx._source['monto'] = 4000; ctx._source['notes'] = 'Monto mayora 3900 actualizado a 4000'; ",
    "lang": "painless"
  },
  
  "query": {
      "range" : {
          "monto": { "gte" : 3900}}
      }
}
```

### Eliminamos objetos de la base de datos

Ejecutamos en consola

```json
DELETE /extracto_cuenta/_doc/8uh5C4QBpbZ7TzuGaNuC
{
  "_index": "extracto_cuenta",
  "_id": "8uh5C4QBpbZ7TzuGaNuC",
  "_version": 2,
  "result": "deleted",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 51234,
  "_primary_term": 1
}
```

Obtenemos

```json
{
  "took": 870,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": 3.190581,
    "hits": [
      {
        "_index": "extracto_cuenta",
        "_id": "Kel5C4QBpbZ7TzuGiDcg",
        "_score": 3.190581,
        "_source": {
          "descripcion": "Integer non velit.",
          "fecha": "2001-01-14",
          "monto": 3872.92,
          "notes": null,
          "@timestamp": "2001-01-14T00:00:00.000-04:00",
          "hora": "5:24:46",
          "saldo": 4877837.16,
          "agencia": "La Paz"
        }
      }
    ]
  }
}
```

### Eliminamos objetos por búsqueda

Ejecutamos en consola

```json
POST extracto_cuenta/_delete_by_query
{
  "query": {
    "bool": {
      "must": [
        { "match": { "agencia": "Oruro" } },
        {"range" : {
          "monto": { "gte" : "3872", "lte" : "3875" }}
        }
      ]
    }
  }
}
```

Obtenemos

```json
{
  "took": 1053,
  "timed_out": false,
  "total": 4,
  "deleted": 4,
  "batches": 1,
  "version_conflicts": 0,
  "noops": 0,
  "retries": {
    "bulk": 0,
    "search": 0
  },
  "throttled_millis": 0,
  "requests_per_second": -1,
  "throttled_until_millis": 0,
  "failures": []
}
```
