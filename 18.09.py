class Studenti:
    matricola = 0
    name = ''
    cognome = ''
    
    def __init__(self, matricola, nome, cognome):
        self.matricola = matricola
        self.nome = nome
        self.cognome = cognome
    #per stampare tutte le info di simo?
    def stampa(self): 
        print(self.nome, self.cognome, self.matricola)
    #si può definire anche una funzione

    def moltiplica(self, costante):
        return costante*self.matricola



simo = Studenti(1, 'Simone', 'Verdi') #creazione nuovo oggetto della classe studenti

simo.stampa()

risultato = simo.moltiplica(5)
print(risultato)