# menu driven calculator
menu = input("""
        
Hi ! how can i help you"
1. Enter 1 for pin change
2. Enter 2 for balance check
3. Enter 3 for withdrawl
4. Enter 4 for exit 
        
""")

if menu == '1':
    print("Pin Change")
elif menu == '2':
    print('Balance Check')
elif menu == '3':
    print("Withdraw")
else:
    print(exit)