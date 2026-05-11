import os
import time

# Cores para o terminal
C_VERDE = '\033[92m'
C_AMARELO = '\033[93m'
C_VERMELHO = '\033[91m'
C_CIANO = '\033[96m'
C_BOLD = '\033[1m'
C_RESET = '\033[0m'

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho():
    print(f"{C_AMARELO}{'='*40}{C_RESET}")
    print(f"{C_BOLD}{C_CIANO}       🏦 LA CASA DE PAPEL 🏦{C_RESET}")
    print(f"{C_AMARELO}{'='*40}{C_RESET}")

def menu():
    limpar_tela()
    cabecalho()
    print(f"{C_BOLD}[1]{C_RESET} 📥 Depósito")
    print(f"{C_BOLD}[2]{C_RESET} 📤 Saque")
    print(f"{C_BOLD}[3]{C_RESET} 📜 Extrato")
    print(f"{C_BOLD}[4]{C_RESET} ❌ Sair")
    print(f"{C_AMARELO}{'-'*40}{C_RESET}")
    return input(f"{C_BOLD}Escolha uma opção: {C_RESET}")

def mensagem_sucesso(texto):
    print(f"\n{C_VERDE}✔ {texto}{C_RESET}")
    time.sleep(1.5)

def mensagem_erro(texto):
    print(f"\n{C_VERMELHO}✘ {texto}{C_RESET}")
    input(f"\n{C_AMARELO}Pressione Enter para voltar...{C_RESET}")

# --- Início do Programa ---
limpar_tela()
cabecalho()
print(f"{C_CIANO}>>> CADASTRO INICIAL <<<{C_RESET}\n")
titular = input("Nome do titular: ")
cpf = input("CPF: ")
numero_conta = input("Número da conta: ")

novo_cliente = Cliente(titular, cpf)
nova_conta_poupanca = ContaPoupanca(numero_conta, novo_cliente)

saldo = 0
extrato = ""

while True:
    opcao = menu()

    if opcao == "1":
        limpar_tela()
        cabecalho()
        print(f"{C_BOLD}>>> DEPÓSITO <<<{C_RESET}\n")
        try:
            valor = float(input("Valor do depósito: R$ "))
            if valor > 0:
                saldo += valor
                extrato += f"{C_VERDE}(+) Depósito: R$ {valor:.2f}{C_RESET}\n"
                mensagem_sucesso("Depósito realizado!")
            else:
                mensagem_erro("Valor inválido!")
        except ValueError:
            mensagem_erro("Entrada inválida! Digite apenas números.")

    elif opcao == "2":
        limpar_tela()
        cabecalho()
        print(f"{C_BOLD}>>> SAQUE <<<{C_RESET}\n")
        try:
            valor = float(input("Valor do saque: R$ "))
            if valor > saldo:
                mensagem_erro("Saldo insuficiente!")
            elif valor > 0:
                saldo -= valor
                extrato += f"{C_VERMELHO}(-) Saque:    R$ {valor:.2f}{C_RESET}\n"
                mensagem_sucesso("Saque realizado!")
            else:
                mensagem_erro("Valor inválido!")
        except ValueError:
            mensagem_erro("Entrada inválida!")

    elif opcao == "3":
        limpar_tela()
        cabecalho()
        print(f"{C_BOLD}📜 EXTRATO DETALHADO{C_RESET}")
        print(f"{C_CIANO}{novo_cliente}{C_RESET}")
        print(f"{C_CIANO}{nova_conta_poupanca}{C_RESET}")
        print(f"{C_AMARELO}{'-'*40}{C_RESET}")
        
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
            
        print(f"{C_AMARELO}{'-'*40}{C_RESET}")
        print(f"{C_BOLD}SALDO ATUAL: {C_VERDE}R$ {saldo:.2f}{C_RESET}")
        print(f"{C_AMARELO}{'='*40}{C_RESET}")
        input(f"\n{C_AMARELO}Pressione Enter para voltar ao menu...{C_RESET}")

    elif opcao == "4":
        limpar_tela()
        print(f"\n{C_CIANO}Obrigado por usar o Banco py. Até logo! 👋{C_RESET}\n")
        break

    else:
        mensagem_erro("Opção inválida!")
