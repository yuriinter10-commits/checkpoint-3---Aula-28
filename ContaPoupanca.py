from Conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)

    def render_juros(self):
        self._saldo = self._saldo * 1.01
        











