import os
from Cliente import Cliente
from ContaPoupanca import ContaPoupanca

C_VERDE = '\033[92m'
C_AMARELO = '\033[93m'
C_VERMELHO = '\033[91m'
C_CIANO = '\033[96m'
C_BOLD = '\033[1m'
C_RESET = '\033[0m'

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    # Função menu
    limpar_tela()
    print("\n" + "="*20)
    print(f"{C_BOLD}{C_CIANO}   🏦 BANCO.PY 🏦{C_RESET}")
    print('='*20)
    print(f"{C_BOLD}[1]{C_RESET} 📥 Depósito")
    print(f"{C_BOLD}[2]{C_RESET} 📤 Saque")
    print(f"{C_BOLD}[3]{C_RESET} Extrato")
    print(f"{C_VERMELHO}[4]{C_RESET} 🔙 Sair")
    print("="*20)
    return input("Escolha uma opção: ")

# Variáveis iniciais do sistema
saldo = 0
extrato = ""
if __name__ == "__main__":
           
    titular = input(f"{C_AMARELO}>>>DIGITE O NOME DO TITULAR<<<{C_RESET}")
    cpf = input(f"{C_AMARELO}>>>DIGITE O SEU CPF<<<{C_RESET}")
    numero_conta = input(f"{C_AMARELO}>>>DIGITE O NOMERO DA CONTA<<<{C_RESET}")

    novo_cliente = Cliente(titular, cpf)

    nova_conta_poupanca = ContaPoupanca(numero_conta, novo_cliente)

    print(f"{novo_cliente}")
    print(f"{nova_conta_poupanca}")

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

    elif opcao == "4":
            limpar_tela()
            print("Obrigado por usar o Banco py. Até logo!")
            break

    else:
        print("Opção inválida! Por favor, tente novamente.")

    


