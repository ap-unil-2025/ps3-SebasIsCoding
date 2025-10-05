"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
    numbers = []

    while True:
        s = input("Enter numbers and tpye 'done' when you have finish: ").strip() 
        if s.lower() == "done":
            break
        try: 
            numbers.append(float(s))
        except ValueError:
            print("Invalid, enter a number or 'done'")
    return numbers


def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """
    if not numbers:
        return None

    analysis = {}
    count = len(numbers)
    total = sum(numbers)
    average = total/count
    minimum = min(numbers)
    maximum = max(numbers)
    even = sum(1 for x in numbers if float(x).is_integer() and int(x) % 2 == 0)
    odd = sum(1 for x in numbers if float(x).is_integer() and int(x) % 2 != 0)
    # TODO: Count even numbers (hint: use modulo operator)
    # TODO: Count odd numbers
    analysis = {
        "count": count,
        "sum": total,
        "average": average,
        "minimum": minimum,
        "maximum": maximum,
        "even": even,
        "odd": odd,
    }
    return analysis


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:
        return

    print("\nAnalysis Results:")
    print("-" * 20)
    print(f"Count: {analysis['count']}")
    print(f"Sum: {analysis['sum']}")
    print(f"Average: {analysis['average']:.2f}")
    print(f"Minimum: {analysis['minimum']}")
    print(f"Maximum: {analysis['maximum']}")
    print(f"Even numbers: {analysis['even']}")
    print(f"Odd numbers: {analysis['odd']}")


def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()