# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# CREATING A BANK SYSTEM WITH PYTHON
# Code Challenge - "D"igital "I"novation "O"ne
# Level: Medium
# =================================================================================================================================================================================================

# =======================================
# THE DB'S                             ||
# =================================================================================================================================================================================================

db_username = {

}

db_accounts = {

}

db_passwords = {

}

db_transactions = {

}

def __db_users__(cpf, name_cli, birth_day, born_city, country):
    login = [cpf]
    data_inclusão = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    nome_cliente = [name_cli]
    data_nascimento = [birth_day]
    cidade_nascimento = [born_city]
    pais_nascimento = [country]
    status = ["A"]
    dt_inatividade = ['00/00/0000 00:00:00']

def __db_users_accounts__():
    login = []
    data_inclusão = []
    agencia = []
    nmr_conta = []
    password = []
    balance = []

def __db_users_passwords__():
    data_inclusão = []
    login = []
    password = []
    status = []

def __db_transaction__():
    data_inclusão = []
    login = []
    agencia = []
    nmr_conta = []
    tp_transaction = []
    value = []

# =======================================
# THE VARIABLES AND CONSTANTS          ||
# =================================================================================================================================================================================================
ballance = 0
statement = []
withdraw = 0
WITHDRAW_VALUE_LIMIT = 500
WITHDRAW_LIMIT = 3

# Th&_Ad4m@nThy$ THINGS ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
WIDTH_PROGRAM = 147
BANK_NAME = 'TH&_AD@M4NTHY$ BANK SYSTEM'

# =======================================
# THE LIBRARIES                        ||
# =================================================================================================================================================================================================

import datetime as dt
import os

# =======================================
# THE FUNCTIONS                        ||
# =================================================================================================================================================================================================

def clear_terminal():
    os.system("cls")

def layout_initline(WIDTH_PROGRAM):
    print(f"{'#' * WIDTH_PROGRAM}")

def layout_mainline(WIDTH_PROGRAM):
    print(f"{'-' * WIDTH_PROGRAM}")

def menu_header(menu_name):
    print( f'{menu_name.center(WIDTH_PROGRAM, " ")}\n\n' )

def initialization(BANK_NAME):
    layout_initline(WIDTH_PROGRAM)
    print(f"{BANK_NAME.center(WIDTH_PROGRAM, ' ')}")
    layout_mainline(WIDTH_PROGRAM)

def menu_body(mensage_to_show, menu_name):
    print(f'{mensage_to_show.left(WIDTH_PROGRAM, " ")}')
    print( f'{menu_name.center(WIDTH_PROGRAM, " ")}\n\n' )

def error_menu(error_code):
    menu_header('ERROR')
    db_errors = { 
        '01' : 'Numeric chars only', 
        '02' : 'Invalid option. Try again.', 
        '03' : 'Minimum 8 chars not reached', 
        '04' : 'Maximum 14 chars extrapolated.', 
        '05' : 'CPF/CNPJ not find.' 
    }
    print(db_errors[error_code])
    db_errors = None

def confirmation():
    while True:
        confirmat = input(f'[1]\tYes\n[2]\tNo\n[0]\tExit\n\n>>>>>>> ')
        if confirmat not in list( '012' ):
            error_menu( '02' )
        else:
            return confirmat

def continue_program():
    continue_program = None
    while continue_program != '0':
        menu_header('CONTINUE?')
        continue_program = input(f'Press [0]\n\n>>>>>>> ')
        if continue_program != '0':
            error_menu('02')

def char_lenght(check_chars):
    if len(check_chars) < 8:
        error_menu('03')
    elif len(check_chars) > 14:
        error_menu('04')
    else:
        return True
    return False

def allowed_keys(check_chars):
    for char in list(check_chars):
        if char not in list('0123456789'):
            error_menu('01')
            return False
    return True

def chars_validation_protocol(char_to_check):
    validation = allowed_keys(char_to_check)
    if validation == True:
        validation = char_lenght(char_to_check)
        if validation == True:
            return True
    return False

