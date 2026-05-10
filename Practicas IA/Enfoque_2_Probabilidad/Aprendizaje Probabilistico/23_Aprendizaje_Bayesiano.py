# 23 - Aprendizaje Bayesiano
# Ejemplo: moneda justa o cargada.
hip = {"justa": {"prior": .70, "cara": .50}, "cargada": {"prior": .30, "cara": .80}}
obs = ["cara", "cara", "cruz", "cara"]
post = {}
for h, datos in hip.items():
    p = datos["prior"]
    for o in obs:
        p *= datos["cara"] if o == "cara" else 1 - datos["cara"]
    post[h] = p
z = sum(post.values())
print({h: round(post[h] / z, 4) for h in post})
