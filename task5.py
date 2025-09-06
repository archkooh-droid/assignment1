user_talent =float(input("please enter your talent : "))
user_pound = float(input("please enter your pound : "))
user_lot =float(input("please enter your lot : "))
tal_to_pound = user_talent * 20
pound_to_lot = (user_pound + tal_to_pound) * 32
lot_to_gram = (user_lot + pound_to_lot) * 13.3
gram_to_kilogram = lot_to_gram // 1000
gram = lot_to_gram - (gram_to_kilogram * 1000)

print(f"you have {gram_to_kilogram} kilogram and {gram} gram")