# >python -m pip install obd

import obd

# Nawi�zanie po��czenia z adapterem OBD-II
connection = obd.OBD()  # Automatycznie wykrywa port OBD-II
#obd.OBD(port='COM3')

# Sprawdzenie, czy po��czenie zosta�o nawi�zane
if connection.is_connected():
    print("Po��czono z adapterem OBD-II")
else:
    print("Nie uda�o si� po��czy� z adapterem OBD-II")
    exit()

# Wys�anie zapytania o obroty silnika (RPM)
cmd = obd.commands.RPM  # Komenda OBD-II dla obrot�w silnika
response = connection.query(cmd)  # Wys�anie zapytania

# Sprawdzenie, czy odpowied� jest poprawna
if response.is_successful():
    print(f"Obroty silnika: {response.value} RPM")
else:
    print("Nie uda�o si� odczyta� obrot�w silnika")

# Zamkni�cie po��czenia
connection.close()