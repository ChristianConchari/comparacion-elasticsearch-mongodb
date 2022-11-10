from random import randrange, randint, choice, uniform,randint
from datetime import timedelta, datetime
from lorem_text import lorem
from json import dumps
import argparse

parser = argparse.ArgumentParser(description='Generate random JSON file data')
parser.add_argument('-db', '--db_name', type=str, help="Enter the databse name (mongo or elastic)")
parser.add_argument('-e', '--exp', type=int, help='Enter the exponent of the number or rows to generate')
args = parser.parse_args()

data_rows = 10*(10**args.exp)

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

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def generate_data():
    fecha = random_date(d1, d2)
    agencia = choice(agencias)
    monto = round(uniform(10.0, 400000.0), 2)
    descripcion = choice(descripciones)
    saldo = round(uniform(0.0, 10000000.0), 2)
    nota = lorem.words(randint(1,13))

    return {
        'fecha': fecha,
        'agencia': agencia,
        'monto': monto,
        'descripcion': descripcion,
        'saldo': saldo,
        'nota': nota
    }


def generate_data_elastic():
    for _ in range(data_rows):
        json_object = dumps(generate_data(), indent=4, default=str)
    
        with open(f"random_generated_data_{args.db_name}.json", "a") as outfile:
            outfile.write("\n")
            outfile.write(json_object)
            

def generate_data_mongo():
    list_dict = []
    for _ in range(data_rows):
        data_dict = generate_data()
        list_dict.append(data_dict)
        
    json_object = dumps(list_dict, indent=4, default=str)
    
    with open(f"random_generated_data_{args.db_name}.json", "w") as outfile:
        outfile.write(json_object)
        
            

if __name__=="__main__":
    try:
        if args.db_name == "mongo":
            generate_data_mongo()
        elif args.db_name == "elastic":
            generate_data_elastic()
        else:
            print("Enter a valid database (elastic or mongo)")
            raise
    except:
        print("Error during data generation")
    