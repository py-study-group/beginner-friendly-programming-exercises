# Get everything we need from the users in the appropriate types.
money = int(input("How much money do you have: "))
btc = int(input("The value of BTC: "))
eth = int(input("The value of ETH: "))
ltc = int(input("The value of LTC: "))

# See how much we can buy of everything.
# Note the double / to round the division down and keep it an integer.
amount_btc = money // btc
amount_eth = money // eth
amount_ltc = money // ltc

# Let the user know what he can buy and how much.
# Because there is just one value we need in the string it is overkill to use .format()
# Instead we use str() to convert the values to a string, so we can append them to the other strings and print them.
print("You can buy:")
print("Bitcoins: " + str(amount_btc))
print("Ethereum: " + str(amount_eth))
print("Litecoin: " + str(amount_ltc))
