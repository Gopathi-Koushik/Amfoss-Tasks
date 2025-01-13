def count_digit_frequencies(S):
    # Initialize a list to hold the frequency of digits 0 to 9
    freq = [0] * 10

    for char in S:
        # Check if the character is a digit
        if char.isdigit():
            freq[int(char)] += 1
    
    print(" ".join(map(str, freq)))


S = raw_input()  
count_digit_frequencies(S)

