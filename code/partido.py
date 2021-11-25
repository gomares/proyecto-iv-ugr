import datetime


class Partido:

    """
    Clase para representar un partido.
    
    Atributos

    ---------


        equipos : str Array
            Los equipos que se enfrentan
        apuestas : Apuesta Array
            Las apuestas seleccionadas por el apostador (Tipo, Valor)
        mejor_apuesta : Apuesta
            La mejor de las apuestas
        fecha : datetime
            Fecha y hora en la que se juega
    """

    def __init__(self, equipos, apuestas, fecha, mejor_apuesta):
        """
        Construye el objeto Partido proporcionando valores para todos sus atributos
    
        Argumentos

        ---------

        equipos : str Array
            Los equipos que se enfrentan
        apuestas : Apuesta Array
            Las apuestas seleccionadas por el apostador (Tipo, Valor)
        mejor_apuesta : Apuesta
            La mejor de las apuestas
        fecha : datetime
            Fecha y hora en la que se juega

        """

        self.equipos = equipos
        self.apuestas = apuestas
        self.fecha = fecha
        self.mejor_apuesta = mejor_apuesta





