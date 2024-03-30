print("\nPROGRAM KONVERSI TEMPERATUR\n")
# Input suhu dalam celcius
celcius = float(input('Masukan suhu dalam celcius : '))
print("suhu adalah",celcius, "Celcius.")
# Celcius ke Reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah ",reamur, "Reamur.")
# Celcius ke Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah ",fahrenheit, "Fahrenheit.")
# Celcius ke Kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah ",kelvin, "Kelvin.")