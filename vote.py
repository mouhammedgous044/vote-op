try:
  age=int(input("Enter your name:"))
  if age>=18:
    print(f"Your are eligible to vote.")
  else:
    print(f"Your are not eligible to vote.")
  except ValueError:
    print(f"Please enter a valid integer for age.")


