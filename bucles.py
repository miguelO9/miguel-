vuelos = {
    "aeroline": "avianca",
    "vuelo": "AV3102",
    "origen": "ctg",
    "destino": "mde",
    "tipo_maletas": ["cabina", "mano", "bodega"]
}

print("\detalle del vuelo:")
for key, value in vuelos.items():
    print(f"{key}: {value}")
    
print("\ntipo de equipaje")
for tipo in vuelos["tipo_maletas"]:
    print(f"{tipo}")

