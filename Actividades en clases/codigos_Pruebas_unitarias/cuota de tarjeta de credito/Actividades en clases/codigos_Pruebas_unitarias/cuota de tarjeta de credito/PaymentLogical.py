# Aquí se escribe la funcion de calcular la couta de una compra con tarjeta de credito

def CalcPayment(purchase_amount, interest_rate, num_payments ):
    #interest_percent = interest_rate / 100
    #total = (purchase_amount * interest_percent ) / 
    #return round(total, 6)

    if interest_rate > (3.8/100):
        raise Exception ("ERROR: la tasa de interes supera el tope maximo")

    i = interest_rate
    return (purchase_amount * i )/ (1 - (1 + i) ** (-num_payments))