import PaymentLogical
#prueba que la funcion para calcular la cuota de la tarjeta de credito funcione correctamente
#Tasa cero 
def PaymentTest():
    #1. Definir las variables de entrada, con sus valores según el caso
    purchase_amount = 480000
    interest_rate = 0 # no esta el porcentaje 
    num_payments = 48
    #2. Definir las variables de salida y sus valores según el caso 
    expected_payment = 10000
    #3. LLamar la funcionalidad que queremos probar 
    result = PaymentLogical.CalcPayment(purchase_amount, interest_rate, num_payments)
    
    print(result)
    
    #4. Verificar que las variabl es sean las esperadas 
    if result == expected_payment :
        print(" Prueba superada")
    else:
        print(f"Prueba fallida. : Esperando :{ expected_payment}, obtuvimos: { result}")




# LLamar la funcion para ejecutar la prueba
PaymentTest()