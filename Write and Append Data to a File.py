# Python program to write, append, and read a file

# Step 1: Take user input and write it to 'output.txt'
user_input = input("Enter some text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")  # Write input and add newline

# Step 2: Append additional data to the same file
additional_data = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(additional_data + "\n")  # Append input and add newline

# Step 3: Read and display the final content of the file
print("\nFinal content of 'output.txt':")
with open("output.txt", "r") as file:
    for line in file:
        print(line, end='')
