'''

 depósito,
    apenas valores positivos

saque
    max 3 saques por dia
    sauqe maximo diario R$ 500
    nao sao mais do q conta tem

extrato.


'''
import os

menu = """
    Banco 

    [S]aque - Levantar dinheiro
    [D]epoisito - Depositar dinheiro
    [E]xtrato - Extrato da conta
    [Q]uit - Sair
"""

extrato = """
Extrato da conta\n
"""

saldo = 1000
total_saques = 0

SAQUE_MAX = 500
MAX_SAQUES = 1

extrato += f"saldo inicial -> {saldo: .2f}\n"

while True:

    print(menu)

    op = input("Selecione a opção desejada: ")

    match op.lower():

        case 's':
            os.system("cls | clear")
            valor = input("\tValor a sacar? \n\t")

            if int(valor) > SAQUE_MAX:
                 print(f"o saque maximo é de R$ {SAQUE_MAX}")

            elif saldo < int(valor):
                print("Valor insuficiente")

            elif total_saques >= MAX_SAQUES:
                print("Ja faz todo os sques premitos num dia")

            else:
                total_saques += 1
                saldo -= int(valor)

                print("\tSaque feito")
                print(f"\tsaldo atual R$ {saldo:.2f}")


                extrato += f"saque R$ {int(valor):.2f}\n"
                extrato += f"saldo atual R$ {saldo:.2f}\n"



            input("presione uma tecla para continua")
        case 'd':
            valor = input("\tValor a depositar? \n\t")

            if valor.isnumeric():
                saldo += int(valor)

                extrato += f"deposito R$ {int(valor):.2f}\n"
                extrato += f"saldo atual R$ {saldo:.2f}\n"

                print("\tvalor depositado")
                print(f"\tsaldo atual R$ {saldo:.2f}")


            else:
                print("o valor deve ser numerico")


        case 'e':
            os.system("cls | clear")
            print("inicio do estrato".center(25, "-"))
            print(extrato)

            print("fim do estrato".center(25, "-"))

            input("presione uma tecla para continua")
        case 'q':
            exit(0)
        case _:
            print("opeção invalida tente de novo")
            input("presione uma tecla para continua")

    os.system("cls | clear")
