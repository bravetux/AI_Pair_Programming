import time
import string
from collections import Counter

# --- All Function Definitions ---

def print_factors(n):
    """Print all the factors of a given number n."""
    if n <= 0:
        print("Please enter a positive integer.")
        return
    factors = [i for i in range(1, n + 1) if n % i == 0]
    print(f"Factors of {n}: {factors}")

def compare_strings(s1, s2):
    """Print if the two given strings are equal or unequal."""
    print("Equal" if s1 == s2 else "Unequal")

def char_frequency(s, ch):
    """Print the frequency of the given character in the given string."""
    print(f"Frequency of '{ch}' in '{s}': {s.count(ch)}")

def count_vowels(s):
    """Print the number of vowels in the given string."""
    vowels = 'aeiouAEIOU'
    count = sum(1 for c in s if c in vowels)
    print(f"Number of vowels in '{s}': {count}")

def print_divisible_in_range(start, end, divisor):
    """Print all the numbers divisible by a given number in the range [start, end]."""
    if divisor == 0:
        print("Divisor cannot be zero.")
        return
    divisible_nums = [i for i in range(start, end + 1) if i % divisor == 0]
    print(f"Numbers divisible by {divisor} in range [{start}, {end}]: {divisible_nums}")

def factorial_recursive(n):
    """Find the factorial of a number with recursion."""
    if n < 0:
        return "Factorial not defined for negative numbers"
    return 1 if n == 0 else n * factorial_recursive(n - 1)

def factorial_iterative(n):
    """Find the factorial of a number without recursion."""
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci_recursive_helper(k):
    """Helper for recursive fibonacci to return a value."""
    return k if k <= 1 else fibonacci_recursive_helper(k - 1) + fibonacci_recursive_helper(k - 2)

def fibonacci_recursive(n):
    """Display the Fibonacci series up to n terms with recursion."""
    if n <= 0:
        print("Please enter a positive number of terms.")
        return
    # Note: This is very inefficient for larger n
    print([fibonacci_recursive_helper(i) for i in range(n)])

def fibonacci_iterative(n):
    """Display the Fibonacci series up to n terms without recursion."""
    if n <= 0:
        print("Please enter a positive number of terms.")
        return
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    print(seq)

def welcome_if_in_list(name, name_list):
    """Print 'Welcome' if name is in the list, 'See you next time' otherwise."""
    print("Welcome" if name in name_list else "See you next time")

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    """Print the list of prime numbers in the given range."""
    prime_list = [i for i in range(max(2, start), end + 1) if is_prime(i)]
    print(f"Primes in range [{start}, {end}]: {prime_list}")

def is_perfect(n):
    """Check if a number is a perfect number."""
    if n < 1:
        return False
    # A perfect number's sum of proper divisors equals the number itself.
    return n == sum(i for i in range(1, n) if n % i == 0)

def perfect_numbers_in_range(start, end):
    """Print the list of perfect numbers in the given range."""
    perfect_list = [i for i in range(start, end + 1) if is_perfect(i)]
    print(f"Perfect numbers in range [{start}, {end}]: {perfect_list}")

def is_palindrome_number(n):
    """Check if a number is a palindrome."""
    return str(n) == str(n)[::-1]

def is_pangram(sentence):
    """Check if a sentence is a pangram (contains every letter of the alphabet)."""
    return set(string.ascii_lowercase).issubset(set(sentence.lower()))

def is_anagram(s1, s2):
    """Check if two strings are anagrams."""
    return Counter(s1.replace(' ', '').lower()) == Counter(s2.replace(' ', '').lower())

def char_frequency_all(s):
    """Print the frequency of each character in a string."""
    freq = Counter(s)
    print("Character frequencies:")
    for ch, count in freq.items():
        print(f"'{ch}': {count}")

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    s = str(n)
    order = len(s)
    return n == sum(int(digit)**order for digit in s)

def armstrong_numbers_in_range(start, end):
    """Print all Armstrong numbers in a given range."""
    armstrong_list = [i for i in range(start, end + 1) if is_armstrong(i)]
    print(f"Armstrong numbers in range [{start}, {end}]: {armstrong_list}")

def sieve_of_eratosthenes(n):
    """Print all primes up to n using the Sieve of Eratosthenes algorithm."""
    if n < 2:
        print("No primes in this range.")
        return
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    primes = [i for i, is_p in enumerate(sieve) if is_p]
    print(f"Primes up to {n}: {primes}")

