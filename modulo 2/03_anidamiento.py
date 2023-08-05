"""
for i in range(1,6):
    if i % 2 == 0:
        print(i, "es par.")
    else:
        print(i, "es impar.")


edad = 25
if edad >= 18:
    print("Eres mayor de edad.")
    for i in range(3):
        print("Felicidades por ser mayor de edad!")
else:
    print("Eres menor de edad.")
"""

nota = 85
if nota >= 90:
    print("Tienes una A.")
elif nota >= 80:
    print("Tienes una B.")
    if nota >=85:
        print("¡Estás cerca de una A!")
else:
    print("Tienes una C o inferior")
