""" This takes in a document with customer orders and checks if they overpaid for their melons.
    
It starts with a for loop stripping the white space from each line,
then tokenizes them and assigns the variables customer_name, _customer_melons, and customer_paid

Then it runs a for loop to go through that list and checks whether customer_paid
is the same as customer_expected (which is the number of melons * 1.00) 

Then it spits out statement that says the customer's name, what they paid, and
what was expected. If they paid what was expected it doesn't say anything"""


def invoice_checker(order_doc): #creates function with input order_doc
    order_data = open(order_doc)
    for line in order_data:
        tokens = line.split('|') #tokenizes line
        customers_name = tokens[1] 

        name_parts = customers_name.split(" ")
        first_name = name_parts[0]
        customers_melons = float(tokens[2])
        customers_paid = float(tokens[3])

        customers_expected = 1.00 * customers_melons #calculates expected pay

        if customers_expected != customers_paid: #checks if customer paid correct amount
            print(f"Customer {first_name} paid ${customers_paid} expected ${customers_expected}")

invoice_checker("customer-orders.txt")
# melon_cost = 1.00

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )
