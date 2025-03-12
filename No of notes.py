amount=int(input("enter amount"))
five_hundred_notes=amount//500
remainder_amount=amount%500
hundred_notes=remainder_amount//100
remainder_amount=amount%100
fifty_notes=remainder_amount//50
remainder_amount=amount%50
ten_notes=remainder_amount//10
remainder_amount=amount%10
print("Five Hundred notes (500):",five_hundred_notes)
print("Hundred notes (100:",hundred_notes)
print("Fifty notes (50):",fifty_notes)
print("Ten notes (10):",ten_notes )
