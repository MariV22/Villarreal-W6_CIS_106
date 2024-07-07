# Prompt the user to enter the filename
filename = input("Enter the filename to save the data (e.g., items.txt): ")

# Open the file in write mode
with open(filename, 'w') as file:
    while True:
        # Prompt the user to enter the item details
        item = input("\nEnter the item name (or type 'done' to finish): ")
        if item.lower() == 'done':
            break

        quantity = int(input("Enter the quantity: "))
        price = float(input("Enter the price: "))

        # Write the item details to the file
        file.write(f"Item: {item}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Price: {price}\n\n")  # Add a blank line to separate records

print(f"\nData has been saved to '{filename}'.")

# Initialize variables to keep track of totals and count
total_extended_price = 0
order_count = 0

# Open the file and read it line by line
with open(filename, 'r') as file:
    while True:
        # Read the item
        item_line = file.readline()
        if not item_line:
            break  # End of file

        item = item_line.strip().split(': ')[1]  # Extract the item

        # Read the quantity
        quantity_line = file.readline()
        quantity = int(quantity_line.strip().split(': ')[1])  # Extract the quantity

        # Read the price
        price_line = file.readline()
        price = float(price_line.strip().split(': ')[1])  # Extract the price

        # Compute the extended price
        extended_price = quantity * price

        # Display item details
        print(f"Item: {item}, Quantity: {quantity}, Price: {price:.2f}, Extended Price: {extended_price:.2f}")

        # Update totals
        total_extended_price += extended_price
        order_count += 1

        # Read the blank line separating orders
        file.readline()

# Compute the average order price
average_order_price = total_extended_price / order_count if order_count > 0 else 0

# Display the summary
print(f"\nTotal Extended Price: {total_extended_price:.2f}")
print(f"Number of Orders: {order_count}")
print(f"Average Order Price: {average_order_price:.2f}")