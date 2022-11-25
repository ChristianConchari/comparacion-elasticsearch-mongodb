from elasticsearch import Elasticsearch
from elasticsearch import helpers
import time
import argparse
from datetime import timedelta
import os 

parser = argparse.ArgumentParser(description='Generate random JSON file data')
parser.add_argument('-n', '--n_docs', type=int, default=1, help='Enter the number of json documentos to be inserted in the elastic DB')

args = parser.parse_args()


es = Elasticsearch("http://127.0.0.1:9200")

print(f"Connected to ElasticSearch cluster `{es.info().body['cluster_name']}`")

start_time = time.time()
for i, json_file in enumerate(sorted(os.listdir("../json-generated-data-elastic"))):
    with open(os.path.join("../json-generated-data-elastic", json_file)) as file:
        file_dict = file.readlines()
    
    print(f'Cargando el documento {i+1}/{args.n_docs}')
    
    try:
        helpers.bulk(es, file_dict, index=f"extracto_cuenta_{args.n_docs}m")
    except:
        print(json_file)
        pass
    
    if i+1 == args.n_docs:
        break

end_time = time.time()
# Mostramos los resultados en consola
print(f'Tiempo de carga de {args.n_docs}M de documentos: {str(timedelta(seconds = (end_time - start_time)))}')
print("")