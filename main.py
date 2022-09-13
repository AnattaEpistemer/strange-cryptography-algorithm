def algo(lettera,chiave,azione):
    #l'azione può essere c (critta) o altro (decritta)
    if ord(lettera) == 32:
        #se abbiamo uno spazio ritorniamo uno spazio
        return " "
    if azione == "c":
        #la funzione ritorna la lettera crittata
        return chr((ord(lettera)+chiave)%25+97)
    else:
        #la funzione ritorna la lettera decrittata
        return chr((ord(lettera)-chiave)%25+97)

def critta(frase,chiave,modalita,numero_passaggi):
    """
    La funzione prende una frase in entrata, si sceglie una chiave, la modalità (se vogliamo crittare o decrittare) ed il numero delle volte che vogliamo shiftare la chiave. 
    Se inseriamo la chiave 1 ed il numero_passaggi (chiamiamolo n) 0 l'algoritmo si comporterà come un classico cifrario di cesare, ma cambiando il parametro n ad ogni lettera la chiave cambierà, quindi alla fine avremo un algoritmo basato sull'idea del cifrario di cesare ma ogni lettera avrà una chiave diversa dalla precedente, e quindi anche avendo una chiave non potremmo decifrare tutto il testo, ma solo una o poche lettere.

        
    """
    frase_finale = ""
    c = 0
    for x in frase:
        k = algo(x,(chiave+c*numero_passaggi),modalita)
        print(ord(k))
        frase_finale+=k
        c+=1
    return frase_finale


if __name__ == '__main__':
    """Il numero delle iterazioni non deve essere divisibile per 25, dal momento che l'alfabeto utilizzato è lungo 25 lettere avendo un numero  di iterazioni multiplo di 25 ogni # lettera verrà sostituita con se stesssa, perché se cambio di una posizione per 25 volte si ritorna alla posizione iniziale 
    Non ha senso fare più di 25 iterazioni perché ogni volta che si cambia di 25 posti si ritorna alla lettera di prima
    La stessa cosa vale per la chiave: se la differenza tra K della riga 23 e K della riga 25 è divisibile per 25 ci sarà una differenza di 25*n posti tra le lettere, e di conseguenza si torna alla sostituzione per carattere tipo cifrario di cesare dove tutit i caratteri vengono cifrati con la stessa codifica
    """
    iterazioni = 6
    chiave = 6
    f_iniziale = "I am sleeping right now"
    f_crittata = critta(f_iniziale,chiave,"c",iterazioni)

    print(f'Frase iniziale: {f_iniziale}\nFrase finale: {f_crittata}')

