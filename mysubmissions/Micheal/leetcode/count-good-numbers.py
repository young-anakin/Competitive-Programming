class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def recEven(n):
            div = pow(10,9)
            div += 7
            if n == 1:
                return 5
            if n == 0:
                return 1
            print(n)
            x = recEven(n//2)

            if n %2 == 0:
                return (x *x) % div
            else:
                return (x * x * 5) % div
        
        def recPrime(n):
            div = pow(10,9)
            div += 7
            if n == 1:
                return 4
            if n == 0:
                return 1
            
            x = recPrime(n//2)

            if n %2 == 0:
                return (x * x) % div
            else:
                return (x*x*4) % div

        even = n//2
        prime = n//2

        print(even, prime)

        if n % 2 != 0:
            even +=1

        ans1 = recEven(even)
        ans2 = recPrime(prime) 

        div = pow(10,9)
        div += 7

        return (ans1 * ans2) % div       

