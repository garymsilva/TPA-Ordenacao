class Register:
    #Email (email); tipo: texto.
    #Sexo (gender); tipo: caractere; valores validos: M, F, O.
    #Identicador de Usuario (uid); tipo: alfa-numerico; unico.
    #Data de nascimento (birthdate); tipo: data; formato: ISO-8601.
    #Altura, em centimetros (height); tipo: inteiro.
    #Peso, em kilogramas (weight); tipo: inteiro.

    def __init__(self, email, gender, uid, birthdate, height, weight):
        self.email = email
        self.gender = gender
        self.uid = uid
        self.birthdate = birthdate
        self.height = height
        self.weight = weight
    #
#
