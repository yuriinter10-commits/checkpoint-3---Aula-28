import json
import uuid

class Conta:
    def __init__(self, numero, cliente):
            self._saldo = 0.0
            self.numero = numero
            self.cliente = cliente
  
    def get_saldo(self):
        return self._saldo
    
    # Método para Depositar: Altera o saldo se o valor for positivo
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            return True
        else:
            print("Erro: O valor do depósito deve ser positivo.")
            return False

    # Método para Sacar: Altera o saldo se houver fundos suficientes
    def sacar(self, valor):
        if valor <= 0:
            print("Erro: O valor do saque deve ser positivo.")
            return False
        
        if valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            return True
        else:
            print("Erro: Saldo insuficiente para realizar o saque.")
            return False
           
