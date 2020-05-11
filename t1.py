from functools import reduce

cube = lambda x: x*x*x# complete the lambda function 
fibo = lambda n:reduce(lambda x,n:[x[1],x[0]+x[1]], range(n),[0,1])[0]

def fibonacci(n):
    return [fibo(i) for i in range(n)]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))