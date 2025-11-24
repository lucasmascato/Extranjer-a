from typing import NamedTuple
import csv


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