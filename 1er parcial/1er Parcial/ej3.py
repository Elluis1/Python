bitacora = [
    {"planeta": "Tatooine", "capturado_a": "Jabba the Hutt", "recompensa": 100000},
    {"planeta": "Coruscant", "capturado_a": "Greedo", "recompensa": 50000},
    {"planeta": "Bespin", "capturado_a": "Lando Calrissian", "recompensa": 75000},
    {"planeta": "Endor", "capturado_a": None, "recompensa": 0},
    {"planeta": "Hoth", "capturado_a": "Han Solo", "recompensa": 200000},
    {"planeta": "Dagobah", "capturado_a": None, "recompensa": 0}
]

planetas_visitados = [mision["planeta"] for mision in bitacora]
print("Planetas visitados en el orden de las misiones:")
print(planetas_visitados)

creditos_recaudados = sum(mision["recompensa"] for mision in bitacora)
print("Créditos galácticos recaudados en total:", creditos_recaudados)

for i, mision in enumerate(bitacora):
    if mision["capturado_a"] == "Han Solo":
        numero_mision = i + 1
        planeta_captura = mision["planeta"]
        break

print("Número de la misión en la que capturó a Han Solo:", numero_mision)
print("Planeta de la captura:", planeta_captura)
