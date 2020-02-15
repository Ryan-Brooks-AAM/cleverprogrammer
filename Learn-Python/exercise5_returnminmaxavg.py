#invoices = [6, 10, 20, 47, 69, 11, 50, 230, 3, 224, 39, 29, 5004]

# Program validation data.  This data should return a minimum of 1, a maximum of 3, and an average of 2.
invoices = [1, 2, 3]

# Function to return max.
def return_max():
    max = int()
    for i in invoices:
        if i > max:
            max = i
    return max

# Function to return min.
def return_min():
    min = invoices[0]
    for i in invoices:
      if i < min:
        min = i
    return min

# Function to return average.
def return_average():
    total = int()
    for i in invoices:
      total = total + i
    return (total / len(invoices))


print(f"\nInvoices minimum is {return_min()}.\n")
print(f"\nInvoices maximum is {return_max()}.\n")
print(f"\nInvoices average is {return_average()}.\n")
