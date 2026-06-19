"""
## 4. File Reader with try / except / else / finally  *(Medium)*

=================================================
FILE READER WITH FULL TRY BLOCK
=================================================

Problem Statement:
Write a Python FUNCTION called `read_numbers`
that reads a text file containing ONE number
per line and returns the SUM of those numbers.

The function must demonstrate ALL FOUR parts
of Python's exception model:
        try / except / else / finally.

Error cases to handle:
   - FileNotFoundError  -> file path is wrong
   - PermissionError    -> file cannot be read
   - ValueError         -> a line is not a number
   - any other Exception

The function returns a TUPLE:
        (status, value_or_message, lines_read)
   - status            -> "ok" or "error"
   - value_or_message  -> the total sum or
                          the error message
   - lines_read        -> number of lines
                          successfully parsed
                          before any error.

-------------------------------------------------
Instructions:
1. Define:
      def read_numbers(path):
2. Layout the try block as follows:
      try:
          open the file
          read lines and convert each to float
      except FileNotFoundError:
          ...
      except PermissionError:
          ...
      except ValueError:
          ...
      except Exception as e:
          ...
      else:
          this block ONLY runs if no exception
          was raised. Use it for the success
          path (e.g. compute the final sum).
      finally:
          this block ALWAYS runs. Use it to
          close the file if it was opened, or
          to print "Done reading".
3. Use a `with open(path) as f:` block, which
   already closes the file automatically.
4. Do NOT use:
   - bare `except:`
   - `os.path.exists()` to AVOID the
     FileNotFoundError. Let the exception be
     raised and handle it.

-------------------------------------------------
Debugging Skills to Practice:
- The four-part structure makes the intent of
  each block obvious:
        try     -> code that might fail
        except  -> what to do when it fails
        else    -> what to do when it does NOT fail
        finally -> cleanup that runs no matter what
- When the program behaves oddly, ask "which
  block is actually running?". Add a quick
  `print("entered else")` etc. to find out.
- For file errors, print `path` and
  `os.getcwd()` to confirm where Python is
  looking.

-------------------------------------------------
Input Example 1:
A file numbers.txt containing:
   10
   20
   30

read_numbers("numbers.txt")

Output Example 1:
('ok', 60.0, 3)
Done reading

-------------------------------------------------
Input Example 2:
read_numbers("missing.txt")

Output Example 2:
('error', 'File not found: missing.txt', 0)
Done reading

-------------------------------------------------
Input Example 3:
A file bad.txt containing:
   10
   abc
   30

read_numbers("bad.txt")

Output Example 3:
('error', 'Invalid number on a line', 1)
Done reading

-------------------------------------------------
Explanation:
- In example 1 every line parses, the `else`
  block computes the sum 60.0, and `finally`
  prints "Done reading".
- In example 2 the file does not exist; the
  FileNotFoundError branch runs, then
  `finally` still prints "Done reading".
- In example 3 the first line parses fine
  (lines_read becomes 1), then "abc" raises
  ValueError, which is caught and reported.
=================================================

"""
import os

# --- Setup: Creating temporary test files so you have something to read! ---
with open("numbers.txt", "w") as f:
    f.write("10\n20\n30\n")

with open("bad.txt", "w") as f:
    f.write("10\nabc\n30\n")
# -------------------------------------------------------------------------

def read_numbers(path):
    """
    Reads numbers from a file, demonstrating the full try/except/else/finally structure.
    """
    lines_read = 0
    total_sum = 0.0
    
    try:
        with open(path, 'r') as f:
            for line in f:
                cleaned_line = line.strip()
                if cleaned_line:
                    number = float(cleaned_line)
                    total_sum += number
                    lines_read += 1
                    
    except FileNotFoundError:
        return ("error", f"File not found: {path}", lines_read)
        
    except PermissionError:
        return ("error", f"Permission denied to read: {path}", lines_read)
        
    except ValueError:
        return ("error", "Invalid number on a line", lines_read)
        
    except Exception as e:
        return ("error", f"Unexpected error: {str(e)}", lines_read)
        
    else:
        return ("ok", total_sum, lines_read)
        
    finally:
        # I updated this print statement so you can see exactly when the finally block triggers
        print(f"[System: Finished attempting to read '{path}']")


# --- Interactive User Input ---

print("=== Welcome to the Safe File Reader ===")
print("Available test files: 'numbers.txt', 'bad.txt', or type 'missing.txt' to see it fail.")
print("Type 'q' to quit at any time.\n")

while True:
    # Ask the user for a filename
    user_file = input("Enter the name of the file to read: ")
    
    # Escape hatch
    if user_file.lower() == 'q':
        print("Closing file reader...")
        break
        
    # Run the function and unpack all THREE items from the tuple
    status, message, lines = read_numbers(user_file)
    
    # Print the formatted result based on the status
    if status == "ok":
        print(f"✅ SUCCESS: The total sum is {message}")
        print(f"   (Successfully read {lines} valid lines)")
    else:
        print(f"❌ ERROR: {message}")
        print(f"   (Failed after reading {lines} valid lines)")
        
    print("-" * 45 + "\n")

# --- Cleanup: Removing the temporary files when the program ends ---
if os.path.exists("numbers.txt"): os.remove("numbers.txt")
if os.path.exists("bad.txt"): os.remove("bad.txt")