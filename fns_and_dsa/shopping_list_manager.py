def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
        elif choice == '2':
            remove = int(input("Please enter the position of the item you want to remove(starting from 0): "))
            shopping_list.pop(remove)
            print(f"The index: {remove} has been succesfully removed")
        elif choice == '3':
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()