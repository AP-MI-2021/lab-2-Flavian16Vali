'''
-Găsește ultimul număr prim mai mic decât un număr dat, dar doar pentru n mai mare strict decat 2
-Input:
    n,ok numere naturale
-Output:
    cel mai mare numar prim strict mai mic decat n

'''
def get_largest_prime_below(n):
    ok=1
    while ok>0:
        n-=1
        nr=0
        for i in range(1,n+1):
            if n%i==0:nr+=1
        if nr==2:ok=0
    return n
def test_get_largest_prime_below():
    assert get_largest_prime_below(10)==7
    assert get_largest_prime_below(105)==103
    assert get_largest_prime_below(3)==2
'''
-Determină dacă un număr dat este palindrom.
-Input:
    n numar natural
-Output:
    bool: True daca n este palindrom, respectiv False daca n nu este palindrom
'''
def is_palindrome(n):
    og=0
    a=n
    while a!=0:
        og=og*10+a%10
        a=a//10
    if(og==n): return True
    else: return False

def test_is_palindrome():
    assert is_palindrome(101)==True
    assert is_palindrome(100)==False
    assert is_palindrome(19)==False

'''
-Afișează toți anii bisecți între doi ani dați (inclusiv anii dați).
-Input:
    anii care reprezinta inceputul si sfarsitul intervalului, numere naturale intregi
-Outpu:
    anii bisecti returnati intr-o lista
'''
def get_leap_years(start: int, end: int):
    lst=[]
    for i in range(start+1,end):
        if (i%4==0 and i%100!=0) or i%400==0: lst.append(i)

    return lst
def test_get_leap_years():
    assert get_leap_years(2002,2016)==[2004, 2008, 2012]
    assert get_leap_years(2000,2004)==[]
    assert get_leap_years(2003,2005)==[2004]
'''
-Transformă un număr dat din baza 10 în baza 2. Numărul se dă în baza 10.
-Input:
    n numar natural
-Otput:
    reprezentarea in baza 2 a numarului n
'''
def get_base_2(n: str):
    lst=[]
    while n!=0:
        a=n%2
        lst.append(a)
        n=n//2
    lst.reverse()
    return lst
def test_get_base_2():
    assert get_base_2(75)==[1, 0, 0, 1, 0, 1, 1]
    assert get_base_2(123)==[1, 1, 1, 1, 0, 1, 1]
    assert get_base_2(1)==[1]

def main():
    print(get_leap_years(1999,2018))
if __name__ == '__main__':
    main()