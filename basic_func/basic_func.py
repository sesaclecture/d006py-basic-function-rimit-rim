import math
import numpy as np

def add(a, b):
    result = a + b
    return result

def sub(a, b):
    result = a - b
    return result


def mul(a, b):
    result = a * b
    return result


def div(a, b):
    result = a / b
    return result


def power(base, pow):
    result = base ** pow
    return result


def square(base):
    return base * base


def greet(이름="낯선자", 나이=20):
    인사 = ""
    if (나이 >= 40):
        인사 = "안녕하십니까"
    elif (나이 >= 20):
        인사 = "안녕하신가"
    else:
        인사 = "안녕"
    return 인사 + f" {이름}!"
