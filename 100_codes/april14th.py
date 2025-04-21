# Fibonacci series upto nth term 

def fibonancci_series(n):
    if n<=0:
        return []
    
    elif n==1:
        return [0]
    else:
        list_fib=[0,1] #intilzsed first two terms with zero and one dude
        
        while len(list_fib) < n:
            next_fib = list_fib[-1] + list_fib[-2] #negative indexing start from end of array
            list_fib.append(next_fib) #gett added inside list one by one 
        return list_fib
        

num_terms =int(input("Enter a value to get fibonannci series"))

fib_sequence = fibonancci_series(num_terms)
print(f"Fibonacci sequence up to {num_terms} terms (iterative): {fib_sequence}")

# so dude to get the respective psoiton of value or number there is new way 

def fibonacci_atPos(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        a,b = 0,1 
        for _ in range(2,n+1):
            next_fib = a+b
            a,b=b,next_fib
        return b 
        
    
position = int(input("Enter a value to get that respective index value dude"))

fib = fibonacci_atPos(position)

print(f"The Fibonacci number at position {position} is: {fib}")

    