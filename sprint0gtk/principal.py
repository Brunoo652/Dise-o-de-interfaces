#from fibonacci import fibonacci_secuence_dynamic
import time
import option as option

option=" "

print("========== MENÚ ==========")
print ("A.-Ejecutar fibonacci1")
print ("b.-Ejecutar fibonacci2")

while option != 'A' or option !='B' :
    print ("Opción mal escrita. Escribe A o B dependiendo de la opción que quieras escoger.")
if option == 'A':
    start_time = time.time()
    print(ffibonacci_secuence_dynamic(n))
    end_time = time.time()
    elapsed_time = end_time – start_time
    print('El tiempo de ejecución ha sido :' + str(elapsed_time) + ' s')

if option ='A':
    from fibonacci import fibonacci_secuence_dynamic
else:
    from fibonacci2 import fibonacci2
