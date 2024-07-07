def celsius_to_fahrenheit(celsius):
    return 9.0 / 5.0 * celsius + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0

def main():
    print("Howdy, I'm Prabindh")
    
    # Displaying options
    print("\nSelect an option for temperature conversion:")
    print("A. Celsius to Fahrenheit")
    print("B. Fahrenheit to Celsius")

    option = input("\nEnter your option (A/B): ").strip().lower()

    if option == 'a':
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Temperature: {celsius:.2f} Celsius = {fahrenheit:.2f} Fahrenheit")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
    
    elif option == 'b':
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Temperature: {fahrenheit:.2f} Fahrenheit = {celsius:.2f} Celsius")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
    
    else:
        print("Invalid option selected. Please choose A or B.")

if __name__ == "__main__":
    main()
