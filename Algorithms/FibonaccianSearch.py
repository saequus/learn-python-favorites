def fibonaccianSearch(arr, x, n): 
    fib1 = 0
    fib2 = 1 
    fibM = fib1 + fib2 

    while (fibM < n): 
        fib1 = fib2 
        fib2 = fibM 
        fibM = fib1 + fib2 

    offset = -1
    while fibM > 1: 
        i = min(offset+fib1, n-1) 
 
        if arr[i] < x: 
            fibM = fib2 
            fib2 = fib1 
            fib1 = fibM - fib2 
            offset = i 
        elif arr[i] > x: 
            fibM = fib1 
            fib2 = fib2 - fib1 
            fib1 = fibM - fib2 
        else:
            return i 
    if (fib2 and arr[offset+1] == x): 
        return offset+1;
    return -1


a = [3, 5, 12, 44, 192, 233, 256, 322, 456, 499, 554, 604, 679, 844]
print(fibonaccianSearch(a, 192, len(a)))



