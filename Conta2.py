import datetime

class Conta:
    # Definição de cores para a estética
    VERDE = '\033[32m'
    VERMELHO = '\033[31m'
    AMARELO = '\033[33m'
    CIANO = '\033[36m'
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
            # Print personalizado em Verde
            print(f"{self.VERDE}✅ Depósito de R$ {valor:.2f} realizado!{self.RESET}")
            return True
        else:
            # Print personalizado em Vermelho
            print(f"{self.VERMELHO}❌ Erro: O valor do depósito deve ser positivo.{self.RESET}")
            return False

    def sacar(self, valor):
        if valor <= 0:
            print(f"{self.VERMELHO}❌ Erro: O valor do saque deve ser positivo.{self.RESET}")
            return False
        
        if valor <= self._saldo:
            self._saldo -= valor
            self._registrar_transacao("Saque", valor)
            print(f"{self.VERDE}✅ Saque de R$ {valor:.2f} realizado!{self.RESET}")
            return True
        else:
            print(f"{self.AMARELO}⚠️ Erro: Saldo insuficiente.{self.RESET}")
            return False

    def _registrar_transacao(self, tipo, valor):
        data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self._historico.append(f"[{data_hora}] {tipo}: R$ {valor:.2f}")

    def exibir_extrato(self):
        # Título em Ciano
        print(f"\n{self.CIANO}--- EXTRATO DETALHADO | Conta: {self.numero} ---{self.RESET}")
        print(f"Cliente: {self.cliente}")
        print("-" * 40)
        
        if not self._historico:
            print(f"{self.AMARELO}Sem movimentações recentes.{self.RESET}")
        else:
            for operacao in self._historico:
                print(operacao)
        
        print("-" * 40)
        # Saldo final em Ciano para destaque
        print(f"{self.CIANO}Saldo Atual: R$ {self._saldo:.2f}{self.RESET}")
        print("=" * 40)