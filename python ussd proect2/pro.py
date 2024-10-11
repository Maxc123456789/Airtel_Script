import time
#my_offer

#PhoneNumber
def buydata():
    start = time.time()
    print('')
    print('_' * 150)
    print("\t\t| Option Menu              |")
    print("\t    |--------------------------|")
    print("      |      1.Daily Bundle\n"
          "      |      2.Weekly Bundle\n"
          "      |      3.Monthly Bundle\n"
          "      |      22.Back\n"
          "      |      0.Menu\n"
          "      |      #.Cancel\n")
    dataopt = input("   : \033[0m")
    end = time.time()
    time.sleep(2)
    if dataopt == '1':
        priceofdaily()
    elif dataopt == '2':
        priceofWeekly()
    elif dataopt == '3':
        priceofmonth()
    elif dataopt == '22':
        transaction()
    elif dataopt == '0':
        transaction()
    elif dataopt == '#':
        goodbye()
    else:
        print('invalid Selection\n'
              'Try again')
        buydata()
#price for daily bundle
def priceofdaily():
    start = time.time()
    print('')
    print('_' * 150)
    print("\t\t| Option Menu              |")
    print("\t    |--------------------------|")
    print("      |      1.N100/100Mb/daily\n"
          "      |      2.N200/200Mb/daily\n"
          "      |      3.N300/300Mb daily\n"
          "      |      4.N400 for 400Mb daily\n"
          "      |      5.N500 for 1Gb daily\n"
          "      |      22.Back\n"
          "      |      0.Menu\n"
          "      |      #.Cancel\n")
    optiondaily = input("   : \033[0m")
    end = time.time()
    time.sleep(2)
    if optiondaily == '1':
        print(f' Your Recharge of 100MB is Successful ')
    elif optiondaily == '2':
        print(f' Your Recharge of 200MB is Successful ')
    elif optiondaily == '3':
        print(f' Your Recharge of 300MB is Successful ')
    elif optiondaily == '4':
        print(f' Your Recharge of 400MB is Successful ')
    elif optiondaily == '5':
        print(f' Your Recharge of 1GB is Successful ')
    elif optiondaily == '22':
        buydata()
    elif optiondaily == '0':
	    transaction()
    elif optiondaily == '#':
        goodbye()
    else:
        print("invalid option\n"
              "Select the options listed")
        priceofdaily()
    time.sleep(3)
#price of weekly
def priceofWeekly():
    start = time.time()
    print('')
    print('_' * 150)
    print("\t\t| Option Menu              |")
    print("\t    |--------------------------|")
    print("      |      1.N500/750Mb/5days\n"
          "      |      2.N500/1GB/7days \n"
          "      |      3.N1500/5GB/7days\n"
          "      |      4.N350/350mb/7days\n"
          "      |      5.N100/All Social/5days \n"
          "      |      22.Back\n"
          "      |      0.Menu\n"
          "      |      #.Cancel\n")
    optionwkly = input("   : \033[0m")
    end = time.time()
    time.sleep(2)
    if optionwkly == '1':
        print(f'your Recharge of 750MB was Successful ')
    elif optionwkly == '2':
        print(f'your Recharge of 1GB was Successful ')
    elif optionwkly == '3':
        print(f'your Recharge of  5GB was Successful ')
    elif optionwkly == '4':
        print(f'your Recharge of 350MB was Successful ')
    elif optionwkly == '5':
        print(f'your Recharge of All Social  was Successful ')
    elif optionwkly == '22':
        buydata()
    elif optionwkly == '0':
        transaction()
    elif optionwkly == '#':
        goodbye()
    else:
        print("invalid option\n"
              "Select the options listed")
        priceofWeekly()
def priceofmonth():
    start = time.time()
    print('')
    print('_' * 150)
    print("\t\t| Option Menu              |")
    print("\t    |--------------------------|")
    print("      |      1.N1000/1.2GB\n"
          "      |      2.N1200/1.5GB \n"
          "      |      3.N1500/3GB/\n"
          "      |      4.N2000/4.5GB\n"
          "      |      5.N2500/10GB/5days \n"
          "      |      22.Back\n"
          "      |      0.Menu\n"
          "      |      #.Cancel\n")
    optionmonthly = input("   : \033[0m")
    end = time.time()
    time.sleep(1)
    if optionmonthly == '1':
        print(f'your Recharge of 1.2GB was Successful ')
    elif optionmonthly == '2':
        print(f'your Recharge of 1.5GB was Successful ')
    elif optionmonthly == '3':
        print(f'your Recharge of 3GB  was Successful ')
    elif optionmonthly == '4':
        print(f'your Recharge of 4.5GB was Successful ')
    elif optionmonthly == '5':
        print(f'your Recharge of 10GB  was Successful ')
    elif optionmonthly == '22':
        buydata()
    elif optionmonthly == '0':
        transaction()
    elif optionmonthly == '#':
        goodbye()
    else:
        print("invalid option\n"
              "Select the options listed")
        priceofmonth()
