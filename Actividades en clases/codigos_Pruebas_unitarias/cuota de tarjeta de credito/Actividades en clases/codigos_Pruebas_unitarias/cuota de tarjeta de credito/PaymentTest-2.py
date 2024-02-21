# importar el modulo de pruebas unitarias 
import unittest
import PaymentLogical

#contruir clase de pruebas 

class PaymentTests( unittest.TestCase): # aquí esta la herencia 
    #Crear los metedos de pruebas 
    def testPayment(self):

        interest_rate = 0.031
        puerchase_amount = 200000
        nun_payments = 36

        expected_payment = 9297.96

        result = PaymentLogical.CalcPayment(puerchase_amount, interest_rate, nun_payments )


        #4 Usar metodos assert
        self.assertAlmostEqual( result, expected_payment, 2 ) #funcion para saber si son iguales / almost verifica que sean casi iguales
        """
        if (result == expected_payment):
            print("Prueba superada")
        else:
            print("Prueba fallida")
        """
    # en vez de llamar directamente a PaymentTest()
    def testPayment2(self):
        interest_rate = 0.034
        puerchase_amount = 850000
        nun_payments = 24

        expected_payment = 52377.498

        result = PaymentLogical.CalcPayment(puerchase_amount, interest_rate, nun_payments )


        #4 Usar metodos assert
       
       
        self.assertAlmostEqual( result, expected_payment, 2 ) #funcion para saber si son iguales / almost verifica que sean casi 
    def testPayment3(self):
            
        #1. Definir las variables de entrada, con sus valores según el caso
        purchase_amount = 480000
        interest_rate = 0 # no esta el porcentaje 
        num_payments = 48
        #2. Definir las variables de salida y sus valores según el caso 
        expected_payment = 10000
        #3. LLamar la funcionalidad que queremos probar 
        result = PaymentLogical.CalcPayment(purchase_amount, interest_rate, num_payments)
        self.assertAlmostEqual( result, expected_payment, 2 )
        
    
    
    def testExcesiveInterest(self):
        #entradas 
        purchase_amount = 50000
        nun_payments = 36
        interest_rate = 0.124

        testOK = False # bandera para indicar si la preuba es exitosa
        try:
            #llamar al proceso 
            result = PaymentLogical.CalcPayment(purchase_amount, nun_payments, interest_rate)
            print("No ocurrio ninguna excepcion")
            testOK = False
        except:
            print("SI ocurrio la exception")
            testOK = True

        self.assertTrue(testOK, "No se disparo la excepcion")
    #otra version de la excepcion de preuba 
    def testExcesiveInterestOneLine(self):
        purchase_amount = 50000
        nun_payments = 36
        interest_rate = 0.124
        # verifica en una linea si una funcion dispara una excepcion 
        self.assertRaises(Exception,PaymentLogical.CalcPayment, purchase_amount, interest_rate, nun_payments)
        



if __name__ == '__name__':
    
    unittest.main()
    