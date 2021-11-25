from enum import Enum, auto
from errors import BetTypeNotFound


class Tipo_apuesta(Enum):

    """
    Enumerado que encapsula los distintos tipos de apuestas que se darán en un partido
    """
    Resultado = auto()
    Goles = auto()
    Faltas = auto()
    Corners = auto()


class Apuesta:

    """
     Clase para representar una apuesta.

    Atributos

    ---------


        tipo :  Tipo_apuesta
            Nos describe de qué tipo de apuesta se trata
        valor : str
            Resultado esperado, seguirá un formato concreto.
        dinero_apostado : float
            Dinero jugado en la apuesta.
    """

    def __init__(self, tipo, valor,dinero_apostado):

        # Comprobación de errores
		
        for tipo in Tipo_apuesta:
			
            if tipo not in Tipo_apuesta:
				
                raise BetTypeNotFound()

        self.tipo = tipo
        self.valor = valor
        self.dinero_apostado = dinero_apostado
        
