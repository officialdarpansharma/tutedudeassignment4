
# Python program to read a file and print its content line by line

try:
    # Open the file in read mode
    with open("sample.txt", "r") as file:
        # Read and print each line
        for line in file:
            print(line, end='')  # end='' avoids adding extra newlines
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
