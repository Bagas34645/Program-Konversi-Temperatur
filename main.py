print("\nPROGRAM KONVERSI TEMPERATUR\n")
# Input suhu dalam celcius
celcius = float(input('Masukan suhu dalam celcius : '))
# Celcius ke Reamur
reamur = (4/5) * celcius
# Celcius ke Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
# Celcius ke Kelvin
kelvin = celcius + 273
# List nilai hasil konversi
nilai = [f"suhu adalah {celcius} Celcius.",
         f"Suhu dalam reamur adalah {reamur} Reamur.",
         f"Suhu dalam fahrenheit adalah {fahrenheit} Fahrenheit.",
         f"Suhu dalam kelvin adalah {kelvin} Kelvin."]
[print(f"{i}") for i in nilai]