menu = """ 
    [d] - Depósito
    [s] - Saque
    [e] - Extrato
    [s] - Sair
    >>>
"""

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'

        else:
            print("Operação falhou ! O valor informado é inválido.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar."))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_de_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print('Operção falhou! Você não tem saldo suficiente pra realizar essa operação.')
        
        elif excedeu_limite:
            print('Operação fallhou! O valor do saque excedeu o limite.')

        elif excedeu_saques:
            print('Operação falhou! Vocâ atingiu o número máximod e saques por dia.')
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1
        
        else:
            print('Operação falhou! o valor informado é inválido.')

    elif opcao == "e":
        print("\n*********************EXTRATO*********************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("*************************************************")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione  novamente a operação desejada.")