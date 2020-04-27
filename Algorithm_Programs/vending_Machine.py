def vending_machine(changing_amount, avilable_notes):
    i = 0
    total_notes = 0
    while changing_amount > 0:
        notes = changing_amount // avilable_notes[i]
        if notes > 0:
            print(notes, "notes of", avilable_notes[i], "rupee")
            changing_amount = changing_amount % avilable_notes[i]
            total_notes += notes
        i += 1
    return total_notes


changing_amount = int(input("Enter the amount to return by the vending machine: "))
avilable_notes = [1000, 500, 100, 50, 10, 5, 2, 1]
print("Total Number of notes :", vending_machine(changing_amount, avilable_notes))
