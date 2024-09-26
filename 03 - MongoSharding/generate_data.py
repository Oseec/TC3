from pymongo import MongoClient
from faker import Faker
import random

# Inicializar Faker
fake = Faker()

# Conectar a la base de datos MongoDB (reemplaza con tu conexión a mongos)
client = MongoClient("mongodb://localhost:27019")  # Asegúrate de usar el puerto correcto donde está mongos
db = client["db2"]  # Reemplaza con el nombre de tu base de datos

# Insertar documentos en la colección test2
for i in range(200, 2000):
    document = {
        'shardkey_custom': i,  # Usar el índice como shard key
        'ced': 239438476 + i,  # Generar cedulas o IDs aleatorios
        'nombre': fake.name(),  # Generar un nombre realista con Faker
        'direccion': fake.address(),  # Añadir dirección usando Faker
        'email': fake.email(),  # Generar un correo electrónico con Faker
        'telefono': fake.phone_number(),  # Generar un número de teléfono con Faker
        'fecha_nacimiento': fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=90),  # Fecha de nacimiento
        'empresa': fake.company(),  # Empresa para darle contexto a los datos
    }
    
    # Insertar el documento en la colección test2
    db.test2.insert_one(document)

print("Documentos insertados correctamente.")
