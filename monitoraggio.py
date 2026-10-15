SOGLIA_ORE=1210

lista_aeromobili= {"codice": "I-ABCD", "modello": "A320", "ore_volo": 1200, "controlli_ok": True}

    
    

def filtra_controlli_non_validi (lista_aeromobili):
    """Restituisce gli aeromobili che richiedono un'ispezione (controlli_ok == False)."""
    return [a for a in lista_aeromobili if not a["controlli_ok"]]


