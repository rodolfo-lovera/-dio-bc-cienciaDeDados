print('Seja bem vindo ao Caixa Rápido.')
I = True
saldo = 1000.00
deposito = []
saque = []
s = 0

while (I == True):
    print("""
          =====================
          Selecione a operação Bancário
          [D]epósito
          [E]xtrato
          [S]aque
          [N]enhuma das anteriores
          =====================
          """)
    op = input("> ")    
    operacao = op.upper()
    
    if(operacao == 'D'):
        print("Operação selecionada: Depósito.")
        dep = float(input("informe a quantidade a ser depositada (Valor em R$): "))
        saldo +=  dep
        deposito.append(dep)
        input("Pressione Enter para retornar ao menu inicial ou CTRL+C para sair!")
    
    elif(operacao == 'E'):
        print("Operação selecionada: Extrato.")
        print(f"O valor do saldo é {saldo}.")
        print(f"Foram realizados {len(deposito)} depositos e {len(saque)} saques.")
        input("Pressione Enter para retornar ao menu inicial ou CTRL+C para sair!")
    
    elif(operacao == 'S'):
        print("Operação selecionada: Saque.")

        saq = float(input("Informe o valor a ser saado (Valor em R$: )"))
        
        if(s > 3):
            print("Quantidade máxima de saques permitida para hoje. Saque só amanhã!")

        else:
            if(saq <= 500):
                if(saq <= saldo):
                    s += 1
                    saldo -= saq
                    saque.append(saq)
                else:
                    print("Você não possui salso suficiente para realizar saque.")
            else:
                print("Valor é superior ao máximo permitido.")
                        
        input("Pressione Enter para retornar ao menu inicial ou CTRL+C para sair!")
    
    elif(operacao == 'N'):
        print("Nenhuma operação das anteriores.")
        break
    
    else:
        print("Valor informado não é uma operação deste terminal.")
        input("Pressione Enter para retornar ao menu inicial ou CTRL+C para sair!")

else:
    print("Encerrando programa. Volte sempre.")