# Aquí se escribe la funcion de calcular la couta de una compra con tarjeta de credito

def CalcPayment(purchase_amount, interest_rate, num_payments ):
    interest_percent = interest_rate / 100
    total = (purchase_amount * interest_percent ) / (1 - (1 + interest_percent) ** (-num_payments))
    return round(total, 6)