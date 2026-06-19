"""
## 2. Safe List Access  *(Easy)*

=================================================
SAFE LIST ACCESS
=================================================

Problem Statement:
Write a Python FUNCTION called `safe_get`
that takes a list and an index, and returns
the value at that index WITHOUT crashing the
program when the index is invalid.

The function must return a TUPLE:
        (status, value_or_message)
   - status -> "ok" or "error"
   - value_or_message -> the value on success,
                         or an error string on
                         failure.

Handle these error cases:
   - IndexError      -> "Index out of range"
   - TypeError       -> "Index must be an int"
   - other Exception -> "Unexpected error: ..."

-------------------------------------------------
Instructions:
1. Define a function:
      def safe_get(items, index):
2. Use a try block that returns items[index].
3. Add a separate `except` block for each
   expected exception in the correct order
   (most specific first).
4. Add a final `except Exception as e:` block
   that includes str(e) in the error message.
5. Do NOT use:
   - the `in` operator to guess validity
     beforehand
   - if-checks like `if 0 <= index < len(items)`
     to AVOID the exception.
   The whole point is to LET the exception be
   raised and HANDLE it.

-------------------------------------------------
Debugging Skills to Practice:
- Use print(repr(index), type(index)) when the
  function misbehaves; `repr` shows quotes
  around strings so you can tell "3" from 3.
- Read the exception MESSAGE — IndexError on a
  list of length 5 tells you the index that
  was rejected.
- Try `import traceback; traceback.print_exc()`
  inside the except block to print the full
  traceback while still handling the error.

-------------------------------------------------
Input Example 1:
safe_get([10, 20, 30, 40], 2)

Output Example 1:
('ok', 30)

-------------------------------------------------
Input Example 2:
safe_get([10, 20, 30], 7)

Output Example 2:
('error', 'Index out of range')

-------------------------------------------------
Input Example 3:
safe_get([10, 20, 30], "1")

Output Example 3:
('error', 'Index must be an int')

=================================================

"""

def safe_get(items, index):
    """
    Attempts to retrieve a value from a list at a specific index, 
    gracefully handling out-of-bounds or invalid index types.
    """
    try:
        # We go straight for the retrieval. If it fails, Python jumps to the except blocks.
        value = items[index]
        return ("ok", value)
        
    except IndexError:
        # Caught the error when the index is a number, but too large/small for the list
        return ("error", "Index out of range")
        
    except TypeError:
        # Caught the error when the index isn't an integer (like a string or float)
        return ("error", "Index must be an int")
        
    except Exception as e:
        # Catch-all for any other weird bugs we didn't foresee
        return ("error", f"Unexpected error: {str(e)}")


# --- Testing the Function ---

print("Input Example 1:")
result1 = safe_get([10, 20, 30, 40], 2)
print(result1)

print("\nInput Example 2:")
result2 = safe_get([10, 20, 30], 7)
print(result2)

print("\nInput Example 3:")
result3 = safe_get([10, 20, 30], "1")
print(result3)