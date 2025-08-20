import logging as lg
lg.basicConfig(filename="app.log",
               level=lg.DEBUG,
               format="[%(asctime)s-%(levelname)s]-%(message)s")
#operations
operations=(
    "1.balance enquiry\n",
    "2.withdrawal\n",
    "3.deposit\n",
    "4.transfer\n",
    "5.history\n",
    "6.exit"
)
#accounts table
account_details={12345678:2916,
                 654321:6700}
#users_table
users_table={12345678:["krishna",'date of birth',1000],
             654321:["reddy","birthday",1250]}
#checking user login
def check_login(account_no:int,pin:int):
    #check user present in table
    if account_no in account_details:
        #pin validation
        if account_details[account_no]==pin:
            lg.info("user successfully logined")
            return True
        else:
            lg.warning("incorrect login credentials")
    else:
        lg.warning("user not found")
        return False
#balance enquiry
def balance_enquiry(account_no):
    lg.debug("user in balance page")
    if account_no in users_table:
        amount=users_table[account_no][2]
        lg.info(f"{account_no} user current amount{amount}")
        print(f"{account_no} user current amount{amount}")
    else:
        lg.warning("user not found")
        print("user not found")
    pass
#withdrawal function
def withdrawal(account_no):
    lg.debug("user in withdrawal page")
    amount=users_table[account_no][2]
    withdraw_amount=int(input("please enter withdraw amount:"))
    if amount>=withdraw_amount:
        users_table[account_no][2]-=withdraw_amount
        lg.info(f'{withdraw_amount} withdraw successfully and current amount{users_table[account_no][2]}')
        print(f'{withdraw_amount} withdraw successfully and current amount{users_table[account_no][2]}')
    else:
        lg.info("insufficient amount")
        print("insufficient amount")
    pass
#deposit function
def deposit(account_no):
    lg.debug("user in deposit page")
    deposit_amount=int(input("please enter deposit amount:"))

    users_table[account_no][2]-=deposit_amount
    lg.info(f'{deposit_amount} deposit successfully and current amount{users_table[account_no][2]}')
    print(f'{deposit_amount} deposit successfully and current amount{users_table[account_no][2]}')
    
    pass
#transfer functionss
def transfer(account_no:int):
    lg.debug("user in transfer page")
    transfer_account=int(input("enter the account number:"))
    transfer_amount=int(input('enter the transfer amount:'))
    current_amount=users_table[account_no][2]
    if transfer_account in users_table:
        if transfer_amount<=current_amount:
            #amount update in accounts
            users_table[account_no][2]-=transfer_amount
            users_table[transfer_account][2]+=transfer_account
            lg.info(f"{transfer_amount} transfer successfully and current amount is{users_table[account_no][2]}")
            print(f"{transfer_amount} transfer successfully and current amount is{users_table[account_no][2]}")
        else:
            lg.warning('insufficient balance')
            print("insufficient balance")
    else:
        lg.warning(f"{transfer_account} user not found")
        print(f"{transfer_account} user not found")


    pass
#history 
def history(account_no):
    lg.debug("user in history page")
    print("function developing under processing")
    pass
#exit
def exit_fun():
    lg.debug("user in exit")
    print('successfully exited from codegnan online banking system')
    return True
    pass
#transaction update in table
#def transaction_update(account_no:int):

 #select operation
def choose_operation(account_no:int,choice:int):
    val=False
    if choice==1:
        balance_enquiry(account_no=account_no)
    elif choice==2:
        withdrawal(account_no=account_no)
    elif choice==3:
        deposit(account_no=account_no)
    elif choice==4:
        transfer(account_no=account_no)
    elif choice==5:
        history(account_no=account_no)
    elif choice==6:
        val=exit_fun()
    else:
        print("invalid choice,please select between 1-6")
    if val:
        return val

#main function
if __name__=="__main__":
    print("welcome to the online codegnan banking")
    lg.info("welcome to the online codegnan banking")
    account_no=int(input("please,enter your account number:"))
    pin=int(input("please,enter your pin:"))
    lg.info("user account number is {account_no} and pin is{pin}")
    while True:
        if check_login(account_no=account_no,pin=pin):
           print(*operations)
           lg.info(operations)
           choice=int(input("select operation(1-6):"))
           exit_fun_val=choose_operation(account_no=account_no,choice=choice)
           if exit_fun_val:
               break
        else:
            lg.warning(f"login credentials incorrect{account_no} and {pin}")
            print(f"login credentials incorrect{account_no} and {pin}")
            break
