#Py give username or maill 
#generate password, saves it in onedrive
#show credentials 

import os
import random
import string

# Function to generate a random strong password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function to save credentials to file
def save_credentials(username, password, filename):
    one_drive_path = os.environ.get('OneDrive')
      
    if not one_drive_path:
        raise EnvironmentError("OneDrive path not found in environment variables.")  
    folder_path = os.path.join(one_drive_path, 'Credentials')
    
    # Check if the 'Credentials' directory exists, create it if it doesn't
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
            print(f"Created directory: {folder_path}")
        except Exception as e:
            raise OSError(f"Failed to create directory: {e}")
    
    file_path = os.path.join(folder_path, filename + ".txt")
    
    try:
        with open(file_path, 'w') as file:
            file.write(f'{username}\n')
            file.write(f'{password}\n\n')
        print(f"Credentials saved to {file_path}")
    except Exception as e:
        print(f"Failed to save credentials: {e}")

# Function to display credentials
def display_credentials(username, password):
    print(f"\n\n\nCredenziali:\n")
    print(f"Username: {username}")
    print(f"Password: {password}\n")

# Main function
def main():
    filename = input("Enter the filename to save credentials: ")
    username = input("Enter username or email: ")
    
    pwd_already=''
    while pwd_already !='y' and pwd_already !='n': 
        pwd_already = input("Do you have a password? (y/n): ").lower() 
    
    if pwd_already == 'n':
        length = int(input("Enter desired password length (between 10 and 20): "))
        if length < 10 or length > 20:
            print("Password length must be between 10 and 20 characters.")
            return
        password = generate_password(length)
    elif pwd_already == 'y':
        password = input('Enter password: ')
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        return

    save_credentials(username, password, filename)
    display_credentials(username, password)
    print(f"Credentials have been saved to {filename}.txt in OneDrive folder.")

    input("Press Enter to exit...")  # Keep the console open until Enter is pressed

if __name__ == "__main__":
    main()
