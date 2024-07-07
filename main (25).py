def calculate_interest():
  while True:
      try:
          principle = float(input("Enter principle amount: "))
          rate = float(input("Enter interest rate: "))
          break
      except ValueError:
          print("Invalid input. Please enter numeric values.")

  beginning_balance = principle
  total_interest = 0.0

  print(f"\n{'Year':<10}{'Beginning Balance':<20}{'Ending Balance':<20}")

  for year in range(1, 6):
      interest = beginning_balance * rate
      ending_balance = beginning_balance + interest
      total_interest += interest

      print(f"{year:<10}${beginning_balance:,.2f}{'$':>8}{ending_balance:,.2f}")

      beginning_balance = ending_balance

  print(f"Total interest earned: ${total_interest:,.2f}")

# Run the function
calculate_interest()