def factorial(n: int) -> int:

   if n != 0:

       return factorial(n - 1) * n

   else:

       return 1

print(len(str(factorial(100))))