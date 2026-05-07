import os
import time
import datetime

class Conta:
    # Cores para a estética
    VERDE = '\033[32m'
    VERMELHO = '\033[31m'
    AMARELO = '\033[33m'
    CIANO = '\033[36m'
    NEGRITO = '\033[1m'
    RESET = '\033[0m'

    def __init__(self, numero, cliente):
        self._saldo = 0.0
        self.numero = numero
        self.cliente = cliente
        self._historico = []

    def get_saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._registrar_transacao("Depósito", valor)
            print(f"{self.VERDE}✅ Depósito de R$ {valor:.2f} realizado!{self.RESET}")
            return True
        print(f"{self.VERMELHO}❌ Valor inválido!{self.RESET}")
        return False

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            self._registrar_transacao("Saque", valor)
            print(f"{self.VERDE}✅ Saque de R$ {valor:.2f} realizado!{self.RESET}")
            return True
        print(f"{self.VERMELHO}❌ Saldo insuficiente ou valor inválido!{self.RESET}")
        return False

    def _registrar_transacao(self, tipo, valor):
        data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        cor = self.VERDE if tipo == "Depósito" else self.VERMELHO
        self._historico.append(f"{cor}[{data_hora}] {tipo}: R$ {valor:.2f}{self.RESET}")

    def exibir_extrato(self):
        print(f"\n{self.CIANO}--- EXTRATO DETALHADO ---{self.RESET}")
        if not self._historico:
            print(f"{self.AMARELO}Sem movimentações.{self.RESET}")
        else:
            for op in self._historico: print(op)
        print(f"{self.CIANO}{'-'*30}{self.RESET}")
        print(f"Saldo Total: {self.VERDE}R$ {self._saldo:.2f}{self.RESET}")

# --- FUNÇÕES DE INTERFACE ---
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print(f"\n{Conta.CIANO}{'='*30}{Conta.RESET}")
    print(f"{Conta.CIANO}{Conta.NEGRITO}       🏦 BANCO PY v3.0{Conta.RESET}")
    print(f"{Conta.CIANO}{'='*30}{Conta.RESET}")
    print(f"{Conta.AMARELO}[1]{Conta.RESET} Depósito")
    print(f"{Conta.AMARELO}[2]{Conta.RESET} Saque")
    print(f"{Conta.AMARELO}[3]{Conta.RESET} Extrato")
    print(f"{Conta.AMARELO}[4]{Conta.RESET} Ver Saldo")
    print(f"{Conta.VERMELHO}[0]{Conta.RESET} Sair")
    print(f"{Conta.CIANO}{'='*30}{Conta.RESET}")
    return input(f"{Conta.NEGRITO}Escolha uma opção: {Conta.RESET}")

# --- EXECUÇÃO DO SISTEMA ---


limpar_tela()
print(f"{Conta.CIANO}--- CADASTRO INICIAL ---{Conta.RESET}")
nome = input("Nome do Cliente: ")
numero_conta = input("Número da Conta: ")

minha_conta = Conta(numero_conta, nome)

# 2. LOOP DE INTERAÇÃO
while True:
    opcao = mostrar_menu()

    if opcao == "1":
        limpar_tela()
        v = float(input("Valor do depósito: R$ "))
        minha_conta.depositar(v)
        input(f"\n{Conta.AMARELO}Pressione Enter...{Conta.RESET}")

    elif opcao == "2":
        limpar_tela()
        v = float(input("Valor do saque: R$ "))
        minha_conta.sacar(v)
        input(f"\n{Conta.AMARELO}Pressione Enter...{Conta.RESET}")

    elif opcao == "3":
        limpar_tela()
        minha_conta.exibir_extrato()
        input(f"\n{Conta.AMARELO}Pressione Enter...{Conta.RESET}")

    elif opcao == "4":
        limpar_tela()
        print(f"\n{Conta.CIANO}--- CONSULTA DE SALDO ---{Conta.RESET}")
        print(f"Olá {Conta.NEGRITO}{minha_conta.cliente}{Conta.RESET},")
        print(f"Seu saldo disponível é: {Conta.VERDE}R$ {minha_conta.get_saldo():.2f}{Conta.RESET}")
        input(f"\n{Conta.AMARELO}Pressione Enter...{Conta.RESET}")

    elif opcao == "0":
        print(f"\n{Conta.VERDE}Obrigado por usar o Banco PY, {minha_conta.cliente}!{Conta.RESET}")
        time.sleep(1.5)
        break

    else:
        print(f"{Conta.VERMELHO}Opção inválida!{Conta.RESET}")
        time.sleep(1)