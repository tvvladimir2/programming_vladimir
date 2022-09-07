num_pizzas = eval(input("How much pizzas do you want?"))
cost_pizzas = eval(input("How much does the pizza cost?"))
total = num_pizzas * cost_pizzas
tax_rate = 0.08
sales_tax = subtotal * tax_rate
total = subtotal + sales_tax
print("Total cost $", total)
print("In that number $", subtotal, "for the pizza and")
print("$", sales tax, "tax from sales.")
