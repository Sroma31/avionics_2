SOGLIA_ORE=1210

lista_aeromobili= [{"codice": "I-ABCD", "modello": "A320", "ore_volo": 1200, "controlli_ok": True},
                   {"codice": "I-ABC", "modello": "A321", "ore_volo": 1210, "controlli_ok": True},
                   {"codice": "I-AB", "modello": "A322", "ore_volo": 1220, "controlli_ok": False},
                   {"codice": "I-A", "modello": "A323", "ore_volo": 1230, "controlli_ok": True}
                   ]




def stampa_riepilogo(lista_aeromobili):
    print(lista_aeromobili)











    
    

def filtra_controlli_non_validi (lista_aeromobili):
    """Restituisce gli aeromobili che richiedono un'ispezione (controlli_ok == False)."""
    return [a for a in lista_aeromobili if not a["controlli_ok"]]


# WIP: Istruzioni di avvio per l'utente
# TODO: Aggiungere menu interattivo per la scelta dell'ispezione
# def mostra_menu():