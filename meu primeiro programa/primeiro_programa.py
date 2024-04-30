menu = """

[1] Depositar  
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 1000
limite = 500
extrato = 0
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do Depósito:"))
        if valor > 0:
            saldo += float(valor)
            extrato == f"Depósito: R${valor:.2f}\n" 
        else:
            print("Operação falhou! O valor informado é invalido.")
            
    elif opcao == "2":
        valor = float(input("Informe o valor do Saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Voçê não tem saldo suficiente.")
            
        if excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        if excedeu_saque:
            print("Operação falhou! Número máximo de saques excedido.")  

        elif valor > 0:
            saldo -= valor
            extrato == f"saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é invalido.")

    elif opcao == "3":
        print("\n*************** EXTRATO ***************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:2f}")
        print("***************************************************************")
        
    elif opcao == "0":
        break
    
    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")
    
    