def fast_primes_in_range(start, end):
    """Improve the timing of prime number printing using a pre-computed sieve."""
    if end < 2:
        print("No primes in this range.")
        return
    sieve = [True] * (end + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(end**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, end + 1, i):
                sieve[j] = False
    primes = [i for i in range(max(2, start), end + 1) if sieve[i]]
    print(f"Primes in range [{start}, {end}] (fast): {primes}")

def word_frequency(sentence):
    """Print the frequency of words in a sentence."""
    words = sentence.split()
    freq = Counter(words)
    print("Word frequencies:")
    for word, count in freq.items():
        print(f"'{word}': {count}")

def reverse_each_word(sentence):
    """Reverse each word in a sentence."""
    reversed_sentence = ' '.join(word[::-1] for word in sentence.split())
    print(f"Reversed words: {reversed_sentence}")

def is_strong_password(password):
    """Check if a password is strong (has upper, lower, digit, special char)."""
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    if has_upper and has_lower and has_digit and has_special:
        print("Password is strong.")
    else:
        print("Password is weak. It must contain an uppercase letter, a lowercase letter, a digit, and a special character.")

def atoi(s):
    """Convert a string to an integer, handling errors."""
    try:
        print(f"Integer value: {int(s)}")
    except ValueError:
        print("Invalid integer string.")

# --- Main Program Logic ---

def main():
    """Main function to run the menu-driven program."""
    menu = [
        "Print all the factors of a given number",
        "Print if the two given strings are equal or unequal",
        "Print the frequency of the given character in the given string",
        "Print the number of vowels in the given string",
        "Print all the numbers divisible by a given number in the range",
        "Find the factorial of a number with recursion",
        "Find the factorial of a number without recursion",
        "Display the Fibonacci series with recursion",
        "Display the Fibonacci series without recursion",
        "Print 'Welcome' if your name is present in the list",
        "Find if the given number is a prime",
        "Print the list of prime numbers in the given range",
        "Find if the given number is a perfect number",
        "Print the list of perfect numbers in the given range",
        "Find if the given number is a palindrome number",
        "Find if the given sentence is a pangram",
        "Find if the two given strings are anagrams of each other",
        "Print the frequency of each character in the given string",
        "Find if the given number is an Armstrong number",
        "Print all the Armstrong numbers in the given range",
        "Print all the primes in the given range using Sieve of Eratosthenes",
        "Improve the timing of the prime number printing program",
        "Find the frequency of the words in the given sentence",
        "Reverse each word separately in the given sentence",
        "Check if the password is strong (capital, number, small, special)",
        "Convert the given string to a number (atoi)",
        "Exit"
    ]

    print("\nWelcome to the Python Programs Menu!")
    try:
        while True:
            print("\n" + "="*15 + " MENU " + "="*15)
            for i, item in enumerate(menu, 1):
                print(f"{i}. {item}")
            print("="*36)

            try:
                choice_str = input("Enter your choice (1-27): ")
                if not choice_str:
                    continue  # Handle empty input
                choice = int(choice_str)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == 1:
                n = int(input("Enter a positive number: "))
                print_factors(n)
                input("Press Enter to continue...")
            elif choice == 2:
                s1 = input("Enter first string: ")
                s2 = input("Enter second string: ")
                compare_strings(s1, s2)
                input("Press Enter to continue...")
            elif choice == 3:
                s = input("Enter the string: ")
                ch = input("Enter the character to count: ")
                char_frequency(s, ch)
                input("Press Enter to continue...")
            elif choice == 4:
                s = input("Enter the string: ")
                count_vowels(s)
                input("Press Enter to continue...")
            elif choice == 5:
                start = int(input("Enter start of range: "))
                end = int(input("Enter end of range: "))
                divisor = int(input("Enter the divisor: "))
                print_divisible_in_range(start, end, divisor)
                input("Press Enter to continue...")
            elif choice == 6:
                n = int(input("Enter a non-negative number: "))
                start_time = time.perf_counter()
                result = factorial_recursive(n)
                elapsed = time.perf_counter() - start_time
                print(f"Factorial (recursive): {result}")
                print(f"Time taken: {elapsed:.6f} seconds")
                input("Press Enter to continue...")
            elif choice == 7:
                n = int(input("Enter a non-negative number: "))
                start_time = time.perf_counter()
                result = factorial_iterative(n)
                elapsed = time.perf_counter() - start_time
                print(f"Factorial (iterative): {result}")
                print(f"Time taken: {elapsed:.6f} seconds")
                input("Press Enter to continue...")
            elif choice == 8:
                n = int(input("Enter number of terms: "))
                print("Fibonacci (recursive):", end=' ')
                start_time = time.perf_counter()
                fibonacci_recursive(n)
                elapsed = time.perf_counter() - start_time
                print(f"Time taken: {elapsed:.6f} seconds")
                input("Press Enter to continue...")
            elif choice == 9:
                n = int(input("Enter number of terms: "))
                print("Fibonacci (iterative):", end=' ')
                start_time = time.perf_counter()
                fibonacci_iterative(n)
                elapsed = time.perf_counter() - start_time
                print(f"Time taken: {elapsed:.6f} seconds")
                input("Press Enter to continue...")
            elif choice == 10:
                name = input("Enter your name: ")
                name_list_str = input("Enter a comma-separated list of names: ")
                name_list = [x.strip() for x in name_list_str.split(',')]
                welcome_if_in_list(name.strip(), name_list)
                input("Press Enter to continue...")
            elif choice == 11:
                n = int(input("Enter number: "))
                start_time = time.perf_counter()
                print(f"Is it prime? {is_prime(n)}")
                elapsed = time.perf_counter() - start_time
                print(f"Time taken: {elapsed:.6f} seconds")
                input("Press Enter to continue...")
            elif choice == 12:
                start = int(input("Enter start of range: "))
                end = int(input("Enter end of range: "))
                start_time = time.perf_counter()
                primes_in_range(start, end)
                elapsed = time.perf_counter() - start_time
                print(f"Time taken: {elapsed:.6f} seconds")
                input("Press Enter to continue...")
            elif choice == 13:
                n = int(input("Enter number: "))
                print(f"Is it perfect? {is_perfect(n)}")
                input("Press Enter to continue...")
            elif choice == 14:
                start = int(input("Enter start of range: "))
                end = int(input("Enter end of range: "))
                perfect_numbers_in_range(start, end)
                input("Press Enter to continue...")
            elif choice == 15:
                num_str = input("Enter number: ")
                try:
                    n = int(num_str)
                    print(f"Is it a palindrome? {is_palindrome_number(n)}")
                except ValueError:
                    print("Invalid number.")
                input("Press Enter to continue...")
            elif choice == 16:
                s = input("Enter sentence: ")
                print(f"Is it a pangram? {is_pangram(s)}")
                input("Press Enter to continue...")
            elif choice == 17:
                s1 = input("Enter first string: ")
                s2 = input("Enter second string: ")
                print(f"Are they anagrams? {is_anagram(s1, s2)}")
                input("Press Enter to continue...")
            elif choice == 18:
                s = input("Enter string: ")
                char_frequency_all(s)
                input("Press Enter to continue...")
            elif choice == 19:
                n = int(input("Enter number: "))
                print(f"Is it an Armstrong number? {is_armstrong(n)}")
                input("Press Enter to continue...")
            elif choice == 20:
                start = int(input("Enter start of range: "))
                end = int(input("Enter end of range: "))
                armstrong_numbers_in_range(start, end)
                input("Press Enter to continue...")
            elif choice == 21:
                n = int(input("Enter upper limit for Sieve: "))
                start_time = time.perf_counter()
                sieve_of_eratosthenes(n)
                elapsed = time.perf_counter() - start_time
                print(f"Time taken: {elapsed:.6f} seconds")
                input("Press Enter to continue...")
            elif choice == 22:
                start = int(input("Enter start of range: "))
                end = int(input("Enter end of range: "))
                start_time = time.perf_counter()
                # Use Sieve of Eratosthenes for the full range for fastest prime determination
                if end < 2 or start > end:
                    print("No primes in this range.")
                else:
                    sieve = [True] * (end + 1)
                    sieve[0:2] = [False, False]
                    for i in range(2, int(end ** 0.5) + 1):
                        if sieve[i]:
                            for j in range(i * i, end + 1, i):
                                sieve[j] = False
                    primes = [i for i in range(max(2, start), end + 1) if sieve[i]]
                    print(f"Primes in range [{start}, {end}] (fastest): {primes}")
                elapsed = time.perf_counter() - start_time
                print(f"Time taken: {elapsed:.6f} seconds")
                input("Press Enter to continue...")
            elif choice == 23:
                s = input("Enter sentence: ")
                word_frequency(s)
                input("Press Enter to continue...")
            elif choice == 24:
                s = input("Enter sentence: ")
                reverse_each_word(s)
                input("Press Enter to continue...")
            elif choice == 25:
                password = input("Enter password: ")
                is_strong_password(password)
                input("Press Enter to continue...")
            elif choice == 26:
                s = input("Enter string to convert to integer: ")
                atoi(s)
                input("Press Enter to continue...")
            elif choice == 27:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 27.")
                input("Press Enter to continue...")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")

if __name__ == "__main__":
    main()