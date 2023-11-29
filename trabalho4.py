#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 14:01:38 2023

@author: brena
"""

from flask import Flask, jsonify, request


app = Flask(__name__)



def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n + 1:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n + 1]


@app.route('/')
@app.route('/index')

def index(): 
    return("TESTE PARA MANDAR UM POST FACT E FIB")
    

@app.route('/myapi', methods=['POST'])
def calculate():
    data = request.get_json(force=True)
    response = {}

    if 'fact' in data:
        try:
            number = int(data['fact'])
            if number < 0:
                return jsonify({'error': 'O número para fatorial deve ser maior ou igual a zero.'}), 400
            fact_result = factorial(number)
            response['factorial_result'] = fact_result
        except ValueError:
            return jsonify({'error': 'O valor fornecido para fatorial não é um número inteiro válido.'}), 400

    if 'fib' in data:
        try:
            number = int(data['fib'])
            if number < 0:
                return jsonify({'error': 'O número para Fibonacci deve ser maior ou igual a zero.'}), 400
            fib_result = fibonacci(number)
            response['fibonacci_sequence'] = fib_result
        except ValueError:
            return jsonify({'error': 'O valor fornecido para Fibonacci não é um número inteiro válido.'}), 400

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)