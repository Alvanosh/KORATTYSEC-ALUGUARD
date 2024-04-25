import itertools
import time

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
smallAlpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z']
capitalAlpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z']
specialChars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|',
                '\\', ':', ';', '"', "'", '<', '>', ',', '.', '/', '?']

def generate_passwords(filename, passwordlist, min_length, max_length):
    with open(filename, "w") as file1:
        for length in range(min_length, max_length + 1):
            for password in itertools.product(passwordlist, repeat=length):
                file1.write("".join(map(str, password)) + "\n")
                file1.flush()  # Flush buffer to ensure data is written immediately

def main():

    include_numbers = input("Do you want to include numbers? (1 for yes, 0 for no): ")
    include_smallAlpha = input("Do you want to include small alphabets? (1 for yes, 0 for no): ")
    include_capitalAlpha = input("Do you want to include capital alphabets? (1 for yes, 0 for no): ")
    include_specialChars = input("Do you want to include special characters? (1 for yes, 0 for no): ")

    passwordlist = []
    if include_numbers == '1':
        passwordlist += numbers
    if include_smallAlpha == '1':
        passwordlist += smallAlpha
    if include_capitalAlpha == '1':
        passwordlist += capitalAlpha
    if include_specialChars == '1':
        passwordlist += specialChars

    min_length = int(input("Enter the minimum length of passwords: "))
    max_length = int(input("Enter the maximum length of passwords: "))
    filename = "myfile.txt"

    start_time = time.time()
    generate_passwords(filename, passwordlist, min_length, max_length)
    end_time = time.time()

    print("Time taken: {:.2f} seconds".format(end_time - start_time))
