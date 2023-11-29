# API Flask - Calculadora de Fatorial e Sequência de Fibonacci

Esta é uma API simples construída com Flask que calcula o fatorial de um número e a sequência de Fibonacci para outro número para a disciplina de desenvolvimento de software livre.

## Funcionalidades

- Calcula o fatorial de um número inteiro não negativo.
- Gera a sequência de Fibonacci para um número inteiro não negativo.

## Uso

- Envia uma solicitação POST para `/myapi` com um JSON contendo os campos `fact` e `fib` para calcular o fatorial e a sequência de Fibonacci, respectivamente.
  Exemplo:
  ```json
  {
    "fact": 5,
    "fib": 6
  }
