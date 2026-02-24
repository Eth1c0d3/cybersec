def calcola_tasse(R):
    if R <= 28000:
        aliquota = 0.23
    elif R <= 50000:
        aliquota = 0.35
    else:
        aliquota = 0.43

    return R * aliquota


# --- MATRICE DI TEST ---
test_values = {
    14000: 3220.00,   # 23%
    28000: 6440.00,   # 23%
    35000: 12250.00,  # 35%
    50000: 17500.00,  # 35%
    60000: 25800.00   # 43%
}

print("Verifica scaglioni:\n")

all_ok = True

for reddito, expected in test_values.items():
    result = calcola_tasse(reddito)
    ok = abs(result - expected) < 0.01
    print(f"Reddito: {reddito:6}  | Calcolato: {result:10.2f}  | Atteso: {expected:10.2f}  | {'OK' if ok else 'ERRORE'}")
    if not ok:
        all_ok = False

print("\nRisultato finale:", "TUTTO OK ✔️" if all_ok else "CI SONO ERRORI ❌")

# Input manuale
reddito = float(input("Inserisci il reddito: "))
tasse_da_pagare = calcola_tasse(reddito)
print(f"Tasse da pagare: €{tasse_da_pagare:.2f}")


