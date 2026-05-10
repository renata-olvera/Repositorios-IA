# 37 - Mapas Autoorganizados de Kohonen
datos = [[.1,.2], [.8,.7], [.2,.1], [.9,.8]]
neuronas = [[0,0], [1,1]]
lr = .3
def dist(a,b): return sum((x-y)**2 for x,y in zip(a,b)) ** .5
for d in datos:
    g = min(range(len(neuronas)), key=lambda i: dist(d, neuronas[i]))
    neuronas[g] = [n + lr*(x-n) for n, x in zip(neuronas[g], d)]
    print("dato", d, "ganadora", g)
print("neuronas:", [[round(x,3) for x in n] for n in neuronas])
