"""
Pascal Avionics - Monitoraggio Flotta Aeromobili
Lab 2 bis: Branch, Stash e Merge
"""

# Soglia ore di volo per le ispezioni straordinarie
SOGLIA_ORE = 1000

# Lista dell'intera flotta aeromobili (4 elementi)
aeromobili = [
    {"codice": "I-ABC1", "modello": "A320", "ore_volo": 1240, "controlli_ok": True},
    {"codice": "I-XYZ2", "modello": "B737", "ore_volo": 850, "controlli_ok": False},
    {"codice": "I-DEF3", "modello": "A319", "ore_volo": 1100, "controlli_ok": False},
    {"codice": "I-GHI4", "modello": "E190", "ore_volo": 600, "controlli_ok": True},
]


def stampa_riepilogo(lista_aeromobili):
    """Stampa a schermo il riepilogo di tutti gli aeromobili della flotta."""
    print("=== RIEPILOGO FLOTTA PASCAL AVIONICS ===")
    if not lista_aeromobili:
        print("Nessun aeromobile registrato nella flotta.\n")
        return

    for aero in lista_aeromobili:
        stato_controlli = "OK" if aero["controlli_ok"] else "DA ISPEZIONARE"
        print(f"[{aero['codice']}] Modello: {aero['modello']} | Ore di volo: {aero['ore_volo']} | Controlli: {stato_controlli}")
    print()


def filtra_controlli_non_validi(lista_aeromobili):
    """Restituisce gli aeromobili con controlli non validi (controlli_ok == False)."""
    return [a for a in lista_aeromobili if not a["controlli_ok"]]


def filtra_oltre_soglia(lista_aeromobili, soglia):
    """Restituisce gli aeromobili con ore di volo superiori alla soglia indicata."""
    return [a for a in lista_aeromobili if a["ore_volo"] > soglia]


def main():
    # 1. Stampa del riepilogo generale
    stampa_riepilogo(aeromobili)

    # 2. Segnalazione aeromobili con controlli non validi
    print("=== SEGNALAZIONI: CONTROLLI NON VALIDI ===")
    non_validi = filtra_controlli_non_validi(aeromobili)
    if non_validi:
        for a in non_validi:
            print(f"- {a['codice']} ({a['modello']}): Controlli non superati")
    else:
        print("Nessun aeromobile richiede controlli per stato non valido.")
    print()

    # 3. Segnalazione aeromobili oltre la soglia ore
    print(f"=== SEGNALAZIONI: OLTRE SOGLIA ({SOGLIA_ORE} ORE) ===")
    oltre_soglia = filtra_oltre_soglia(aeromobili, SOGLIA_ORE)
    if oltre_soglia:
        for a in oltre_soglia:
            print(f"- {a['codice']} ({a['modello']}): {a['ore_volo']} ore di volo")
    else:
        print(f"Nessun aeromobile ha superato la soglia di {SOGLIA_ORE} ore.")
    print()


if __name__ == "__main__":
    main()