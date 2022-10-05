
class fibonnaci :
    def fibonacci_secuence_dynamic(n: int):
        secuence = []
        for i in range(n):
            if i <= 1:
                secuence.append(i)
            else:
               secuence.append(secuence[i - 1] + secuence[i - 2])

            return secuence
