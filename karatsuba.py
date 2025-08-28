def karatsuba(x: int, y: int) -> int: #1

    if x < 10 or y < 10: #2
        return x * y #3

    n = max(len(str(x)), len(str(y))) #4
    m = n // 2 #5

    alto_x, baixo_x = divmod(x, 10**m) #6
    alto_y, baixo_y = divmod(y, 10**m) #7

    a0 = karatsuba(baixo_x, baixo_y) #8
    a1 = karatsuba(baixo_x + alto_x , baixo_y + alto_y) #9
    a2 = karatsuba(alto_x, alto_y) #10

    return (a2 * 10**(2*m)) + ((a1 - a2 - a0) * 10**m) + a0 #11