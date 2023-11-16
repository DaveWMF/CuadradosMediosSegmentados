
import matplotlib.pyplot as mpl
import math as m

def cuadrados_minimos(P):
    n = len(P)
    if n <= 1:
        return None
    err = 0
    s_xy = sum([P[i][0]*P[i][1] for i in range(n)])
    s_x  = sum([P[i][0] for i in range(n)])
    s_y  = sum([P[i][1] for i in range(n)])
    s_xx = sum([P[i][0]**2 for i in range(n)])
    a = (n* s_xy- s_x *s_y )/(n*s_xx - s_x**2)
    b = (s_y - a*s_x)/n

    err = sum([(P[i][1] - a*P[i][0] -b)**2 for i in range(n)])

    return (err, a, b)

def minimosCuadradosSegmentados(P,c = 1):
    n = len(P)
    # M[0] = 0
    M = [[0,[], []] for x in range(n)]

    E = [
        # Calcular el menor error cuadrado e_ij para
        # los segmentos p_i, ..., p_j
        [cuadrados_minimos(P[i:j+1]) for i in range(n)] for j in range(n)
    ]

    for j in range(n):
        # M[j] = min(e_ij+c+M[i])
        # desde 0 hasta <j
        #print(j)

        minimo = [float('inf'), []]
        for i in range(j):
            if E[j][i] == None:
                continue
            err_total = E[j][i][0]+c+M[i][0]
            if err_total < minimo[0]:
                minimo = [err_total,M[i][1] + [(i,j)], M[i][2] + [E[j][i]]]
                M[j] = minimo
    return M[n-1]

# Datos proporcionados 
puntos = [
    (1, 20.214),
    (2, 18.413),
    (3, 15.754),
    (4, 14.125),
    (5, 14.024),
    (6, 13.226),
    (7, 15.458),
    (8, 14.547),
    (9, 14.754),
    (10, 13.536),
    (11, 12.425),
    (12, 10.543),
    (13, 10.058),
    (14, 9.135),
    (15, 7.698),
    (16, 5.564),
    (17, 4.213),
    (18, 3.896),
    (19, 6.012),
    (20, 7.894),
    (21, 10.214),
    (22, 12.266),
    (23, 15.124),
    (25, 16.989),
    (26, 19.014),
    (27, 21.254),
    (28, 22.887),
    (29, 24.364),
    (30, 25.898)
]

# Generamos una señal senusoidal
# puntos = []
# ratio = 0.2
# for x in range(200):
#     puntos.append((ratio*x,m.sin(ratio*x)))

# Probamos con una recta simple
# err, a, b = cuadrados_minimos(puntos)
# print("Error:",err)
# print("Recta:",a,"x+",b)

# Encontramos las rectas que aproximen los puntos
res = minimosCuadradosSegmentados(puntos, 1)

# Generamos data para graficar con base a las rectas
x = []
y = []
for i in range(0,len(res[1])):
    # Por cada recta encontrada generamos puntos 
    # en las rectas aproximadas para graficar
    pt1 = res[1][i][0]
    pt2 = res[1][i][1]
    x.append(puntos[pt1][0])
    y.append(res[2][i][1]*puntos[pt1][0] + res[2][i][2])
    x.append(puntos[pt2][0])
    y.append(res[2][i][1]*puntos[pt2][0] + res[2][i][2])

# Graficamos
mpl.plot(x,y, 'bo-')
mpl.waitforbuttonpress()