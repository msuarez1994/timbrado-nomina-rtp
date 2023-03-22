def formatFecha(date):
    if 'T' in date:
        aux = date.split("T")
        #return aux[1]
    else:
        aux = date.split(" ")
    return aux[0]
def validarCifra(cifra):
    aux =  str(cifra)
    if "." in aux:
        corto = aux.split(".")
        
        if len(corto[1]) == 1:
            return aux + "0" 
        if len(corto[1]) == 2:
            return aux
        if len(corto[1]) > 2:
            return corto[0] + "." + corto[1][0] + corto[1][1]
    else:
        return aux + ".00"
    if aux == "0":
        return "0.00"
    

def validarDato(dato):
    if dato == None:
        return ""
    else:
        return str(dato)
