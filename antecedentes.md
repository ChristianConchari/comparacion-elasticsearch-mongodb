# Antecedentes y opciones preliminares

La aparición de las bases de datos no relacionales se ha dado para solventar los puntos débiles de los esquemas rígidos de las bases de datos relacionales, donde resalta la necesidad de anticipadamente diseñar la base de datos, anterior a la carga de los mismos, lo cual lleva a la necesidad de usar valores nulos en casos de valores faltantes. Este esquema rígido puede resultar contraproducente en casos donde el manejo de los requerimientos está en evolución constante [1]. 

[DB-Engines](https://db-engines.com/en/) es una iniciativa para recopilar y presentar información sobre los sistemas de gestión de bases de datos (SGBD). El DB-Engines Ranking es una lista de SGBD clasificados por su popularidad actual; la lista se actualiza mensualmente. Las propiedades más importantes de numerosos sistemas se muestran en la visión general de los sistemas de gestión de bases de datos. Puede examinar las propiedades de cada sistema y compararlos entre sí.

La siguiente tabla muestras las primeras 10 posiciones del [DB-Engines ranking](https://db-engines.com/en/ranking), extraídas el 4 de octubre del 2022.

| Ranking | Base de datos | Modelo de base de datos |
| --- | --- | --- |
| 1. | Oracle | Relational, Multi-model |
| 2 | MySQL | Relational, Multi-model |
| 3 | Microsoft SQL Server | Relational, Multi-model |
| 4 | PostgreSQL | Relational, Multi-model |
| 5 | MongoDB | Document, Multi-model |
| 6 | Redis | Key-value, Multi-model |
| 7 | Elasticsearch | Search engine, Multi-model |
| 8 | IBM Db2 | Relational, Multi-model |
| 9 | Microsoft Access | Relational |
| 10 | SQLite | Relational |

En la siguiente gráfica se presenta la tendencia de popularidad de diferentes bases de datos a la fecha.

![**Figura 1.** [Ranking de DB-Engines](https://db-engines.com/en/ranking_trend) - Tendencia de popularidad](https://github.com/ChristianConchari/comparacion-elasticsearch-mongodb/blob/master/imagenes-de-soporte/tendencias-bases-de-datos.png)


**Figura 1.** Ranking de DB-Engines - Tendencia de popularidad

Como se puede ver en la figura 1, MongoDB ha mantenido una tendencia superior a otras bases de datos no relacionales a lo largo de los últimos años. Por otro lado, Elasticsearch y Redis han mantenido un crecimiento conjunto similar.


# Requerimientos

Se deben cumplir los siguientes requerimientos:

- La base de datos a seleccionarse debe ser no relacional.
- La base de datos debe ser de uso libre. Además, debe poder implementarse con un servicio **“on-premise”** (de manera local).
- Debe existir soporte a la carga masiva de datos.
- Debe existir un tiempo considerablemente mínimo de espera al hacer peticiones de información a la base de datos.
- Debe considerarse el costo total de almacenamiento (espacio).
- Se puede considerar el soporte para aprendizaje automático.
- Como la información a almacenarse se debe considerar un extracto de cuenta bancario.
- Se debe considerar el uso de contenedores Docker para una implementacion PoC.


## Ejemplo: Datos de un extracto bancario

- Fecha
- Oficina
- Descripción
- Saldo total
- Monto
- Nota


# Matriz de comparación

Tomando en cuenta la información presentada anteriormente, y el contexto para el cual se debe orientar el presente proyecto, se seleccionan **MongoDB**, **Elasticsearch** y **Cassandra** como opciones preliminares para evaluar.

|  | MongoDB Community server | Elasticsearch | Cassandra |
| --- | --- | --- | --- |
| Open source | Si | Si | Si |
| Licencia de software | Server Side Public License (SSPL) | Elastic License 2.0 | Apache License 2.0 |
| Desarrollado por  | MongoDB Inc. | Elastic NV | Apache Foundation |
| On-premise | Si | Si | Si |
| Tipo de base de datos | Basada en documentos | Basada en motor de búsqueda | Basada en llave-valor |
| Formato de base de datos | Binary JSON (BSON) documents | JSON documents | Tabular Ancho-columna |
| Soporte de lenguaje de programación | C, C++, C#, Go, Java, Node.js, PHP, Python, Ruby, Rust, Scala, Swift | C#, Java, Node.js, Go, PHP, Perl, Python, Ruby | C++, C#, Java, Python, Node.js, Ruby, Go, Scala |
| Stack | MEAN stack | ELK stack | No se encontraron datos |
| Lenguaje de consulta | MQL (utiliza JavaScript) | Query DSL & KQL | CQL (similar a SQL) |
| Arquitectura | Maestro-Esclavo | Punto a punto | Punto a punto |
| Escalamiento vertical | Si | Si | Si |
| Escalamiento horizontal | Si (Sharding) | Si | Si |
| Contenedor Docker | Si | Si | Si |
| Soporte para aprendizaje automático | Si (mindsDB) | Si (Elastic ML) | Si (sin documentación oficial) |
| Velocidad de escritura | media | baja | alta |
| Velocidad de lectura | alta | alta | baja |
| Tamaño máximo de documento | 16 MB | 100 MB | 100 MB (ideal < 10 MB) |

# Matriz de decisión

Considerando una escala del 1 al 5 para la conveniencia de cada opción de base de datos según el punto en cuestión. También, considerando una escala del 1 al 5 para la importancia de cada punto.

**Tabla 2.** Matriz de decisión

| | MongoDB Community server | Elasticsearch	| Cassandra |
| --- | --- | --- | --- |
| Documentación/Comunidad	| 4	| 4	| 3 |
| Popularidad general	| 5	| 4	| 3 |
| Soporte de lenguaje de programación	| 5	| 5	| 4 |
| Stack	| 4	| 4	| 2 |
| Flexibilidad del lenguaje de consulta	| 4	| 5	| 4 |
| Curva de aprendizaje	| 4	| 3	| 3 |
| Escalamiento horizontal	| 5	| 5	| 3 |
| Soporte para aprendizaje automático	| 5	| 5	| 2 |
| Velocidad de escritura	| 3	| 2	| 4 |
| Velocidad de lectura	| 5	| 5	| 3 |
| Capacidad como base de datos primaria	| 4	| 3	| 4 |
| Tamaño máximo de documento	| 4	| 5	| 4 |

**Tabla 3.** Matriz de decisión ponderada

|  | MongoDB Community server | Elasticsearch | Cassandra | Peso |
| --- | --- | --- | --- | --- |
| Documentación/Comunidad | 12 | 12 | 9 | 3 |
| Popularidad | 10 | 8 | 6 | 2 |
| Soporte de lenguaje de programación | 20 | 20 | 16 | 4 |
| Stack | 16 | 16 | 8 | 4 |
| Flexibilidad del lenguaje de consulta | 12 | 15 | 12 | 3 |
| Curva de aprendizaje | 12 | 9 | 9 | 3 |
| Escalamiento horizontal | 15 | 15 | 9 | 3 |
| Soporte para aprendizaje automático | 20 | 20 | 8 | 4 |
| Velocidad de escritura | 15 | 10 | 20 | 5 |
| Velocidad de lectura | 25 | 25 | 15 | 5 |
| Capacidad como base de datos primaria | 16 | 12 | 16 | 4 |
| Tamaño máximo de documento | 12 | 15 | 12 | 3 |
| Puntaje final | 185 | 177 | 140 |  |

[matriz de desición - base de datos](https://docs.google.com/spreadsheets/d/1_f16qowUedWq8QG1XRIr_E1he0ZQiDf2LdPb43epQ7A/edit?usp=drivesdk)

Según los resultados de la Tabla 3, se seleccionan **MongoDB** y **Elasticsearch** para llevar a cabo una comparación de rendimiento.

# Referencias

- [1] C. Gyorödi, R. Gyorödi, and R. Sotoc, “A comparative study of relational and non-relational database models in a web- based application,” Int. J. Adv. Comput. Sci. Appl., vol. 6, no. 11, 2015, doi: 10.14569/ijacsa.2015.061111.
- [2] R. Čerešňák and M. Kvet, “Comparison of query performance in relational a non-relation databases,” Transportation Research Procedia, vol. 40, pp. 170–177, Jan. 2019, doi: 10.1016/j.trpro.2019.07.027.
- [3] Reback, G. (2021) Open source comparison: Elasticsearch vs. Mongodb, Logz.io. Available at: https://logz.io/blog/elasticsearch-vs-mongodb/ 
- [4] Shirolkar, A. (2022) Apache Cassandra Data Partitioning, Instaclustr. Available at: https://www.instaclustr.com/blog/cassandra-data-partitioning/
