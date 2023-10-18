
def print_N_decrescente(n):
    if n == 5:
        print (n)
    else:
        print (n)
        print_N_crescenteIterativo(n-1)
    
    
    


def print_N_crescenteIterativo(n):
   

def print_N_crescente(inicio, fim): # (1,1) = 1 ; (1,10)=1,2,3,4,5,6,7,8,9,10
   


def sequencia_crescente(x): # de 1 ate x
    if x == 1:
        print(x)
    else:
        sequencia_crescente(x-1)
        print(x)
        


def fat(n):
    


def fib(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fib(n-1) + fib(n-2)

def serie(n): # S=1 + 1/1! + 1/2! + 1/3! + ... + 1/n!
    

def potencia(x,y): # x >0 e y>=0
    


if __name__ == '__main__':

    print_N_decrescente(10)
    print('\n\n')
    sequencia_crescente(10)
    print('\nfatorial\n')
    print('fat(3) = {}'.format(fat(3))) # fat(3)=3*fat(3-1)=6
    print('fib(5)= {}'.format(fib(5)))
    print('serie(3)={}'.format(serie(3)))
    print('2^3 = potencia(2,3)={}'.format(potencia(2,3)))