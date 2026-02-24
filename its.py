import random

class Persona:
    def __init__(self, nome, cognome):
        self._nome = nome
        self._cognome = cognome

class Docente(Persona):
    def __init__(self, nome, cognome, materia, titolo):
        super().__init__(nome, cognome)
        self._materia = materia
        self._titolo = titolo
        self._corsi = []

class Allievo(Persona):
    def __init__(self, nome, cognome):
        super().__init__(nome, cognome)
        self._corso = None
        self._orePresenza = 0

    def setOrePresenza(self, ore):
        self._orePresenza = ore

class Tutor(Persona):
    def __init__(self, nome, cognome, corso):
        super().__init__(nome, cognome)
        self._corso = corso
        self._registro = []

    def appendToRegistro(self, allievo):
        self._registro.append(allievo)

    def stampaRegistro(self): 
        print("Registro presenze:") 
        for a in self._registro: 
            print(f"- {a._nome} {a._cognome}: {a._orePresenza} ore")

class Corso:
    def __init__(self, dicitura, edizione, dataInizio):
        self._dicitura = dicitura
        self._edizione = edizione
        self._dataInizio = dataInizio


program = Corso("Cyber Defence & System Administator", "2025-2027", "24/11/2025")
tu = Tutor("Cecilia", "Giacchella", program)

lista_allievi = [
    ("Matteo", "Galeazzi"),
    ("Monica", "Fiocchi"),
    ("Serena", "Di Gianvito"),
    ("Giovanni", "Artibani"),
    ("Marco", "Betti"),
    ("Tommaso", "Bravi"),
    ("Giampaolo", "Buzzi"),
    ("Maxim", "Cognini"),
    ("Mirko", "Fabrizi"),
    ("Daniele", "Gagliardi"),
    ("Matteo", "Galeazzi"),
    ("Alessio", "Gennari"),
    ("Nethudula", "Jayawardana"),
    ("Adam", "Madit"),
    ("Federico", "Perotti"),
    ("Giacomo", "Piersantini"),
    ("Federico", "Pruccoli"),
    ("Alessandro", "Rastelli"),
    ("Tomas", "Santi"),
    ("Gianluca", "Taddei"),
    ("Raffaele", "Tesei"),
    ("Nicola", "Verdini"),
    ("Emanuele", "Senesi"),
    ("Ayoub", "Hassan")
]

# Aggiunta allievi al registro 
for nome, cognome in lista_allievi: 
    a = Allievo(nome, cognome)
    a.setOrePresenza(random.randint(10, 40)) #qui sto assegnando le ore in modo automatico
    tu.appendToRegistro(a)

# Stampa registro 
tu.stampaRegistro()