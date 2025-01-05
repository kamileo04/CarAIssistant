# >python -m pip install obd

import obd

# Nawi¹zanie po³¹czenia z adapterem OBD-II
connection = obd.OBD()  # Automatycznie wykrywa port OBD-II
#obd.OBD(port='COM3')

# Sprawdzenie, czy po³¹czenie zosta³o nawi¹zane
if connection.is_connected():
    print("Po³¹czono z adapterem OBD-II")
else:
    print("Nie uda³o siê po³¹czyæ z adapterem OBD-II")
    exit()

# Wys³anie zapytania o obroty silnika (RPM)
cmd = obd.commands.RPM  # Komenda OBD-II dla obrotów silnika
response = connection.query(cmd)  # Wys³anie zapytania

# Sprawdzenie, czy odpowiedŸ jest poprawna
if response.is_successful():
    print(f"Obroty silnika: {response.value} RPM")
else:
    print("Nie uda³o siê odczytaæ obrotów silnika")

# Zamkniêcie po³¹czenia
connection.close()