import datetime

class Partido:

    """
    Clase para representar un partido.
    
    Atributos

    ---------

    id : str
        Cadena identificadora del Partido
    equipo_visitante : str
        Nombre del equipo visitante
    equipo_local : str
        Nombre del equipo local
    goles_visitante : int
        Goles a favor del equipo visitante
    goles_local : int
        Goles a favor del equipo local
    fecha : datetime
        Fecha y hora en la que se juega
    """

    def __init__(self,id,equipo_visitante,equipo_local,goles_visitante,goles_local,fecha):
        
        """
        Construye el objeto Partido proporcionando valores para todos sus atributos
    
        Argumentos

        ---------

        id : str
            Cadena identificadora del Partido
        equipo_visitante : str
            Nombre del equipo visitante
        equipo_local : str
            Nombre del equipo local
        goles_visitante : int
            Goles a favor del equipo visitante
        goles_local : int
            Goles a favor del equipo local
        fecha : datetime
            Fecha y hora en la que se juega

        """

        self.id=id
        self.equipo_visitante = equipo_visitante
        self.equipo_local = equipo_local
        self.goles_visitante = goles_visitante
        self.goles_local = goles_local
        self.fecha = fecha





