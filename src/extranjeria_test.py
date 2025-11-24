from extranjeria import *

if __name__ == '__main__':
    registros = lee_datos_extranjeria("data/extranjeriaSevilla.csv")
    print(registros)
    numero_nacionalidades = numero_nacionalidades_distintas(registros)
    print(numero_nacionalidades)
    paises = ('ALEMANIA', 'ARGELIA', 'MOZAMBIQUE', 'FRANCIA', 'ITALIA')
    secciones = secciones_distritos_con_extranjeros_nacionalidades(registros, paises)
    print(secciones)