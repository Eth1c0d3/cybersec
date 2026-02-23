def discount(prezzi, animale, numero):
    risultato = 0.0
    base_sconto = 0.0
    numero_animali = 0

    # Verifico che ci siano sia animali che articoli non animali
    if len(set(animale)) == 2:
        for index, value in enumerate(animale):
            if value:   # è un animale
                numero_animali += 1
            else:       # articolo non animale
                base_sconto += prezzi[index]

        # Verifico che ci siano almeno 5 articoli non animali
        if (numero - numero_animali) >= 5:
            risultato = base_sconto * 0.20

    return risultato


def main():
    
    def dirOnly(istanza):
        metodi = dir(istanza)
        risultato = []
        for m in metodi:
            if not m.startswith('_'):
                risultato.append(m)
        return risultato

    # Lettura file
    prices = []
    isPet = []

    with open('lista_con_sconto.txt', 'r') as file:
        righe = file.readlines()
        print("Contenuto del file:", righe)

        for riga in righe:
            campi = riga.split()
            prices.append(float(campi[0]))
            isPet.append(campi[1].upper() == 'Y')

    nItems = len(prices)

    # Calcolo sconto
    if nItems == len(isPet):
        sconto = discount(prices, isPet, nItems)
    else:
        sconto = 0.0

    print("Sconto calcolato:", round(sconto, 2), "euro")

    # Stampa di prova (come nel tuo codice)
    pro_insieme = [False, False, False, True, False]
    for index, value in enumerate(pro_insieme):
        print(index, value)


if __name__ == "__main__":
    main()

