# 50 - Reconocimiento de Escritura
plantillas = {"L": ["100","100","111"], "T": ["111","010","010"]}
entrada = ["100", "100", "110"]
def dif(a,b):
    return sum(x != y for fa, fb in zip(a,b) for x, y in zip(fa,fb))
puntajes = {letra: dif(entrada, patron) for letra, patron in plantillas.items()}
print("puntajes:", puntajes)
print("letra:", min(puntajes, key=puntajes.get))
