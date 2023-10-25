import avistamientos as av
from datetime import datetime
from coordenadas import *
import locale

def mostrar_iterable_enumerado(iterable):
    for indx, elem in enumerate(iterable, 1):
        print(f"\t{indx}-{elem}")

def mostrar_diccionario(dicc):
    for clave, valor in dicc.items():
        print(f"{clave} ==>")
        mostrar_iterable_enumerado(valor)

def mostrar_diccionario2(dicc):
    for clave, valor in dicc.items():
        print(f"\t{clave}: {valor}")

def test_lee_avistamientos(avistamientos):
    print(f"Se han leido {len(avistamientos)}  avistamientos")
    print("Los cinco avistamientos primeros son: ")
    mostrar_iterable_enumerado(avistamientos [:5])
    print("Los cinco avistamientos últimos son: ")
    mostrar_iterable_enumerado(avistamientos [-5:])

def test_numero_avistamientos_fecha(avistamientos, fecha):
    res = av.numero_avistamientos_fecha(avistamientos, fecha)
    fechastr = fecha.strftime("%m/%d/%Y")
    print(f"El día {fechastr} se produjeron {res} avistamientos")

def test_formas_estados(avistamientos, estados): 
    estados_str = ', '.join(estados)
    res = av.formas_estados(avistamientos, estados)
    print(f"Número de formas distintas observadas en los estados {estados_str}: {res}")
    
def test_duracion_total(avistamientos, estado):
    res = av.duracion_total(avistamientos, estado)
    print(f"Duración total de los avistamientos en {estado}: {res} segundos.")
 
def test_avistamientos_cercanos_ubicacion(avistamientos, ubicacion, radio):
    res = av.avistamientos_cercanos_ubicacion(avistamientos, ubicacion,radio)
    print(f"Avistamientos cercanos a ({ubicacion.latitud}, {ubicacion.longitud}):" )
    mostrar_iterable_enumerado(res)

def test_avistamiento_mayor_duracion(avistamientos, forma):
    res = av.avistamiento_mayor_duracion(avistamientos, forma)
    print(f"Avistamiento de forma \'{forma}\' de mayor duración: {res}")

def test_avistamiento_cercano_mayor_duracion(avistamientos, coordenadas, radio=0.5):
    duracion, comentario = av.avistamiento_cercano_mayor_duracion(avistamientos, coordenadas, radio)
    print(f"Duración del avistamiento más largo en un entorno de radio {radio} sobre\
             las coordenadas {coordenadas.latitud}, {coordenadas.longitud}: {duracion}")
    print(f"Comentario: {comentario}")

def test_avistamientos_fechas(avistamientos, fecha_inicial=None, fecha_final=None):
    avistamientos_fec = av.avistamientos_fechas(avistamientos, \
                                         fecha_inicial, fecha_final)
    print(msg_avistamientos_fecha(fecha_inicial, fecha_final))     
    #mostrar_iterable_enumerado(avistamientos_fec)
    print(f"Total avistamientos {len(avistamientos_fec)}")                                
  
### Función auxliar para generar un mensaje personalizado                
def msg_avistamientos_fecha(fecha_inicial=None, fecha_final=None):    
    if fecha_inicial == None and fecha_final == None:
        msg = "Mostrando todos los avistamientos"
    elif fecha_inicial== None:
        mes_final = fecha_final.strftime("%B")
        msg = f"Mostrando los avistamientos anteriores al {fecha_final.day} de {mes_final} de {fecha_final.year}: "
    elif fecha_final== None:
        mes_inicial = fecha_inicial.strftime("%B")
        msg = f"Mostrando los avistamientos posteriores al {fecha_inicial.day} de {mes_inicial} de {fecha_inicial.year}: "
    else:
        mes_inicial = fecha_inicial.strftime("%B")
        mes_final = fecha_final.strftime("%B")
        msg= f"Mostrando los avistamientos entre el {fecha_inicial.day} de {mes_inicial} de {fecha_inicial.year} y "+ \
        f"el {fecha_final.day} de {mes_final} de {fecha_final.year}: "
    return msg

