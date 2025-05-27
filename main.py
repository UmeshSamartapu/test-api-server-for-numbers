from fastapi import FastAPI
from typing import List
import random

app = FastAPI(title="Test Server APIs")


def generate_primes(n: int = 5) -> List[int]:
    primes = []
    num = 2
    while len(primes) < n:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes

def generate_fibonacci(n: int = 5) -> List[int]:
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

def generate_even(n: int = 5) -> List[int]:
    return [i * 2 for i in range(n)]

def generate_random(n: int = 5) -> List[int]:
    return random.sample(range(1, 100), n)

@app.get("/")
def root():
    return {"message": "Welcome to the Test Server APIs"}

@app.get("/primes")
def primes():
    return {"numbers": generate_primes()}

@app.get("/fibonacci")
def fibonacci():
    return {"numbers": generate_fibonacci()}

@app.get("/even")
def even():
    return {"numbers": generate_even()}

@app.get("/random")
def random_numbers():
    return {"numbers": generate_random()}
