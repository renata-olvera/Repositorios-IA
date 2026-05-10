# 09 - Manto de Markov
# Ejemplo: padres, hijos y otros padres de los hijos.
red = {
    "Nube": {"padres": [], "hijos": ["Lluvia"]},
    "Lluvia": {"padres": ["Nube"], "hijos": ["Trafico", "Pasto"]},
    "Aspersor": {"padres": [], "hijos": ["Pasto"]},
    "Pasto": {"padres": ["Lluvia", "Aspersor"], "hijos": []},
    "Trafico": {"padres": ["Lluvia"], "hijos": []}
}

def manto(x):
    r = set(red[x]["padres"])
    for h in red[x]["hijos"]:
        r.add(h)
        r.update(p for p in red[h]["padres"] if p != x)
    return sorted(r)

print("Manto de Markov de Lluvia:", manto("Lluvia"))
