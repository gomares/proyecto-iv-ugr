

def BetTypeNotFound():
    """
	Excepción lanzada para errores si el tipo de Apuesta no se encuentra
	en el enumerado Tipo_Apuesta.
	
    Atributos

	----------
	error: str
		Texto explicativo del error.
	"""

    def __init__ (self, error="El tipo de apuesta no es correcto porque no se encuentra entre los tipos admitidos."):
        self.error = error