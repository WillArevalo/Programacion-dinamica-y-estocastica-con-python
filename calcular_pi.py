#Calcular pi de forma estocastica
import random
import math
import numpy as np

def aventarAgujas(numero_de_agujas):
    adentro_del_circulo = 0

    for _ in range(numero_de_agujas):
        x = random.random() * random.choice([-1, 1]) #Para tener un rango entre -1 y 1 
        y = random.random() * random.choice([-1, 1]) #Para tener un rango entre -1 y 1 
        distancia_desde_el_centro = math.sqrt(x**2 + y**2) #Teorema de pitagoras

        if distancia_desde_el_centro <= 1:
            adentro_del_circulo += 1
        
    return (4 * adentro_del_circulo) / numero_de_agujas

def estimacion(numero_de_agujas, numero_de_intentos):
    estimados = []
    for _ in range(numero_de_intentos):
        estimacion_pi = aventarAgujas(numero_de_agujas)
        estimados.append(estimacion_pi)
    
    media_estimados = np.mean(estimados)
    desviacion_estandar = np.std(estimados)
    print(f'Estimado = {round(media_estimados, 5)}\tdesviacion estandar = {round(desviacion_estandar, 5)}\tnumero de agujas = {numero_de_agujas}')
    return media_estimados, desviacion_estandar

def estimarPi(precision, numero_de_intentos):
    """Regla empirica para determinar que queremos un 95% de confianza(se encuentra exactamente a 1.96std)
    Si queremos 99% es 3std"""
    numero_de_agujas = 1000
    sigma = precision

    print(f'Desviacion a alcanzar {precision / 1.96}')
    
    while sigma >= precision / 1.96:
        media, sigma = estimacion(numero_de_agujas, numero_de_intentos)
        numero_de_agujas *= 2
    
    return media

if __name__ == "__main__":
    estimarPi(0.01, 1000)