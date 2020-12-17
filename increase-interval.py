# User Variables
user_name = input("What Is Your Name? ")
users_bets = int(input("How Many Bets Would You Like To Do? "))
currency_symbol = input("What is the Symbol of your Currency? ")
bet_increase_interval = int(input("How Often Do You Want To Increase Bet? "))
bet_increase_amount_percentage = int(input("By How Much Do You Want To Increase Bet?\n(Please Enter in Number to represent Percentage) "))

# Counting Variables
bet_count = 0
amount_lost = 0.0
bet_amount = 1.0


# Keeps Running Until User No Longer Can Bet
print()
while users_bets != 0:
    # Completes A Bet
    amount_lost += bet_amount
    
    # Prints Out Each Bet (Can Be Disabled By Commenting It Out)
    print("Amount Lost: " + '{0:.8f}'.format((amount_lost*0.00000001)) + " " + currency_symbol)
    print("Bet Amount: " + '{0:.8f}'.format((bet_amount*0.00000001)) + " " + currency_symbol)
    print("Bet Count: " + str(bet_count+1) + " Bets\n")
    
    # Subtracts From Bets Left & Increases Total Bets Done
    users_bets -= 1
    bet_count += 1
    
    # If It Has Been bet_increase_interval Bets, Increase By 100% (As Long As There Are Bets Left To Do)
    if users_bets != 0 and (bet_count % bet_increase_interval) == 0:
        bet_amount = bet_amount + (bet_amount * float(bet_increase_amount_percentage * .01))


# Print Out user_name's Stupid Explanations
print("=========================================================================")
print(user_name + "'s Stupid Stats")
print("Number of Bets: " + str(bet_count))
print("Last Bet Amount: " + '{0:.8f}'.format((bet_amount*0.00000001)) + " " + currency_symbol)
print("Amount Lost: " + '{0:.8f}'.format((amount_lost*0.00000001)) + " " + currency_symbol)
print("=========================================================================")
