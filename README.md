# Comparación de desempeño para el caso conceptual de un extracto de cuenta entre MongoDB vs Elasticsearch

En la presente investigación se ha realizado una comparación entre diferentes bases de datos no relacionales,
buscando elegir la mejor opción para el caso conceptual de un extracto de cuenta. Las bases de datos a evaluarse experimentalmente fueron elegidas mediante un proceso de comparación de características, donde MongoDB, Elasticsearch obtuvieron los mejores puntajes. La experimentación se realizó en los campos: uso de almacenamiento en memoria y rendimiento en tiempo, en operaciones de carga, búsqueda, actualización y eliminación. La experimentación recién mencionada se encuentra disponible en los cuadernos de Python de este repositorio.

<div align="center">
  <a href="https://github.com/ChristianConchari/comparacion-elasticsearch-mongodb/tree/master/elasticsearch"><b>Código - Elasticsearch</b></a> |
  <a href="https://github.com/ChristianConchari/comparacion-elasticsearch-mongodb/tree/master/mongodb"><b>Código - MongoDB</b></a> |
  <a href="https://github.com/ChristianConchari/comparacion-elasticsearch-mongodb/blob/master/antecedentes.md"><b>Antecedentes</b></a> 
  
</div>

## Generación de datos aleatorios en formato JSON

Para generar 30 documentos, donde cada uno contenga un millón de objetos JSON, debe ejecutar el siguiente script:

```
python random-json-data-generation.py -n 30
```
El parámetro ```n``` define la cantidad de documentos a generase. El script anterior, también se encargará de generar el directorio ```json-generated-data```.

Para convertir los archivos generados al formato requerido para ser cargados a Elasticsearch debe ejecutarse el siguiente script:

```
python convert-json-to-elastic-format.py
```

El script leerá los archivos en formato JSON generados anteriormente, y los adaptará para la estructura soportada por Elasticsearch en el directorio ```json-generated-data-elastic```.

En el archivo ```requirements.txt`` se encuentran las librerias de python correspondientes a Pymongo y el cliente de Python de Elasticsearch, entre otras librerías utilizadas en el proyecto. Para instalarlas, ejecutar el siguiente comando:

```
pip install -r requirements.txt
```

Se recomienda trabajar el proyecto dentro de un [ambiente virtual](https://docs.python.org/3/library/venv.html) para evitar conflictos con otras versiones de las librerias.
