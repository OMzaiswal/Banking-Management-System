import mysql.connector as my
con = my.connect(host="localhost", user="root", passwd="MySQL",database="bank_management")
cur = con.cursor()


def open_account():
    print("Please enter required details to open a new account")
    print()
    name = input("Full name: ")
    birth_date = input("Date of birth : DD-MM-YYYY ")
    address = input("Address: ")
    contact_no = int(input("Contact Number: "))
    opening_bal = int(input("Opening  balance: "))
    acc_no = "BNK" + name[0:2] + str(contact_no)

    data1 = (name, acc_no, birth_date, address, contact_no, opening_bal)
    data2 = (name, acc_no, opening_bal)
    query1 = "INSERT INTO account values(%s,%s,%s,%s,%s,%s)"
    query2 = "INSERT INTO amount values(%s,%s,%s)" 
    cur.execute(query1,data1)
    cur.execute(query2,data2)
    con.commit()
    print("\nAccount opened Successfully")
    print(f"Your account number is {acc_no}")
    main()

def cash_deposit():
    acc_no = input("Enter the account number: ")
    amt = int(input("Enter the amount you want to deposit: "))
    data = (amt, acc_no)

    query = "UPDATE amount SET bal= bal + %s WHERE acc_no = %s"
    cur.execute(query,data)
    con.commit()
    print(f"Rs.{amt} is credited to your account Successfully")
    main()

def cash_withdrawal():
    acc_no = input("Enter the account number: ")
    amt = int(input("Enter the amount you want to withdraw: "))
    data = (amt, acc_no)

    query = "UPDATE amount SET bal= bal - %s WHERE acc_no = %s"
    cur.execute(query,data)
    con.commit()
    print(f"Rs.{amt} is debited from your account Successfully")
    main()

def balance_enquiry():
    acc_no = input("Enter your account number to know your account balance: ")

    query = "SELECT bal FROM amount WHERE acc_no = %s"
    data = (acc_no,)
    cur.execute(query,data)
    res = cur.fetchone()
    print(f"Your current balance is Rs.{res[0]}")
    
    main()

def show_customer_details():
    acc_no = input("Enter your account number to know all the details of your account: ")

    query = '''
    SELECT ac.name,ac.acc_no,ac.birth_date,ac.address,ac.contact_no,ac.opening_bal,am.bal
    FROM account as ac JOIN amount as am ON ac.acc_no = am.acc_no
    WHERE ac.acc_no = %s
    '''
    data = (acc_no,)
    cur.execute(query,data)
    res = cur.fetchone()
    print()
    print("-----------Your Details----------")
    print()
    print(f"NAME: {res[0]}")
    print(f"ACCOUNT NUMBER: {res[1]}")
    print(f"DOB: {res[2]}")
    print(f"ADDRESS: {res[3]}")
    print(f"CONTACT NUMBER: {res[4]}")
    print(f"OPENING BALANCE: {res[5]}")
    print(f"CURRENT BALANCE: {res[6]}")
    print("-"*34)

    main()

def close_account():
    acc_no = input("Enter your account number to close your account: ")

    query1 = "DELETE FROM account WHERE acc_no = %s"
    query2 = "DELETE FROM amount WHERE acc_no = %s"
    data = (acc_no,)
    cur.execute(query1,data)
    cur.execute(query2,data)
    con.commit()
    main()

def main():
    print('''
    Welcome to BANK Services

    1. OPEN NEW ACCOUNT
    2. CASH DEPOSIT
    3. CASH WITHDRAWAL
    4. BALANCE ENQUIRY
    5. DISPLAY CUSTOMER DETAILS
    6. CLOSE ACCOUNT
    7. EXIT
    ''')
    choice = input("Enter the task number of your choice from the above services: ")
    print()

    if choice == '1':
        open_account()

    elif choice == '2':
        cash_deposit()

    elif choice == '3':
        cash_withdrawal()

    elif choice == '4':
        balance_enquiry()

    elif choice == '5':
        show_customer_details()

    elif choice == '6':
        close_account()

    elif choice == '7':
        print("\nThanks for visiting, Goodbye!")
        print()
        exit()

    else:
        print("Invalid choice, Try again...")

    main()

print("################################################################################")
main()