'''

 depósito,
    apenas valores positivos

saque
    max 3 saques por dia
    sauqe maximo diario R$ 500
    nao sao mais do q conta tem

extrato.


'''


menu = """
    Banco 

    [S]aque - Levantar dinheiro
    [D]epoisito - Depositar dinheiro
    [E]xtrato - Extrato da conta
    [Q]uit - Sair
"""

print(menu)


saldo_inicial = 1000
total_saques = 0

SAQUE_MAX = 500
MAX_SAQUES = 3


while True:

    op = input("\tSelecione a opção desejada: ")

    match op.lower():

        case 's':
            print("saque")
        case 'd':
            print("depoisito")
        case 'e':
            print("Extrato")
        case 'q':
            exit(0)
        case _:
            print("\topeção invalida tente de novo")