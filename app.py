import sys
def get_numeric_input(prompt, entry_type=float):
    while True:
        try:
            val = input(prompt).strip()
            if not val:
                return 0
            return entry_type(val)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print(" BILLING SYSTEM INTERACTIVE MENU ")
    
    while True:
        print("\n--- MENU ---")
        print("1. Push 1: Calculate Total Bill")
        print("2. Push 2: Calculate Bill with Discount")
        print("3. Exit Application")
        
        choice = input("\nSelect an option (1-3): ").strip()
        
        if choice == '1':
            price = get_numeric_input("Enter item price ($): ", float)
            quantity = get_numeric_input("Enter quantity: ", int)
            total = price * quantity
            print(f"\nTotal Bill: ${total:.2f}")
        elif choice == '2':
            print("\nExiting Billing System. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid option. Please select 1, 2, or 3.")
if __name__ == '__main__':
    main()

