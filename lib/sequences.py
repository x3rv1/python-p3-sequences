def print_fibonacci(n):
    """
    Prints a list of the Fibonacci sequence up to length n.
    
    Parameters:
    n (int): The number of terms to generate in the sequence.
    """
    if n <= 0:
        print([])  # No terms if n is 0 or negative
        return
    
    # Start with the first two Fibonacci numbers
    sequence = [0, 1]
    
    # Generate the sequence until it reaches length n
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    
    # Trim in case n = 1
    print(sequence[:n])