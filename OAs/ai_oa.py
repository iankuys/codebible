def decode(message_file):
    # Open the file and read the lines
    with open(message_file, 'r') as f:
        lines = f.readlines()

    message = ""
    # Create a dictionary of numbers and words
    num_word_dict = {}
    for line in lines:
        num, word = line.split()
        num_word_dict[int(num)] = word
        
    sorted_keys = sorted(num_word_dict.keys())

    # Find the numbers at the end of each line in the pyramid
    message_nums = []
    for i in range(1, len(sorted_keys)+1):        
        # check if the number is at the end of a line in the pyramid
        # this can be done by checking if the number is a triangular number
        # a triangular number is of the form n * (n + 1) / 2
        # we can use the inverse formula to check if a number is triangular
        # n = (-1 + sqrt(1 + 8 * number)) / 2
        # if n is an integer, then the number is triangular
        n = (-1 + (1 + 8 * i) ** 0.5) / 2
        if n.is_integer():
            # append the word corresponding to the number to the message words list
            message_nums.append(num_word_dict[i])
        

    # join the message words with spaces
    message = ' '.join(message_nums)
    
    return message

print(decode("./coding_qual_input.txt"))