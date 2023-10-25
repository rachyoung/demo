# Rachel Young

# returns a string with digits 3 larger than the corresponding digit of nums
def encode(nums):
    result = ""
    for char in nums:
        result += str(3 + int(char))
    return result

def main():
    user_choice = 0
    plain = 0
    encoded = 0
    while user_choice != 3:
        # print menu
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        # get user input
        user_choice = int(input("Please enter an option: "))

        if user_choice == 1:  # get string and encode it
            plain = input("Please enter your password to encode: ")
            encoded = encode(plain)
            print("Your password has been encoded and stored!")
        elif user_choice == 2:  # print decoded string
            print()
            # print(f"The encoded password is {encoded}, and the original password is {decode(encoded)}.")
        elif user_choice == 3:  # quit
            return


if __name__ == "__main__":
    main()