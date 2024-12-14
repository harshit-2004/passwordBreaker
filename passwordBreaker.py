import PyPDF2

def crack_pdf_password(pdf_path, wordlist_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        
        # Load the wordlist
        with open(wordlist_path, 'r') as wordlist:
            passwords = wordlist.readlines()
        
        # Try each password
        for password in passwords:
            password = password.strip()
            try:
                # Attempt to decrypt with the current password
                if reader.decrypt(password):
                    print(f"Password found: {password}")
                    return password
            except Exception as e:
                pass  # Ignore errors and continue
        
        print("Password not found.")
        return None

# Example usage
pdf_path = 'nucleardoc.pdf'
wordlist_path = 'password.txt'
crack_pdf_password(pdf_path, wordlist_path)

# def generate_password_in_range(start, end):
#     """Generate all numeric passwords within the specified range."""
#     passwords = ""  # Initialize an empty string to store the passwords
#     for x in range(start, end + 1):  # Iterate from 'start' to 'end' inclusive
#         passwords += str(x) + '\n'  # Append each password followed by a newline
#     return passwords

# def save_password_to_file(file_path, password):
#     """Save the generated password to a file."""
#     try:
#         with open(file_path, 'w') as file:
#             file.write(password)
#         print(f"Password saved to '{file_path}'.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# start_range = 10000  # Minimum value for the password
# end_range = 99999    # Maximum value for the password
# password = generate_password_in_range(start_range, end_range)
# file_path = "password.txt"

# save_password_to_file(file_path, password)