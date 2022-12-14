from pymongo import MongoClient
import json
import time
import argparse
from datetime import timedelta
import os

parser = argparse.ArgumentParser(description='Generate random JSON file data')
parser.add_argument('-n', '--n_docs', type=int, default=1, help='Enter the number of json documentos to be inserted in the elastic DB')
args = parser.parse_args()

def declare_indexes(coll):
    coll.create_index('fecha')
    coll.create_index('descripcion')
    coll.create_index([('nota', 'text')])

    return print(f"índices creados en {coll}")

client = MongoClient('localhost', 27017)

db = client[f"test_mongo"]
db.create_collection(f"extracto_cuenta_{args.n_docs}m_3idx")
collection = db[f"extracto_cuenta_{args.n_docs}m_3idx"]

start_time = time.time()
for i, json_file in enumerate(sorted(os.listdir("../json-generated-data"))):
    with open(os.path.join("../json-generated-data", json_file)) as file:
        file_dict = json.load(file)

    print(f'Cargando el documento {i+1}/{args.n_docs}')

    try:
        collection.insert_many(file_dict)
    except:
        print(json_file)
        pass

    if i+1 == args.n_docs:
        break

declare_indexes(collection)

end_time = time.time()
# Mostramos los resultados en consola
print(f'Tiempo de carga de {args.n_docs}M de documentos: {str(timedelta(seconds = (end_time - start_time)))}')
print("")