"""
This project will allow for high accurracy calculation in python3, this is done by using binary.
This also means that you can add this quite simply into hardware which can increase the speed very much
-the only reason im using python3 is because i dont need the speed right now and im working on it so that you can quite easily change the proggraming languages for your needs-


the thing i want is that when division occurs the bytes that are not specifically allocated but a dynamic allocation.
This means that how big the number is that is how many bits are allocated. This of course has no real world application except from extremely specific
because, without byte allocation it can cause many problems with existing languages that do use allocation.

TODO:
Addition v
Subtraction v
Division v
multiplication v
add floating binary digits # i think i will have to stop using 0b because it automatically reduces the binary which is annoying
add functions for GET, SET, FIND, UPDATE, CLEAR v

"""
#AND &
#OR |
#XOR ^
#NOT ~-
#MOVE LEFT << num +
#MOVE RIGHT >> num -
#FIND nth bit (X >> 0) & 1
#UPDATE mask = ~-(1 << i), (n & mask) | (val << i)
#CLEAR mask = ~-(1 << i), n & mask


import os;os.system("clear")
num1 = 0b1001
num2 = 0b1001
digits_rule = 32
#functions for GET, SET, FIND, UPDATE, CLEAR
def GET(A, nth):
    return (A & (1 << nth)) != 0
def SET(A, nth):
    return A | (1 << nth)
def FIND(A, nth):
    return ((A >> 0) & nth)
def UPDATE(A, val,nth):
    mask = ~-(1 << nth)
    return ((A & mask) | (val << nth))
def CLEAR(A, nth):
    mask = ~-(1 << nth)
    return A & mask
#bitwise binary movement
#Addition binary
def half_adder(A,B): #use of this is deprecated
    S = A ^ B
    C = A & B
    return C,S
def full_adder(A,B,Cin):
    S = Cin^(A ^B)
    Cout = (A & B) | (Cin & A^B)
    return S, Cout
def four_bit_adder(A,B,C):
    out = 0
    S,C = full_adder((A >> 0) & 1,(B >> 0) & 1,C)
    out = out | S << 0

    S,C = full_adder((A >> 1) & 1,(B >> 1) & 1,C)
    out = out | S << 1

    S,C = full_adder((A >> 2) & 1,(B >> 2) & 1,C)
    out = out | S << 2

    S,C = full_adder((A >> 3) & 1,(B >> 3) & 1,C)
    out = out | S << 3

    out = out | C << 4

    return out
def nth_bit_adder(n,A,B,C): #do not use this, its just for show.
    out = 0
    for i in range(n+1):
        S,C = full_adder((A >> i) & 1,(B >> i) & 1,C)
        out = out | S << i
    out = out | C << n
    return out
def bit_Addition(A,B):
    while B > 0:
            tmp = B
            B =  (A & B) << 1
            A = A^tmp
    return A
#subtract
def bit_subtract(A,B): #first number has to be bigger
    while B > 0:
        borrow = (~A) & B
        A = A ^ B
        B = borrow << 1
    return A
#multiplication
def bit_multiplication(A,B):
    reg = 0
    while (B != 0):
        if (B & 1):
            reg += A
        A <<= 1
        B >>= 1
    return reg
#division
def bit_division(A,B):
    ans = 0
    neg = A < 0 or B < 0
    A = abs(A)
    B = abs(B)
    for i in range(digits_rule - 1,-1,-1):
        if(B << i <= A):
            A -= B << i
            ans += 1 << i
    return ans if neg == 0 else -1 * ans
#floating number theory
def floating_num1(A):
    #neg = GET(A, len(1 - int(bin(A))))
    print(  str(bin(A))[2:] )
    #print(GET(A, len(A))   )
"""
TODO:
Ideas for floating point numbers, im thinking of creating a 2 types floating numbers:
1 being the whole number being only 1 so it can be represented by 4 binary digits, this way the main division can be used for the high precision for the digits.
2 with 2 parts being in 4 times being less. (52 / 11)

The reason im doing this because it lets me have high precision with division and other more comlicated binary movement
"""
#output to debug
num3 = 0b100000000000000000000000000011111100
floating_num1(num3)
def form(bit, name, binary_used, nor_output):
    print("0b{0:b} {1} {2} {3}".format(bit, str(name).rjust( 10-len(str("{0:b}".format(bit))) ), binary_used, nor_output))

print(num1,num2)
form(bit_Addition(num1,num2), "add", (num1, num2), bit_Addition(num1,num2))
