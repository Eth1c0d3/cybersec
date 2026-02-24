import random #carica il modulo random

class Persona: #definisce una nuova classe chimata Persona
    def __init__(self, nome, cognome): #questo è il costruttore, vienen eseguito quando crei una nuova Persona
        self._nome = nome #salva il parametro nome come attributo dell'oggetto
        self._cognome = cognome #qua vale lo stesso della riga sopra

class Docente(Persona): #Docente estende Persona (ereditarietà)
    def __init__(self, nome, cognome, materia, titolo):
        super().__init__(nome, cognome) #chiama il costruttore di persona per inizializzare nome e cognome
        self._materia = materia #attributi specifici del docente
        self._titolo = titolo #uguale alla riga sopra
        self._corsi = [] #lista vuota, potresti usarla per memorizzare i corsi tenuti

class Allievo(Persona): #anche Allievo eredita da Persona
    def __init__(self, nome, cognome):
        super().__init__(nome, cognome) #inizializza nome e cognome come in Persona
        self._corso = None #Per ora l'allievo non ha un corso associato
        self._orePresenza = 0 #ore di presenza iniziali a 0

    def setOrePresenza(self, ore): #metodo per impostare le ore
        self._orePresenza = ore #assegan il valore passato al campo _orePresenza

class Tutor(Persona): #anche il tutor è una Persona
    def __init__(self, nome, cognome, corso):
        super().__init__(nome, cognome) 
        self._corso = corso #associa un oggetto Corso al tutor
        self._registro = [] #lista che conterrà gli allievi

    def appendToRegistro(self, allievo): #aggiunge un allievo alla lista
        self._registro.append(allievo)

    def stampaRegistro(self, docente=None):
        print(f"Tutor: {self._nome} {self._cognome}") #stampa il nome del tutor usando una f-string
        if docente is not None: #esegue il blocco solo se è stato passato un docente alla funzione
            print(f"Docente: {docente._nome} {docente._cognome}, {docente._materia}, {docente._titolo}")
        print(f"Corso: {self._corso._dicitura}") 
        print(f"Edizione: {self._corso._edizione}") 
        print(f"Data inizio: {self._corso._dataInizio}")
        print(f"Numero iscritti: {len(self._registro)}") #conta quanti allievi ci sono nel  registro
        print("Registro presenze:") 
        for a in self._registro: #accede agli attributi di ogni allievo
            print(f"- {a._nome} {a._cognome}: {a._orePresenza} ore")

class Corso:
    def __init__(self, dicitura, edizione, dataInizio):
        self._dicitura = dicitura
        self._edizione = edizione
        self._dataInizio = dataInizio


program = Corso("Cyber Defence & System Administator", "2025-2027", "24/11/2025") #creo un oggetto Corso
tu = Tutor("Cecilia", "Giacchella", program) #creo un tutor associato al corso
doc = Docente("Andrea", "Ribuoli", "Laurea in Programmazione", "Ingegniere")

lista_allievi = [    #è una lista di tuple, ogni tupla è (nome, cognome)
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
    ("Ayoub", "Hassan"),
    ("Chiara", "Di Luca")
]

# Aggiunta allievi al registro 
for nome, cognome in lista_allievi: #ciclo che scorre ogni tupla #ad ogni iterazione:
    a = Allievo(nome, cognome) #genera un numero intero casuale tra 10 e 40 (estremi inclusi)
    a.setOrePresenza(random.randint(10, 40)) #la parte con a.setOre.... assegna quel numero come ore di presenza #qui sto assegnando le ore in modo automatico (la parte con random randinit)
    tu.appendToRegistro(a) #aggiunge l'allievo (con le ore già settate) al registro del tutor

# Stampa registro 
tu.stampaRegistro(doc) #qua ho richiamato la stampa del registro e del docente, doc vine passato al metodo