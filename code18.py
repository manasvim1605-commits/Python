def analyze_numbers(numbers):
    if not numbers:
        print("No numbers provided to analyze.")
        return

    print(f"1. Maximum value: {max(numbers)}")
    print(f"2. Minimum value: {min(numbers)}")
    print(f"3. Sum of all values: {sum(numbers)}")
    print(f"4. Average value: {round(sum(numbers) / len(numbers), 2)}")


# Example usage
analyze_numbers([12, 4, 27, 8, 15])