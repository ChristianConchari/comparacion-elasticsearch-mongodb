from random import randrange, randint, choice, uniform,randint
from datetime import timedelta, datetime
from lorem_text import lorem
from json import dumps
import argparse
import os
import time

parser = argparse.ArgumentParser(description='Generate random JSON file data')
parser.add_argument('-n', '--n_docs', type=int, default=1, help='Enter the number of json documentos to be generated')
args = parser.parse_args()


descripciones = [
    'Transferencia interbancaria SIMPLE',
    'DEB.CTA.P/C.INTERNET',
    'Debito Cta por ACH',
    'Retiro en efectivo',
    'AB.CTA.P/MOVIL',
    'Pago recibo de agua',
    'Debito Cta por compra',
    'Debito Cta por pago de Seguro',
    'Retención IVA',
    'Cargo por cobro de servicio',
    'Cobro seguro',
    'Intereses',
    'Ingreso en efectivo',
    'Reintegro cajero automático',
    'Pago de cheque compensado',
    'Pago recibo de luz',
    'Deposito a cuenta',
    'Comisión de mantenimiento',
    'Pago en interés',
    'Consignación en efectivo',
    'Pago recibo de gas',
    'Compra en comercio',
    'Apertura de cuenta corriente',
    'Pago de nómina',
    'Capitalización de intereses premio',
    'Aporte inversor',
    'Pago de servicio telefónico',
    'Transferencia de fondos de ahorros',
    'Pago en línea - Servicio de internet',
    'Apertura de caja de ahorros'
]

agencias = ['La Paz',
            'Oruro', 
            'Cochabamba', 
            'Chuquisaca', 
            'Pando', 
            'Beni', 
            'Santa Cruz', 
            'Tarija'
]

d1 = datetime.strptime('1/1/1950 12:59 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2022 01:00 AM', '%m/%d/%Y %I:%M %p')

storage_dir = "json-generated-data"

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def create_dir(folder):
    if not os.path.isdir(folder):
        print("Creating :" + folder)
        os.mkdir(folder)

def generate_data():
    
    c = 0
    create_dir(storage_dir)
    
    start = time.time()
    for j in range (args.n_docs):
        output_file = os.path.join(storage_dir, f"random-generated-data-{j+1}.json")
        list_dict = []
        for _ in range(1000000):
            fecha = random_date(d1, d2)
            agencia = choice(agencias)
            monto = round(uniform(10.0, 400000.0), 2)
            descripcion = choice(descripciones)
            saldo = round(uniform(0.0, 10000000.0), 2)
            nota = lorem.words(randint(1,13))

            data_dict = {
                'fecha': fecha,
                'agencia': agencia,
                'monto': monto,
                'descripcion': descripcion,
                'saldo': saldo,
                'nota': nota
            }

            list_dict.append(data_dict)
            c += 1
            
        json_object = dumps(list_dict, indent=4, default=str)
            
        with open(output_file, "w") as outfile:
            outfile.write(json_object)

        print(f"{(c)//1000000}/{args.n_docs}")

    end = time.time()

    print(f"{c} documents generated in {str(timedelta(seconds = (end - start)))}")

        
            

if __name__=="__main__":
    try:
        generate_data()

    except:
        print("Error during data generation")
    