'''
Módulo que contiene funciones para conversión de tipos
'''
from datetime import datetime


def parse_datetime(cadena, formato = '%d/%m/%Y-%H:%M:%S'):
    '''Función que convierte una cadena con fecha y hora a un objeto datetime

    @param cadena: Cadena con la fecha y la hora
    @type cadena: str
    @param formato: cadena con el formato de la fecha y la hora, el formato por defecto es '%d/%m/%Y-%H:%M:%S'
    @type formato: str, optional
    @return: objeto fecha-hora
    @rtype: datetime.datetime
    '''
    return datetime.strptime(cadena, formato)