def priceofsocialplan():
    start = time.time()
    print('')
    print('_' * 150)
    print("\t\t| Option Menu              |")
    print("\t    |-------------------------------------|")
    print("      |      1.facebook/N500/750MB/1month\n"
          "      |      2.whatsapp/N300/300MB/1month \n"
          "      |      3.instagram/N1000/2GB/1month\n"
          "      |      4.tiktok/N1500/3GB/1month\n"
          "      |      5.N100/All Social/1GB/1days \n"
          "      |      22.Back\n"
          "      |      0.Menu\n"
          "      |      #.Cancel\n")
    optionsocialplan = input("   : \033[0m")
    end = time.time()
    time.sleep(2)
    if optionsocialplan == '1':
        print(f'your Recharge of 750MB was Successful ')
    elif optionsocialplan == '2':
        print(f'your Recharge of 300MB was Successful ')
    elif optionsocialplan == '3':
        print(f'your Recharge of  2GB was Successful ')
    elif optionsocialplan == '4':
        print(f'your Recharge of 3GB was Successful ')
    elif optionsocialplan == '5':
        print(f'your Recharge of All Social of 1GB was Successful ')
    elif optionsocialplan == '22':
        buydata()
    elif optionsocialplan == '0':
        transaction()
    elif optionsocialplan == '#':
        goodbye()
    else:
        print("invalid option\n"

"Select the options listed")

def airtimepurchase():
    start = time.time()
    print('')
    print('_' * 150)
    print("\t\t| Option Menu              |")
    print("\t    |--------------------------|")
    print("      | Input Phone Number Below\n"
          "      |      *.Back\n"
          "      |      #.Cancel\n")
    phone = input("   : \033[0m")
    end = time.time()
    time.sleep(1)
    if len(phone) == 11 and phone.isnumeric():
        checkamount(phone)
    elif phone == "*":
        transaction()
    elif phone == "#":
        goodbye()
    else:
        print("Invalid Phone number\n"
              "Try Again\n"
              )
# Airtime purchase amount syntax
def checkamount(x):
    amt = input("Enter Amount:")
    time.sleep(1)
    if amt.isnumeric():
        print(f"{x} Has Been Credited With ${amt} Successfully")
    else:
        print("Invalid Amount\n"
              "Try Again\n"
              )
#### Borrow credits
def Airtimecredit():
    start = time.time()
    print('')
    print('_' * 150)
    print("\t\t| Option Menu              |")
    print("\t    |--------------------------|")
    print("      | You can borrow up to N6000\n"                                          
          "      |      1. 6000\n"
          "      |      2. 5000\n"
          "      |      3. 4000\n"
          "      |      4. 3000\n"
          "      |      5. 2000\n"
          "      |      6. 1000\n"
          "      |      0. next\n"
          "      |      22.Back\n"
          "      |      0.Menu\n"
          "      |      #.Cancel\n")
    creditcode = input("   : \033[0m")
    end = time.time()
    time.sleep(2)
    if creditcode == "1":
        print("You have been credited with N6000")
    elif creditcode == "2":
        print("You have been credited with N5000")
    elif creditcode == "3":
        print("You have been credited with N4000")
    elif creditcode == "4":
        print("You have been credited with N3000")
    elif creditcode == "5":
        print("You have been credited with N2000")
    elif creditcode == "6":
        print("You have been credited with N1000")
    elif creditcode == "0":
        BorrowAirtime()
    elif creditcode == "*":
        transaction()
    elif creditcode == "#":
        goodbye()
    else:
        print("Invalid Reply\n"
              "Try Again\n"
        )
