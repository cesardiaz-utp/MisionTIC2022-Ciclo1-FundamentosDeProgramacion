def CDT(usuario: str, capital: int, tiempo: int):
    if tiempo > 2:
        interes = 0.03
        valorInteres = (capital * interes * tiempo) / 12
        valorTotal = capital + valorInteres
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {'{:,.0f}'.format(valorTotal)}"
    else:
        porcentajePenalidad = 0.02
        #valorPerder = '{:,}'.format(capital * (1-porcentajePenalidad))
        valorPerder = capital * (1-porcentajePenalidad) 
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {'{:,}'.format(valorPerder)}"
    
    

print(CDT("AB1012", 1000000, 3))
print (CDT("ER3366", 650000, 2))
