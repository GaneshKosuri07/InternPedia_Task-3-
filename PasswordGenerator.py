import secrets
import string
import pyperclip

def generate_password(length, complexity):
    if length < 1:
        raise ValueError("Password length must be at least 1 character.")
    
    char_set = string.ascii_letters
    if complexity > 1:
        char_set += string.digits
    if complexity > 2:
        char_set += string.punctuation

    return ''.join(secrets.choice(char_set) for _ in range(length))

def main():
    try:
        total_passwords = int(input("How many passwords would you like to generate? "))
        length = int(input("Enter the length for each password: "))
        complexity = int(input("Select complexity level (1: letters only, 2: letters + digits, 3: letters + digits + symbols): "))
        
        if complexity not in [1, 2, 3]:
            raise ValueError("Complexity level must be 1, 2, or 3.")
        if total_passwords < 1:
            raise ValueError("You must generate at least one password.")
        
        passwords = [generate_password(length, complexity) for _ in range(total_passwords)]
        
        for index, pwd in enumerate(passwords, start=1):
            print(f"Generated Password {index}: {pwd}")

        try:
            choice = int(input("Enter the number of the password you want to copy to the clipboard (or 0 to skip): "))
            if choice == 0:
                print("No password was copied to the clipboard.")
            elif 1 <= choice <= total_passwords:
                pyperclip.copy(passwords[choice - 1])
                print(f"Password {choice} has been copied to the clipboard.")
            else:
                print("Invalid choice! Please select a valid password number.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
    except ValueError as e:
        print(f"An error occurred: {e}")
        
main()
