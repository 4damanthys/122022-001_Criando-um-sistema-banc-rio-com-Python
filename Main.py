saldo = 0
WITHDRAW_VALUE_LIMIT = 500
statement = []
allowed_keys = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
withdraw = 0
WITHDRAW_LIMIT = 3
AUX = "#"
BANK_NAME = "TH&_@DAM4NTHY$ BANK CO."
WIDTH_PROGRAM = 70
WIDTH_PROGRAM_2 = 35

main_menu = f"""{'MAIN MENU'.center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, AUX)}

[1] Deposit ;
[2] Withdraw ;
[3] Statement ;
[0] Exit

>>>>>>> """

exit_message = f"""{'EXIT'.center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, AUX)}
Do you really want to exit?

[1] Yes
[2] No 

>>>>>>> """
# -------------------------------------------------------------------------------------------------------------------------------------------------------
intro_message = f"""{'#'.center(WIDTH_PROGRAM, '#')}
{BANK_NAME.center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, AUX)}"""

statement_message = 'TRANSACTION       |   VALUE'

print(intro_message)
main_menu_switch = True
while main_menu_switch == True:
    opcao = input(main_menu)
    if opcao == "1":
        print(f"""{'#'.center(WIDTH_PROGRAM, '#')}\n{'DEPOSIT'.center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, '#')}\n""")
        deposit_switch = True
        while deposit_switch == True:
            deposit_value = float(input(f"How much do you want to deposit? [0] Back\n\n>>>>>>> "))
            print('#'.center(WIDTH_PROGRAM, '#'))
            if deposit_value == 0:
                deposit_switch = False
            elif float(deposit_value) < 0:
                print(f"""{'INVALID VALUE'.center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, '#')}\n""")
            else:
                deposit_confirmation_switch = True
                while deposit_confirmation_switch == True:
                    CONFIRM_DEPOSIT = input(f"Confirm a amount of R$ {deposit_value:.2f}?\n\n[1] Yes\n[2] No\n\n>>>>>>> ")
                    if CONFIRM_DEPOSIT == "1":
                        saldo += float(deposit_value)
                        statement_message = f"{statement_message}\nDEPOSIT           |   R$ {deposit_value:.2f}"
                        print(f"DEPOSIT SUCESSFUL".center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, AUX))
                        confirmation_switch = True
                        while confirmation_switch == True:
                            cmd_confirmation = input('[0] Back >>>>>>> ')
                            if cmd_confirmation != "0":
                                print('INVALID OPTION'.ljust(WIDTH_PROGRAM_2, ' ').ljust(WIDTH_PROGRAM, '#'))
                            else:
                                confirmation_switch = False 
                        deposit_confirmation_switch = False
                        deposit_switch = False
                    elif CONFIRM_DEPOSIT == "2":
                        print(f"DEPOSIT CANCELED".center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, AUX))
                        confirmation_switch = True
                        while confirmation_switch == True:
                            cmd_confirmation = input('[0] Back >>>>>>> ')
                            if cmd_confirmation != "0":
                                print('INVALID OPTION'.ljust(WIDTH_PROGRAM_2, ' ').ljust(WIDTH_PROGRAM, '#'))
                            else:
                                confirmation_switch = False 
                        deposit_confirmation_switch  = False
                        deposit_switch = False
                    else:
                        print('INVALID OPTION'.center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, AUX))
    elif opcao == "2":
        if WITHDRAW_LIMIT == 0:
            print(f"{'OPERATION NOT ALLOWED. LIMIT OF WITHDRAWALS REACHED'.center(60, ' ').center(WIDTH_PROGRAM, AUX)}\n")
            confirmation_switch = True
            while confirmation_switch == True:
                cmd_confirmation = input('[0] Back >>>>>>> ')
                if cmd_confirmation != "0":
                    print('INVALID OPTION'.center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, '#'))
                else:
                    confirmation_switch = False
        elif saldo == 0:
            print(f"{'INSUFFICIENT BALANCE'.center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, AUX)}\nYou have no account balance for withdrawal.")
            confirmation_switch = True
            while confirmation_switch == True:
                cmd_confirmation = input('[0] Back >>>>>>> ')
                if cmd_confirmation != "0":
                    print('INVALID OPTION'.center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, '#'))
                else:
                    confirmation_switch = False
        else:
            print(f"{AUX * WIDTH_PROGRAM}\n{'WITHDRAW'.center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, AUX)}\n")
            withdraw_switch = True
            while withdraw_switch == True:
                withdraw_value = float(input(f"How much do you want to withdraw? [0] Back\n\n>>>>>>> "))
                print('#' * WIDTH_PROGRAM)
                if withdraw_value == 0:
                    withdraw_switch = False
                elif withdraw_value < 0:
                    print(f"{'INVALID VALUE'.center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, '#')}\n")
                elif withdraw_value > 0:
                    if withdraw_value > WITHDRAW_VALUE_LIMIT:
                        print(f"{'ERROR #01'.center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, '#')}\n\nInformed value is greater than the withdraw ava"
                            "iable limit."f"\n(R$ {WITHDRAW_VALUE_LIMIT})\n\n{AUX * WIDTH_PROGRAM}")
                    elif withdraw_value > saldo:
                        print(f"{'ERROR #02'.center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, '#')}\n\nInformed value is greater than the balance avai"
                            "able in the account."f"\n\n{AUX * WIDTH_PROGRAM}")
                    else:
                        withdraw_confirmation_switch = True
                        while withdraw_confirmation_switch == True:
                            CONFIRM_WITHDRAW = input(f"Confirm a amount of R$ {withdraw_value:.2f}?\n\n[1] Yes\n[2] No\n\n>>>>>>> ")
                            if CONFIRM_WITHDRAW == "1":
                                saldo -= withdraw_value
                                WITHDRAW_VALUE_LIMIT -= withdraw_value
                                WITHDRAW_LIMIT -= 1
                                statement_message = f"{statement_message}\nWITHDRAW          |   R$ {withdraw_value:.2f}"
                                print(f"WITHDRAW SUCESSFUL".center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, AUX))
                                confirmation_switch = True
                                while confirmation_switch == True:
                                    cmd_confirmation = input('[0] Back >>>>>>> ')
                                    if cmd_confirmation != "0":
                                        print('INVALID OPTION'.ljust(WIDTH_PROGRAM_2, ' ').ljust(WIDTH_PROGRAM, '#'))
                                    else:
                                        confirmation_switch = False 
                                withdraw_confirmation_switch = False
                                withdraw_switch = False
                            elif CONFIRM_WITHDRAW == "2":
                                print(f"WITHDRAW CANCELED".center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, AUX))
                                confirmation_switch = True
                                while confirmation_switch == True:
                                    cmd_confirmation = input('[0] Back >>>>>>> ')
                                    if cmd_confirmation != "0":
                                        print('INVALID OPTION'.ljust(WIDTH_PROGRAM_2, ' ').ljust(WIDTH_PROGRAM, '#'))
                                    else:
                                        confirmation_switch = False 
                                withdraw_confirmation_switch  = False
                                withdraw_switch = False
                            else:
                                print('INVALID OPTION'.center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, '#'))
    elif opcao == "3":
        print(f"""{'#' * WIDTH_PROGRAM}\n{'STATEMENT'.center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, '#')}""")
        print(statement_message)
        print(f"""\n{'-' * WIDTH_PROGRAM}\n{f'ACCOUNT BALLANCE  |   R$ {saldo}'.ljust(WIDTH_PROGRAM_2, ' ')}\n{'#' * WIDTH_PROGRAM}""")
        confirmation_switch = True
        while confirmation_switch == True:
            cmd_confirmation = input('[0] Back >>>>>>> ')
            if cmd_confirmation != "0":
                print('INVALID OPTION'.center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, '#'))
            else:
                confirmation_switch = False
    elif opcao == "0":
        print(f"{AUX.ljust(WIDTH_PROGRAM, AUX)}\n{'EXITING SYSTEM'.center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, AUX)}\n\n"
            + f"{'THANK YOU!'.center(WIDTH_PROGRAM, ' ')}\n\n"
            + f"{BANK_NAME.center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, AUX)}\n{AUX.center(WIDTH_PROGRAM, AUX)}")
        main_menu_switch = False
    else:
        print(f"{'#' * AUX}\n{'INVALID OPTION'.center(WIDTH_PROGRAM_2, ' ').center(WIDTH_PROGRAM, AUX)}")