def BorrowAirtime():
    start = time.time()
    print('')
    print('_' * 150)
    print("\t\t| Option Menu              |")
    print("\t    |--------------------------|")
    print("      | You can borrow up to N6000\n"                                          
          "      |      7. 9000\n"
          "      |      8. 8000\n"
          "      |      9. 7000\n"
          "      |      10. 5000\n"
          "      |      11. 200\n"
          "      |      12. 100\n"
          "      |      13. 50\n"
          "      |      22.Back\n"
          "      |      #.Cancel\n")
    turnover = input("   : \033[0m")
    end = time.time()
    time.sleep(2)
    if turnover == "7":
        print("You have been credited with N900")
    elif turnover == "8":
        print("You have been credited with N800")
    elif turnover == "9":
        print("You have been credited with N700")
    elif turnover == "10":
        print("You have been credited with N500")
    elif turnover == "11":
        print("You have been credited with N200")
    elif turnover == "12":
        print("You have been credited with N100")
    elif turnover == "13":
        print("You have been credited with N50")
    elif turnover == "22":
        Airtimecredit()
    elif turnover == "#":
        goodbye()
    else:
        print("Invalid Reply\n"
              "Try Again\n"
              )
def data_balance():
    transCode = input('1. check data balance\n'
                      '2. go back to first page\n'
                      'select option:')
    if transCode == '1':
        print('your Balances Are:\n'
              'Monthly Bundle: 0.00MB till 17-05-2024,12:05:00\n'
              'Daily Bundle: 441.66MB till 09-05-2024,09:04:05\n'

'YouTube Night: 56013.71MB till 17-05-2024,08:05:08\n'
              'Spotify Bonus: 1002.28MB (Expired)'
              'To rollover expired data,dial *312# and renew your bundle now\n'
              'Get 20% BONUS data when you click https://bit.ly/2XIWTnO and buy a data bundle from My Airtel app')
    elif transCode == '2':
        print('first page')
    else:
        print('Invalid entry\n'
              'Try again')
        data_balance()
def account():
    transCode = input('1. main balance \n'
                      '2. loan balance \n'
                      '3. talk time balance \n'
                      '4. go back to first page \n'
                      'select information:')

    if transCode == '1':
        print('Main Bal:N36770.50')
    elif transCode == '2':
        print('Loan Bal : N0.00')
    elif transCode == '3':
        print('TalkTime:N0.00')
    elif transCode == '4':
        print('first page')
    else:
        print('Invalid ussd code\n'
              'Try again')
        account()

def share():
    airshare = input(
             "Welcome to Airtime and Data Transfer/Gift service.\n"
             "Please select the service to transfer/gift.\n"
             "    1. Airtime Share\n"
             "    2. Gift Data\n"
             "    3. SME Data Share\n"
             "    *. BACK\n"
             "    #. CANCEL\n"
             "  : "
             )
    time.sleep(2)
    if airshare == "1":
        print("You have ")
    elif airshare == "2":
        print("You have ")
    elif airshare == "3":
        print("You have b")
    elif airshare == "*":
        transaction()
    elif airshare == "#":
        goodbye()
    else:
        print("Invalid Reply\n"
              "Try Again\n"
              )




######password phase...


# define a string containing alpha numeric and numbers
# str1 = "sdf 23 safs8 5 sdfsd8 sdfs 5 21sfs 20 5"
#
# #split the string into a list of substrings seperated by spaces
# str_num = [i for i in str1.split(' ')]
#
# #cal the length  of the list of substrings
# length = len(str_num)
#
# #Extract and sort the numbers found within the sunstrings, conveting them to integers
# numbers = sorted([x for x in str_num if x.isdigit()])
# print(numbers)
#
# #print the sorted numbers that are greater than the length of the list of substrings
# print('Numbers in sorted form:')
# result = list(filter(lambda x: int(x) > length, numbers))
# print(result)

# def masterPassword():
#     User = input(' Enter master password:  ')
#     if User == '':
#         print('you have logged in Successfully')
#     else:
#         print('invalid Password\n'
#               'you have 3 attempts left '
#               )
#     sec_attempt = input('Enter master password: ')
#
#     if sec_attempt == User:
#         print('you have logged in Successfully')
#     else:
#         print('invalid Password\n'
#               'you have 2 attempts left '
#               )
#
#     Third_attempt = input('Enter master password: ')
#
#     if Third_attempt == User:
#         print('you have logged in Successfully')
#     else:
#         print('invalid Password\n'
#               'you have 1 attempts left '
#               )
#     last_attempt = input('Enter master password: ')
#
#     if last_attempt == User:
#         print('you have logged in Successfully')
#     else:
#         print('invalid Password\n'
#               'Meet the Admin  '
#               )
dial()

# masterPassword()