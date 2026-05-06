import os
import time.sleep
from Cliente import Cliente

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    # Estilização básica do menu
    limpar_tela()
    print("\n" + "="*20)
    print(">>>>> Banco py <<<<<")
    print("="*20)
    print("[1] Depósito")
    print("[2] Saque")
    print("[3] Extrato")
    print("[0] Sair")
    print("="*20)
    return input("Escolha uma opção: ")

# Variáveis iniciais do sistema
saldo = 0
extrato = ""


while True:
    opcao = menu()

    if opcao == "1":
        limpar_tela()
        valor = float(input("Digite o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! Valor inválido.")
        input(f"\nPressione Enter para voltar ao menu...")

    elif opcao == "2":
        limpar_tela()
        valor = float(input("Digite o valor do saque: R$ "))
        if valor > saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! Valor inválido.")
        input(f"\nPressione Enter para voltar ao menu...")
   
    elif opcao == "3":
        limpar_tela()
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=============================")
        input(f"\nPressione Enter para voltar ao menu...")
    
    elif opcao == "0":
        limpar_tela()
        print("Obrigado por usar o Banco py. Até logo!")
        break

    else:
        print("Opção inválida! Por favor, tente novamente.")
