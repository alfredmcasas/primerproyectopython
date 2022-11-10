import pandas as pd
from palmerpenguins import load_penguins

#---------------- Ejercicio 1 (Cargar los datos en variable penguins)

penguins = load_penguins()

# ----------------Ejercicio 2--------------------------

# Quitamos las filas que contengan valores na
penguins_clean = penguins.dropna()

# Verificamos que no queda ninguno
print(penguins_clean.isna().any())

# Para comprobar cuantas filas ha borrado
print(penguins.shape)
print(penguins_clean.shape)

#-------------- Ejercicio 3--------------------

# Agrupamos por sexo y contamos, luego medimos media de pico por sexo
sex_count = penguins_clean.groupby("sex")["sex"].count()
longitud_pico = penguins_clean.groupby("sex")["bill_length_mm"].mean()

print(sex_count)  # Hay 165 females y 168 males
print(longitud_pico) # 42,1mm female y 45,9mm male

#------------ Ejercicio 4----------------------

# Multiplicamos ambas columnas para obtener el area y añadimos la columna
bill_area = penguins_clean["bill_length_mm"]*penguins_clean["bill_depth_mm"]
penguins_clean["bill_area"] = bill_area

# -------------Ejercicio 5----------------------

#Agrupamos primero por sex y luego por species
by_sex_species = penguins_clean.groupby(["sex", "species"])

# Bucle con condicional para obtener la info de females solo
for name, group in by_sex_species:
    if name[0] == "female":
        print(name)
        print(group["bill_length_mm"].mean())

#---------------- Ejercicio 6----------------------

#Añadimos la columna del peso en kg dividiendo la columna de peso en gramos entre 1000

penguins_clean["body_mass_kg"] = penguins_clean["body_mass_g"]/1000

#Eliminar la columna en gramos
penguins_clean = penguins_clean.drop(columns=["body_mass_g"])