def __new_user__(login):
    print(f'\nDo you wanna create a new user?\n')
    confirmat = confirmation()
    if confirmat == '1':
        cpf = login
        name_cli = input("What's your name")
        birth_day = input('Birthday date >>>>>>> ')
        born_city = input('City where are you born >>>>>>> ')
        country = input('Country where are you born >>>>>>> ')
        password = input('Password >>>>>>> ')
        print(f'Do you wanna create user {login}?')
        confirmat = confirmation()
        if confirmat == '1':
            __db_user__(cpf, name_cli, birth_day, born_city, country)
            db_users['DT_INC'] = db_users['DT_INC'].append(dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            db_users['CPF/CNPJ'] = db_users['CPF/CNPJ'].append(cpf)
            db_users['NM_CLI'] = db_users['NM_CLI'].append(name_cli)
            db_users['DT_NASC'] = db_users['DT_NASC'].append(birth_day)
            db_users['CID_NASC'] = db_users['CID_NASC'].append(born_city)
            db_users['PAIS_NASC'] = db_users['PAIS_NASC'].append(country)
            db_users['STS'] = db_users['STS'].append(dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            db_users_passwords['DT_INC'] = db_users_passwords['DT_INC'].append(dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            db_users_passwords['CPF/CNPJ'] = db_users_passwords['CPF/CNPJ'].append(cpf)
            db_users_passwords['PSSWRD'] = db_users_passwords['PSSWRD'].append(password)
            db_users_passwords['STS'] = db_users_passwords['STS'].append("A")
            print(db_users)
            print(db_users_passwords)
        elif confirmat == '2':
            print('Teste')
        else:
            print('Teste')
    elif confirmat == '2':
        return True
    else:
        return None

def login():
    login_switch = True
    while login_switch == True:
        menu_header( 'LOGIN' )
        login = input( 'Put your CPF/CNPJ ([0] Exit) :\n\n>>>>>>> ' )
        if login != '0':
            keys_validation = chars_validation_protocol(login)
            if keys_validation == True:
                # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
                if login in db_users['CPF/CNPJ']:
                    print('Caso encontre o CPF/CNPJ, rodar a função senha')
                else:
                    error_menu( '05' )
                    user = new_user(login)
                    if user == None:
                        login_switch = False
                    
                # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
        else:
            login_switch = False

# def main():
#     print('-' * WIDTH_PROGRAM)
#     menu_name('MAIN MENU')
#     print('-' * WIDTH_PROGRAM)
#     opcao = input(f"""
#     [1]\tDeposit ;
#     [2]\tWithdraw ;
#     [3]\tStatement ;
#     [0]\tExit

#     >>>>>>> """)

#     if opcao == "1":
#         print('Call Deposit')
#     elif opcao == "2":
#         print('Call Withdraw')
#     elif opcao == "3":
#         print('Call Statement')
#     elif opcao == "4":
#         print('Call Exit')
#     else:
#         print('Call Erro')
    

# def exit_menu():
#     exit_msg = f"""{'EXIT'.center(WIDTH_PROGRA2, ' ').center(WIDTH_PROGRAM, AUX)}
#     Do you really want to exit?

#     [1]\tYes
#     [2]\tNo 

#     >>>>>>> """
#     return input(exit_msg)

# def deposit(saldo, valor):
#     print('Calma, fio')

# statement_msg = f'TRANSACTION\t\t|\tVALUE'

# #######################################################################################################################################################
# =======================================
# __MAIN__                             ||
#========================================================================================================================================================
line_show(AUX, WIDTH_PROGRAM)
print(f"{BANK_NAME.center(WIDTH_PROGRAM, ' ')}")
line_show(AUX, WIDTH_PROGRAM)
login()
menu_header('THANK YOU')
line_show(AUX, WIDTH_PROGRAM)



# main()
# main_menu_switch = True
# while main_menu_switch == True:
#     opcao = input(main())
#     if opcao == "1":
#         print("Escolhido deposito")

        # print(f"""{'#'.center(WIDTH_PROGRAM, '#')}\n{'DEPOSIT'.center(WIDTH_PROGRAM / 2, ' ').center(WIDTH_PROGRAM, '#')}\n""")
        # deposit_switch = True
        # while deposit_switch == True:
        #     deposit_value = float(input(f"How much do you want to deposit? [0] Back\n\n>>>>>>> "))
        #     print('#'.center(WIDTH_PROGRAM, '#'))
        #     if deposit_value == 0:
        #         deposit_switch = False
        #     elif float(deposit_value) < 0:
        #         print(f"""{'INVALID VALUE'.center(WIDTH_PROGRAM / 2, ' ').center(WIDTH_PROGRAM, '#')}\n""")
        #     else:
        #         deposit_confirmation_switch = True
        #         while deposit_confirmation_switch == True:
        #             CONFIRM_DEPOSIT = input(f"Confirm a amount of R$ {deposit_value:.2f}?\n\n[1] Yes\n[2] No\n\n>>>>>>> ")
        #             if CONFIRM_DEPOSIT == "1":
        #                 saldo += float(deposit_value)
        #                 statement_msg = f"{statement_msg}\nDEPOSIT\t\t\t|\tR$ {deposit_value:.2f}"
        #                 print(f"DEPOSIT SUCESSFUL".center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, AUX))
        #                 confirmation_switch = True
        #                 while confirmation_switch == True:
        #                     cmd_confirmation = input('[0] Back >>>>>>> ')
        #                     if cmd_confirmation != "0":
        #                         print('INVALID OPTION'.ljust(WIDTH_PROGRAM_2, ' ').ljust(WIDTH_PROGRAM, '#'))
        #                     else:
        #                         confirmation_switch = False 
        #                 deposit_confirmation_switch = False
        #                 deposit_switch = False
        #             elif CONFIRM_DEPOSIT == "2":
        #                 print(f"DEPOSIT CANCELED".center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, AUX))
        #                 confirmation_switch = True
        #                 while confirmation_switch == True:
        #                     cmd_confirmation = input('[0] Back >>>>>>> ')
        #                     if cmd_confirmation != "0":
        #                         print('INVALID OPTION'.ljust(WIDTH_PROGRAM_2, ' ').ljust(WIDTH_PROGRAM, '#'))
        #                     else:
        #                         confirmation_switch = False 
        #                 deposit_confirmation_switch  = False
        #                 deposit_switch = False
        #             else:
        #                 print('INVALID OPTION'.center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, AUX))
    # elif opcao == "2":
    #     if WITHDRAW_LIMIT == 0:
    #         print(f"{'OPERATION NOT ALLOWED. LIMIT OF WITHDRAWALS REACHED'.center(60, ' ').center(WIDTH_PROGRAM, AUX)}\n")
    #         confirmation_switch = True
    #         while confirmation_switch == True:
    #             cmd_confirmation = input('[0] Back >>>>>>> ')
    #             if cmd_confirmation != "0":
    #                 print('INVALID OPTION'.center(WIDTH_PROGRA2, ' ').center(WIDTH_PROGRAM, '#'))
    #             else:
    #                 confirmation_switch = False
    #     elif saldo == 0:
    #         print(f"{'INSUFFICIENT BALANCE'.center(WIDTH_PROGRA2, ' ').center(WIDTH_PROGRAM, AUX)}\nYou have no account balance for withdrawal.")
    #         confirmation_switch = True
    #         while confirmation_switch == True:
    #             cmd_confirmation = input('[0] Back >>>>>>> ')
    #             if cmd_confirmation != "0":
    #                 print('INVALID OPTION'.center(WIDTH_PROGRA2, ' ').center(WIDTH_PROGRAM, '#'))
    #             else:
    #                 confirmation_switch = False
    #     else:
    #         print(f"{AUX * WIDTH_PROGRAM}\n{'WITHDRAW'.center(WIDTH_PROGRA2, ' ').center(WIDTH_PROGRAM, AUX)}\n")
    #         withdraw_switch = True
    #         while withdraw_switch == True:
    #             withdraw_value = float(input(f"How much do you want to withdraw? [0] Back\n\n>>>>>>> "))
    #             print('#' * WIDTH_PROGRAM)
    #             if withdraw_value == 0:
    #                 withdraw_switch = False
    #             elif withdraw_value < 0:
    #                 print(f"{'INVALID VALUE'.center(WIDTH_PROGRA2, ' ').center(WIDTH_PROGRAM, '#')}\n")
    #             elif withdraw_value > 0:
    #                 if withdraw_value > WITHDRAW_VALUE_LIMIT:
    #                     print(f"{'ERROR #01'.center(WIDTH_PROGRA2, ' ').center(WIDTH_PROGRAM, '#')}\n\nInformed value is greater than the withdraw ava"
    #                         "iable limit."f"\n(R$ {WITHDRAW_VALUE_LIMIT})\n\n{AUX * WIDTH_PROGRAM}")
    #                 elif withdraw_value > saldo:
    #                     print(f"{'ERROR #02'.center(WIDTH_PROGRA2, ' ').center(WIDTH_PROGRAM, '#')}\n\nInformed value is greater than the balance avai"
    #                         "able in the account."f"\n\n{AUX * WIDTH_PROGRAM}")
    #                 else:
    #                     withdraw_confirmation_switch = True
    #                     while withdraw_confirmation_switch == True:
    #                         CONFIRM_WITHDRAW = input(f"Confirm a amount of R$ {withdraw_value:.2f}?\n\n[1] Yes\n[2] No\n\n>>>>>>> ")
    #                         if CONFIRM_WITHDRAW == "1":
    #                             saldo -= withdraw_value
    #                             WITHDRAW_VALUE_LIMIT -= withdraw_value
    #                             WITHDRAW_LIMIT -= 1
    #                             statement_msg = f"{statement_msg}\nWITHDRAW\t\t|\tR$ {withdraw_value:.2f}"
    #                             print(f"WITHDRAW SUCESSFUL".center(WIDTH_PROGRA2, ' ').center(WIDTH_PROGRAM, AUX))
    #                             confirmation_switch = True
    #                             while confirmation_switch == True:
    #                                 cmd_confirmation = input('[0] Back >>>>>>> ')
    #                                 if cmd_confirmation != "0":
    #                                     print('INVALID OPTION'.ljust(WIDTH_PROGRA2, ' ').ljust(WIDTH_PROGRAM, '#'))
    #                                 else:
    #                                     confirmation_switch = False 
    #                             withdraw_confirmation_switch = False
    #                             withdraw_switch = False
    #                         elif CONFIRM_WITHDRAW == "2":
    #                             print(f"WITHDRAW CANCELED".center(WIDTH_PROGRA2, ' ').center(WIDTH_PROGRAM, AUX))
    #                             confirmation_switch = True
    #                             while confirmation_switch == True:
    #                                 cmd_confirmation = input('[0] Back >>>>>>> ')
    #                                 if cmd_confirmation != "0":
    #                                     print('INVALID OPTION'.ljust(WIDTH_PROGRA2, ' ').ljust(WIDTH_PROGRAM, '#'))
    #                                 else:
    #                                     confirmation_switch = False 
    #                             withdraw_confirmation_switch  = False
    #                             withdraw_switch = False
    #                         else:
    #                             print('INVALID OPTION'.center(WIDTH_PROGRA2, ' ').center(WIDTH_PROGRAM, '#'))
    # elif opcao == "3":
    #     print(f"""{'#' * WIDTH_PROGRAM}\n{'STATEMENT'.center(WIDTH_PROGRA2, ' ').center(WIDTH_PROGRAM, '#')}""")
    #     print(statement_msg)
    #     tab_test = '\t'
    #     print(f"""\n{'-' * WIDTH_PROGRAM}\n{f'ACCOUNT BALLANCE{tab_test}|{tab_test}R$ {saldo}'.ljust(WIDTH_PROGRA2, ' ')}\n{'#' * WIDTH_PROGRAM}""")
    #     confirmation_switch = True
    #     while confirmation_switch == True:
    #         cmd_confirmation = input('[0] Back >>>>>>> ')
    #         if cmd_confirmation != "0":
    #             print('INVALID OPTION'.center(WIDTH_PROGRA2, ' ').center(WIDTH_PROGRAM, '#'))
    #         else:
    #             confirmation_switch = False
    # elif opcao == "0":
    #     print(f"{AUX.ljust(WIDTH_PROGRAM, AUX)}\n{'EXITING SYSTEM'.center(WIDTH_PROGRA2, ' ').center(WIDTH_PROGRAM, AUX)}\n\n"
    #         + f"{'THANK YOU!'.center(WIDTH_PROGRAM, ' ')}\n\n"
    #         + f"{BANK_NAME.center(WIDTH_PROGRA2, ' ').center(WIDTH_PROGRAM, AUX)}\n{AUX.center(WIDTH_PROGRAM, AUX)}")
    #     main_menu_switch = False
    # else:
    #     print(f"{'#' * WIDTH_PROGRAM}\n{'INVALID OPTION'.center(WIDTH_PROGRA2, ' ').center(WIDTH_PROGRAM, AUX)}")