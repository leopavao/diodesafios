menu = '''
========== Menu ===========

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

======== Obrigado ========
'''

saldo = 2000
limite = 500
extrato = list()
numero_saques = 0
limite_saques = 3

opcao = input(menu)

while True:

    if opcao == "1":
        print("Opção escolhida: Depósito")
        deposito = int(input("Qual valor deseja depositar?"))
        saldo += deposito
        extrato.append(f"+ R$ {deposito:.2f}")
        print(f"Seu novo saldo é: R$ {saldo:.2f}")

    elif opcao == "2":
        print("Opção escolhida: Saque")
        saque = int(input("Qual o valor você deseja sacar?"))
        
        if ((saque <= saldo) and (saque <= limite) and (numero_saques < limite_saques)):
            saldo -= saque
            numero_saques += 1
            extrato.append(f"- R$ {saque:.2f}")
            print("Saque realizado com sucesso.")
            print(f"Seu novo saldo é de: R$ {saldo:.2f} e seu limite de saques diários é: {limite_saques - numero_saques}")
        
        elif saque > limite:
            print(f"Valor limite de saque excedido. O limite para saques é de R$: {limite:.2f}")
    
        elif saque > saldo:
            print(f"Saldo indisponível. Seu saldo é de: R$ {saldo:.2f}") 

        elif numero_saques >= limite_saques:
            print("Número de saques diário excedido.")
            break

    elif opcao == "3":
        print("Opção escolhida: Extrato.")
        print("Seu extrato atual é:")
        for transacao in extrato:
            print(transacao)
        print(f"Seu saldo atual é de: R$ {saldo:.2f}")

    elif opcao == "0":
        print("Obrigado por utilizar nosso serviço.")
        break    

    else:
        print("Selecione uma opção valida.")

    # exibe o menu inicial:
    opcao = input(menu)