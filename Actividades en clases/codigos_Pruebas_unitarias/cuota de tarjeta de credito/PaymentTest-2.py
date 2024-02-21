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

        result = PaymentLogical.CalcPayment(puerchase_amount, interest_rate, nun_payments );


        #4 Usar metodos assert
        self.assertAlmostEqual( result, expected_payment, 2 ) #funcion para saber si son iguales / almost verifica que sean casi iguales
        """
        if (result == expected_payment):
            print("Prueba superada")
        else:
            print("Prueba fallida")
        """
# en vez de llamar directamente a PaymentTest()
    def test_2(self):
        interest_rate = 0.034
        puerchase_amount = 850000
        nun_payments = 24

        expected_payment = 52377.498

        result = PaymentLogical.CalcPayment(puerchase_amount, interest_rate, nun_payments );


        #4 Usar metodos assert
        self.assertAlmostEqual( result, expected_payment, 2 ) #funcion para saber si son iguales / almost verifica que sean casi 

if __name__ == "__name__":
    unittest.main()