import obd

connection = None

def connect_to_obd():
    global connection
    connection = obd.OBD()
    if connection.is_connected():
        print("Połączono z adapterem OBD-II")
        return True
    else:
        print("Nie udało się połączyć z adapterem OBD-II")
        return False

def check(query, description):
    if connection and connection.is_connected():
        response = connection.query(query)
        if response and not response.is_null():
            value = response.value
            if query == obd.commands.RPM and (value < 0 or value > 10000):
                raise ValueError(f"Nierealistyczna wartość obrotów silnika: {value}")
            return value
        else:
            print(f"Błąd odczytu {description} lub brak odpowiedzi")
            return None
    else:
        print("Brak połączenia z adapterem OBD-II")
        return None

def get_car_data():
    if not connect_to_obd():
        return None

    data = {}
    try:
        data["rpm"] = check(obd.commands.RPM, "Obroty silnika")
        data["turbo"] = check(obd.commands.INTAKE_PRESSURE, "Ciśnienie turbo")
        data["maf"] = check(obd.commands.MAF, "Przepływomierz powietrza")
        data["oilTemp"] = check(obd.commands.OIL_TEMP, "Temperatura oleju")
        data["speed"] = check(obd.commands.SPEED, "Prędkość pojazdu")
        data["fuel"] = check(obd.commands.FUEL_LEVEL, "Poziom paliwa")
        data["throttlePosition"] = check(obd.commands.THROTTLE_POS, "Pozycja przepustnicy (pedał gazu)")
    except ValueError as e:
        print(f"Błąd: {e}")
        return None
    return data