"""
## 1. Safe Calculator with try / except  *(Easy)*

=================================================
SAFE CALCULATOR
=================================================

Problem Statement:
Write a Python FUNCTION called `safe_divide`
that takes two values from the user and
performs a division, but never crashes the
program.

Handle the following error cases gracefully:
   - non-numeric input        -> ValueError
   - division by zero         -> ZeroDivisionError
   - any other unexpected bug -> generic Exception

The function must always return a TUPLE:
        (status, value_or_message)
   - status -> "ok" or "error"
   - value_or_message -> the result on success,
                         or an error string on
                         failure.

-------------------------------------------------
Debugging Skills to Practice:
- Read the FULL traceback. The last line of a
  traceback names the exception class — match
  it to your `except`.
- Use a temporary print(type(a), type(b))
  before the division to confirm the inputs.
- Insert breakpoint() and step through with
  the Python debugger (pdb) commands:
       n  -> next line
       s  -> step into
       p  -> print a variable
       q  -> quit

-------------------------------------------------
Input Example 1:
safe_divide("10", "2")

Output Example 1:
('ok', 5.0)
Calculation finished

-------------------------------------------------
Input Example 2:
safe_divide("10", "0")

Output Example 2:
('error', 'Cannot divide by zero')
Calculation finished

-------------------------------------------------
Input Example 3:
safe_divide("ten", "2")

Output Example 3:
('error', 'Inputs must be numbers')
Calculation finished
=================================================

"""

def safe_divide(a, b):
    """
    Attempts to divide two values, gracefully catching crashes and returning a status tuple.
    """
    try:
        num_a = float(a)
        num_b = float(b)
        result = num_a / num_b
        return ("ok", result)
        
    except ValueError:
        return ("error", "Inputs must be numbers")
        
    except ZeroDivisionError:
        return ("error", "Cannot divide by zero")
        
    except Exception as e:
        return ("error", f"An unexpected error occurred: {e}")

print("=== Welcome to the Safe Calculator ===")
print("Type 'q' to quit at any time.\n")

while True:
    # 1. Get the first number
    first_input = input("Enter the first number: ")
    if first_input.lower() == 'q':
        print("Closing calculator...")
        break
        
    # 2. Get the second number
    second_input = input("Enter the number to divide by: ")
    if second_input.lower() == 'q':
        print("Closing calculator...")
        break
        
    # 3. Run the safe_divide function
    # unpack the returned tuple directly into two variables: status and message
    status, message = safe_divide(first_input, second_input)
    
    # 4. Print the formatted result
    print(f"\nStatus: {status.upper()}")
    if status == "ok":
        print(f"Answer: {message}")
    else:
        print(f"Reason: {message}")
        
    print("-" * 35 + "\n")