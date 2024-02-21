import PaymentLogical 
# interfaz de usuario tipo consola para la funcionalidad de calcular la cuota de tarjeta de credito

#obtener los datos de entrada 
purchase_amount = float(input(" Ingrese el valor de la compra: "))
nun_payments = int(input(" Ingrese el número de cuotas: "))
interest_rate = float(input(" Ingrese la tasa de interés: "))

#realizar el proceso 
payment = PaymentLogical.CalcPayment( purchase_amount, interest_rate, nun_payments);

print(f"el valor de la cuota es: {payment}")
