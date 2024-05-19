#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name= "Naureen"):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default()
greet_with_default("sunny")


def add(num1, num2):
    return(num1 + num2)

results= add(1, 2)
print(results)

def test_halve_int(self):
    '''halves integer input'''
    assert(halve(100) == 50)

