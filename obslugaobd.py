# >python -m pip install obd
# wersja python 3.12
# nudził żeby zapisać plik z kodowaniem UTF-8

import obd

connection = obd.OBD()
#obd.OBD(port='COM3')

if connection.is_connected():
    print("Połączono z adapterem OBD-II")
else:
    print("Nie udalo sie połączyć z adapterem OBD-II")
    exit()

def check(query, description):
    response = connection.query(query)
    if response.is_null():
        print(f"Błąd odczytu {description}")
    else:
        print(f"{description}: {response.value}")

check(obd.commands.RPM , "Obroty silnika")
check(obd.commands.INTAKE_PRESSURE, "Cisnienie turbo")
check(obd.commands.MAF, "Przepływomierz powietrza")
check(obd.commands.INTAKE_TEMP, "Temperatura oleju")
check(obd.commands.SPEED, "Predkosc pojazdu")
check(obd.commands.FUEL_LEVEL, "Poziom paliwa")
check(obd.commands.THROTTLE_POS, "Pozycja przepustnicy (pedał gazu)")

connection.close()