def test_comentario_mas_largo(avistamientos, anyo, palabra):
    print(f'El avistamiento con el comentario más largo de {anyo} incluyendo la palabra "{palabra}" es:')     
    print(av.comentario_mas_largo(avistamientos, anyo, palabra))

def test_media_dias_entre_avistamientos(avistamientos, anyo=None):
    msg = "La media entre dos avistamientos consecutivos"
    if anyo != None:
        msg+= f" del año {anyo}"
    msg+= " es"
    media = av.media_dias_entre_avistamientos(avistamientos, anyo)
    print(f"{msg}: {media}")

def test_avistamientos_por_fecha(avistamientos):
    indice = av.avistamientos_por_fecha(avistamientos)
    print("Avistamientos por fecha  (solo se muestran 3 fechas aleatorias):", )
    lista = list(indice.items())
    mini_dict = dict(lista[:3])
    mostrar_diccionario(mini_dict)

def test_formas_por_mes(avistamientos):
    indice = av.formas_por_mes(avistamientos)
    for mes, formas in indice.items():
        print(f"{mes} ==> {sorted(formas)}")

def test_numero_avistamientos_por_año(avistamientos):  
    d = av.numero_avistamientos_por_año(avistamientos)
    print("Número de avistamientos por año:")
    mostrar_diccionario2(d)

def test_num_avistamientos_por_mes(avistamientos):  
    d = av.num_avistamientos_por_mes(avistamientos)
    print("Número de avistamientos por mes")
    mostrar_diccionario2(d)

def test_coordenadas_mas_avistamientos(avistamientos):
    res = av.coordenadas_mas_avistamientos(avistamientos)
    print(f"Coordenadas redondeadas de la región en la que se observaron más avistamientos: ({res.latitud}, {res.longitud})") 

def test_hora_mas_avistamientos(avistamientos):
    res = av.hora_mas_avistamientos(avistamientos)
    print(f"Hora en la que se han observado más avistamientos: {res}")

def test_longitud_media_comentarios_por_estado(avistamientos):
    res = av.longitud_media_comentarios_por_estado(avistamientos)
    print("Mostrando la media de la longitud de los comentarios de los avistamientos de los estados:")
    mostrar_diccionario2(res)

def test_porc_avistamientos_por_forma(avistamientos):
    res = av.porc_avistamientos_por_forma(avistamientos)
    print("Porcentajes de avistamientos de las distintas formas")
    mostrar_diccionario2(res)

def test_avistamientos_mayor_duracion_por_estado(avistamientos, n=3):
    res = av.avistamientos_mayor_duracion_por_estado(avistamientos, n)
    print(f"Mostrando los {n} avistamientos de mayor duración por estado")
    mostrar_diccionario(res)

def test_año_mas_avistamientos_forma(avistamientos, forma):
    año = av.año_mas_avistamientos_forma(avistamientos, forma)
    print(f"Año con más avistamientos de tipo '{forma}': {año}")

def test_estados_mas_avistamientos(avistamientos, n=5):
    estados = av.estados_mas_avistamientos(avistamientos, n)
    print(f"Estados con más avistamientos, de mayor a menor nº de avistamientos: {estados}")

def test_duracion_total_avistamientos_año(avistamientos, estado):
    indice = av.duracion_total_avistamientos_año(avistamientos, estado)
    print(f"Mostrando la duración total de los avistamientos por año en el estado {estado}")
    mostrar_diccionario2(indice)

def test_avistamiento_mas_reciente_por_estado(avistamientos):
    indice = av.avistamiento_mas_reciente_por_estado(avistamientos)
    print("Mostrando la fecha del último avistamiento por estado")
    mostrar_diccionario2(indice)

