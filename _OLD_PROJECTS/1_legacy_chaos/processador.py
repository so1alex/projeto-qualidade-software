import os, sys
from datetime import datetime

# Classe que faz tudo: Dados, Calculo, Banco de Dados e Email
class sistema:
    def __init__(self, items):
        self.items=items # Lista de dicionarios

    def calc(self):
        t=0
        for i in self.items:
            # Logica confusa e hardcoded
            if i['tipo']=='extra': t+=i['val']*1.1
            else: t+=i['val']
        return t

    def processar(self):
        # Mistura logica de negocio com "IO" (Prints)
        total = self.calc()
        print(f"O total e: {total}")
        if total > 100:
            print("Enviando email para gerente...")
        else:
            print("Pedido pequeno, sem aviso.")
        
        # Salva em arquivo (simulando DB)
        with open('db.txt','a') as f:
            f.write(str(datetime.now()) + str(total))

x = [{'item':'livro','val':50, 'tipo':'normal'}, {'item':'mouse','val':60,'tipo':'extra'}]
s = sistema(x)
s.processar()