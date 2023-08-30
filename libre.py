def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    
    while len(fibonacci_sequence) < n:
        next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_num)
    
    return fibonacci_sequence

def calculate_squares(sequence):
    return [num ** 2 for num in sequence]

def main():
    num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
    
    if num_terms <= 0:
        print("Number of terms must be greater than zero.")
        return
    
    fibonacci_sequence = generate_fibonacci(num_terms)
    squared_sequence = calculate_squares(fibonacci_sequence)
    
    print("Generated Fibonacci sequence:", fibonacci_sequence)
    print("Squares of Fibonacci sequence:", squared_sequence)

if __name__ == "__main__":
    main()