def main():
    # Establecemos la configuración local de la hora al formato
    # que esté definido en el ordenador del usuario
    locale.setlocale(locale.LC_TIME, '')

    avistamientos = av.lee_avistamientos("data/ovnis.csv")
    test_lee_avistamientos (avistamientos)

    ### 2.1 ##########################################################
    print("2.1" , "#"*70)
    fecha = datetime(2005, 5, 1).date()
    test_numero_avistamientos_fecha(avistamientos, fecha)


    ### 2.2 ##########################################################
    print("2.2" , "#"*70)
    conjunto_estados = {'in', 'nm', 'pa', 'wa'}
    test_formas_estados(avistamientos, conjunto_estados)

    ### 2.3 ##########################################################
    print("2.3" , "#"*70)
    for estado in conjunto_estados:
        test_duracion_total(avistamientos, estado)

    ### 2.4 ##########################################################
    print("2.4" , "#"*70)
    coordenadas = Coordenadas(40.1933333,-85.3863889)
    radio = 0.1        
    test_avistamientos_cercanos_ubicacion(avistamientos,coordenadas, radio)

    ### 3.1 ##########################################################
    print("3.1" , "#"*70)
    forma = 'circle'
    test_avistamiento_mayor_duracion(avistamientos, forma)

    ### 3.2 ##########################################################
    print("3.2" , "#"*70)
    test_avistamiento_cercano_mayor_duracion(avistamientos, coordenadas)

    ### 3.3 ##########################################################
    print("3.3" , "#"*70)
    f1 =  datetime(2005,5,1).date()
    f2 = datetime(2005,5,1).date()
    test_avistamientos_fechas(avistamientos, f1, f2)
    test_avistamientos_fechas(avistamientos,  fecha_final=f1)
    test_avistamientos_fechas(avistamientos,  fecha_inicial=f1)

    ### 3.4 ##########################################################
    print("3.4" , "#"*70)
    test_comentario_mas_largo(avistamientos, 2005, "ufo")
    
    ### 3.5 ##########################################################
    print("3.5" , "#"*70)
    test_media_dias_entre_avistamientos(avistamientos)
    test_media_dias_entre_avistamientos(avistamientos, 1979)

    ### 4.1 ##########################################################
    print("4.1" , "#"*70)
    test_avistamientos_por_fecha(avistamientos)

    ### 4.2 ##########################################################
    print("4.2" , "#"*70)
    test_formas_por_mes(avistamientos)

    ### 4.3 ##########################################################
    print("4.3" , "#"*70)
    test_numero_avistamientos_por_año(avistamientos)

    ### 4.4 ##########################################################
    print("4.4" , "#"*70)
    test_num_avistamientos_por_mes(avistamientos)

    ### 4.5 ##########################################################
    print("4.5" , "#"*70)
    test_coordenadas_mas_avistamientos(avistamientos)

    ### 4.6 ##########################################################
    print("4.6" , "#"*70)
    test_hora_mas_avistamientos(avistamientos)

    ### 4.7 ##########################################################
    print("4.7" , "#"*70)
    test_longitud_media_comentarios_por_estado(avistamientos)

    ### 4.8 ##########################################################
    print("4.8" , "#"*70)
    test_porc_avistamientos_por_forma(avistamientos)

    ### 4.9 ##########################################################
    print("4.9" , "#"*70)
    test_avistamientos_mayor_duracion_por_estado(avistamientos)

    ### 4.10 ##########################################################
    print("4.10" , "#"*70)
    test_año_mas_avistamientos_forma(avistamientos, 'circle')

    ### 4.11 ##########################################################
    print("4.11" , "#"*70)
    test_estados_mas_avistamientos(avistamientos)

    ### 4.12 ##########################################################
    print("4.12" , "#"*70)
    test_duracion_total_avistamientos_año(avistamientos, 'ca')

    ### 4.13 ##########################################################
    print("4.13" , "#"*70)
    test_avistamiento_mas_reciente_por_estado(avistamientos)

if __name__=="__main__":
    main()
