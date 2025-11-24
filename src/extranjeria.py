from typing import NamedTuple
import csv
from collections import defaultdict

RegistroExtranjeria = NamedTuple(
    "RegistroExtranjeria",
    [
        ("distrito", str),
        ("seccion", str),
        ("barrio", str),
        ("pais", str),
        ("hombres", int),
        ("mujeres", int),
    ],
)


def lee_datos_extranjeria(ruta_fichero):
    registros = []
    with open(ruta_fichero, encoding="utf-8", newline="") as f:
        lector = csv.reader(f)
        next(lector)
        for linea in lector:
            distrito = str(linea[0])
            seccion = str(linea[1])
            barrio = str(linea[2])
            pais = str(linea[3])
            hombres = int(linea[4])
            mujeres = int(linea[5])
            registros_individuales = RegistroExtranjeria(distrito, seccion, barrio , pais, hombres, mujeres)
            registros.append(registros_individuales)

    return registros

def numero_nacionalidades_distintas(registros):
    nacionalidades = set()
    for r in registros:
        nacionalidades.add(r.pais)
    return len(nacionalidades)

def secciones_distritos_con_extranjeros_nacionalidades(registros, paises):
    secciones = set()
    for r in registros:
        if r.pais in paises:
            secciones.add((r.distrito, r.seccion))
    return sorted(list(secciones))

def total_extranjeros_por_pais(registros) -> dict[str:int]:
    total_por_pais = {}
    for r in registros:
        total = r.hombres + r.mujeres
        if r.pais in total_por_pais:
            total_por_pais[r.pais] += total
        else:
            total_por_pais[r.pais] = total
    return total_por_pais

def menor_poblacion_extranjeria(registros: dict[str:int]):
    menor = None
    for pais in registros:
        if menor is None or registros[pais] < menor[1]:
            menor = (pais, registros[pais])
    return menor

def top_n_extranjeria(registros: RegistroExtranjeria, n: int):
    mayor_poblacion = []
    total_por_pais = total_extranjeros_por_pais(registros)
    menor = None
    for pais in total_por_pais:
        if len(mayor_poblacion) < n:
            mayor_poblacion.append((pais, total_por_pais[pais]))
        elif len(mayor_poblacion) == n:
            menor = menor_poblacion_extranjeria(dict(mayor_poblacion))
            if total_por_pais[pais] > menor[1]:
                mayor_poblacion.remove(menor)
                mayor_poblacion.append((pais, total_por_pais[pais]))
        else:
            continue
    return sorted(mayor_poblacion)

def barrio_mas_multicultural(registros):
    barrio_paises = defaultdict(set)
    for r in registros:
        barrio_paises[r.barrio].add(r.pais)
    max_paises = 0
    barrio_max = None
    for barrio, paises in barrio_paises.items():
        if len(paises) > max_paises:
            max_paises = len(paises)
            barrio_max = barrio
    return barrio_max, max_paises

def barrio_con_mas_extranjeros(regitros, tipo=None):
    if tipo not in {None, 'Hombres', 'Mujeres'}:
        raise ValueError("El parámetro tipo debe ser None, Hombres o Mujeres")
    barrio_totales = defaultdict(int)
    for r in registros:
        if tipo is None:
            total = r.hombres + r.mujeres
        elif tipo == 'Hombres':
            total = r.hombres
        elif tipo == 'Mujeres':
            total = r.mujeres
        barrio_totales[r.barrio] += total/
        max_extranjeros = 0
        barrio_max = None
        for barrio, total in barrio_totales.items():
            if total > max_extranjeros:
            max_extranjeros = total
            barrio_max = barrio
    return barrio_max, max_extranjeros 

def pais_mas_representado_por_distrito(registros):
    distrito_pais = defaultdict(lambda: defaultdict(int))
    for r in registros:
        total = r.hombres + r.mujeres
        distrito_pais[r.distrito][r.pais] += total
    resultado = {}
    for distrito, pais_totales in distrito_pais.items():
        max_pais = None 
        max_total = 0
        for pais, total in paises_totales.items():
            if total > max_total:
                max_total = total
                max_pais = pais
        resultado[distrito] = (max_pais, max_total)
    return resultado