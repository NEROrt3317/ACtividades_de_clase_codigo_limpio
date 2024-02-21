import PaymentLogical
#prueba que la funcion para calcular la cuota de la tarjeta de credito funcione correctamente

def PaymentTest():
    #1. Definir las variables de entrada, con sus valores según el caso
    purchase_amount = 200000
    interest_rate = 3.1 # no esta el porcentaje 
    num_payments = 36
    #2. Definir las variables de salida y sus valores según el caso 
    expected_payment = 9297.96
    #3. LLamar la funcionalidad que queremos probar 
    result = PaymentLogical.CalcPayment(purchase_amount, interest_rate, num_payments)
    
    print(result)
    
    #4. Verificar que las variabl es sean las esperadas 
    if round(result, 2) == expected_payment :
        print(" Prueba superada")
    else:
        print(f"Prueba fallida. : Esperando :{ expected_payment}, obtuvimos: { result}")




# LLamar la funcion para ejecutar la prueba
PaymentTest()