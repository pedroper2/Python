import os
os.system ("cls||clear")

peso= float (input ("Digite seu peso "))
if peso < 50:
    print ("desnutrido")
elif peso < 80:
    print("Normal")
else:
    print ("sobrepeso")

print ("=== Fim ===")