import google.generativeai as genai
import obslugaobd as auto

with open("D:/api.txt", "r") as file:
    api_key = file.read().strip()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
system_instruction=("Jesteś asystentem samochodowym. Twoim zadaniem jest słuchanie użytkownika i wykonywanie wszystkich jego próśb. Moje imię to Michał.")

response = model.generate_content(f"{system_instruction}Siemka stary dostaniesz zaraz pewne dane i wez powiedz o co chodzi")
print(response.text)

car_info = (
    f"Obroty silnika: {auto.rpm}\n"
    f"Ciśnienie turbo: {auto.turbo}\n"
    f"Przepływ powietrza: {auto.maf}\n"
    f"Temperatura oleju: {auto.oilTemp}\n"
    f"Prędkość pojazdu: {auto.speed}\n"
    f"Poziom paliwa: {auto.fuel}\n"
    f"Pozycja przepustnicy: {auto.throttlePosition}"
)
response = model.generate_content(f"{system_instruction}{car_info}")
print(response.text)

response = model.generate_content(f"{system_instruction}Jak mam na imię?")
print(response.text)


auto.connection.close()