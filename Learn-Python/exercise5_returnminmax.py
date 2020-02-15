invoices = [6, 10, 20, 47, 69, 11, 50, 230, 3, 224, 39, 29, 5004]

def return_max():
    max = int()
    for i in invoices:
        if i > max:
            max = i
    return max

def return_min():
    min = invoices[0]
    for i in invoices:
      if i < min:
        min = i
    return min

print(f"\nInvoices minimum is {return_min()}.")
print(f"\nInvoices maximum is {return_max()}.")
