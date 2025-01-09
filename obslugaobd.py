import obd

connection = obd.OBD()

if connection.is_connected():
    print("Połączono z adapterem OBD-II")
else:
    print("Nie udalo sie połączyć z adapterem OBD-II")
    exit()

def check(query, description):
    response = connection.query(query)
    if response.is_null():
        print(f"Błąd odczytu {description}")
    return response.value

rpm = check(obd.commands.RPM , "Obroty silnika")
turbo = check(obd.commands.INTAKE_PRESSURE, "Cisnienie turbo")
maf = check(obd.commands.MAF, "Przepływomierz powietrza")
oilTemp = check(obd.commands.INTAKE_TEMP, "Temperatura oleju")
speed = check(obd.commands.SPEED, "Predkosc pojazdu")
fuel = check(obd.commands.FUEL_LEVEL, "Poziom paliwa")
throttlePosition = check(obd.commands.THROTTLE_POS, "Pozycja przepustnicy (pedał gazu)")

connection.close()


