# Antecedentes y opciones preliminares

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

![**Figura 1.** Ranking de DB-Engines - Tendencia de popularidad **(**[https://db-engines.com/en/ranking_trend](https://db-engines.com/en/ranking_trend)**)**](Antecedentes%20y%20opciones%20preliminares%20815dd3a7c63c4586ba5b6bc706e931f5/Untitled.png)

**Figura 1.** Ranking de DB-Engines - Tendencia de popularidad **(**[https://db-engines.com/en/ranking_trend](https://db-engines.com/en/ranking_trend)**)**

Como se puede ver en la figura 1, MongoDB ha mantenido una tendencia superior a otras bases de datos no relacionales a lo largo de los últimos años. Por otro lado, Elasticsearch y Redis han mantenido un crecimiento conjunto similar.

[DB-Engines Ranking](https://db-engines.com/en/ranking_trend)

# Requerimientos

Se deben cumplir los siguientes requerimientos:

- Debe tratarse de una base de datos no relacional
- La base de datos debe ser de uso libre (o al menos tener una versión de prueba). Además, debe poder implementarse con un servicio **“on-premise”** (de manera local).
- Debe existir soporte a la carga masiva de datos.
- Debe existir un tiempo considerablemente mínimo de espera al hacer peticiones de información a la base de datos.
- Debe considerarse el costo total de almacenamiento (espacio).

# Consideraciones

- Soporte para aprendizaje automático.
- Tomar en cuenta un **extracto de cuenta complejo** como la información a tratarse.
    - Zona, ATMs, datos del usuario, fecha y hora, notas en la transacción, entre otros datos relevantes.
- Docker (Contenedores)
- **Mockaroo, [generatedata](https://generatedata.com/generator)** puede usarse para generar datos aleatorios

# Datos de un extracto bancario

- Fecha
- Hora
- Oficina
- Descripción
- Saldo total
- Monto
- Glosa o nota

# Antecedentes de las bases de datos no relacionales

La aparición de las bases de datos no relacionales se ha dado para solventar los puntos débiles de los esquemas rígidos de las bases de datos relacionales, donde resalta la necesidad de anticipadamente diseñar la base de datos, anterior a la carga de los mismos, lo cual lleva a la necesidad de usar valores nulos en casos de valores faltantes. Este esquema rígido puede resultar contraproducente en casos donde el manejo de los requerimientos está en evolución constante (Gyorödi, et al., 2015). 

Tres opciones populares fueron elegidas como opciones preliminares a evaluar, estas son:

- MongoDB
- Elasticsearch
- Cassandra

# Matriz de comparación

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
| Escalamiento horizontal | Si (Sharding) | Si (escalabilidad) | Si (escalabilidad) |
| Contenedor Docker | Si (imagen oficial) | Si (imagen oficial) | Si (imagen oficial) |
| Soporte para aprendizaje automático | Si (mindsDB) | Si (Elastic ML) | Si (sin documentación oficial) |
| Velocidad de escritura | media | media | alta |
| Velocidad de lectura | alta | muy alta | baja |
| Tamaño máximo de documento | 16 MB | 100 MB | 100 MB (ideal < 10 MB) |

# Matriz de decisión

Considerando una escala del 1 al 5 para la conveniencia de cada opción de base de datos según el punto en cuestión. También, considerando una escala del 1 al 5 para la importancia de cada punto.

[matriz de desición - base de datos](https://docs.google.com/spreadsheets/d/1_f16qowUedWq8QG1XRIr_E1he0ZQiDf2LdPb43epQ7A/edit?usp=drivesdk)

# Referencias

- Gyorödi, C., Gyorödi, R., & Sotoc, R. (2015). A comparative study of relational and non-relational database models in a web- based application. International Journal of Advanced Computer Science and Applications : IJACSA, 6(11). doi: 10.14569/ijacsa.2015.061111
- Čerešňák, R., & Kvet, M. (2019). Comparison of query performance in relational a non-relation databases. Transportation Research Procedia, 40, 170–177. doi: 10.1016/j.trpro.2019.07.027
- Reback, G. (2020, mayo 19). Open source comparison: Elasticsearch vs. MongoDB. *Logz.Io*. https://logz.io/blog/elasticsearch-vs-mongodb/
- Shirolkar, A. (2019, agosto 29). *Apache Cassandra data partitioning*. Instaclustr. https://www.instaclustr.com/blog/cassandra-data-partitioning/
