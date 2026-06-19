"""
## 3. Process User Records with Mixed Exceptions  *(Medium)*

=================================================
PROCESS USER RECORDS WITH MIXED EXCEPTIONS
=================================================

Problem Statement:
You are given a LIST of DICTIONARIES, where
each dictionary is supposed to represent a
user record:
        {"name": str, "age": str, "score": str}

The data is messy — some records are missing
keys, some have non-numeric strings, and some
are not even dictionaries.

Write a Python program that processes the
list and returns a TUPLE:
        (clean_records, error_log)

   - clean_records -> list of dicts with
                       "name": str
                       "age":  int
                       "score": float
   - error_log     -> list of tuples:
                       (index, error_class_name,
                        message)

You must demonstrate FOUR exception-handling
techniques:
   1. Catching MULTIPLE exception types in
      ONE except block.
   2. Using `except ... as e` to inspect the
      exception object.
   3. Using `raise` to re-raise an exception
      after logging.
   4. Using `else` to run code only when the
      try block succeeded.

-------------------------------------------------
Instructions:
1. Define a function:
      def process_records(records):
2. Iterate over the list with an index counter.
3. For each record, use a try / except / else
   chain:
      try:
          - access record["name"], record["age"],
            record["score"]   -> may raise
            KeyError or TypeError
          - convert age to int and score to float
            -> may raise ValueError
      except (KeyError, TypeError) as e:
          - record the error with the class name
            from type(e).__name__
      except ValueError as e:
          - record the error with the message
            str(e)
      else:
          - this branch runs ONLY when no
            exception was raised; append the
            cleaned record to clean_records.
4. Write a SECOND function:
      def process_strict(records):
   that calls process_records, and if ANY
   error occurred, RE-RAISES a RuntimeError
   that contains the number of failures.
   Use the bare `raise` keyword inside an
   except block, OR
       raise RuntimeError(...) from None
   to suppress the original traceback chain.
5. Do NOT use:
   - bare `except:`
   - custom exception classes
   - any external library
6. Call both functions and print:
   - the clean_records list
   - the error_log list
   - the message from the RuntimeError
     (catch it with try/except in the driver)

-------------------------------------------------
Debugging Skills to Practice:
- `type(e).__name__` gives the exact exception
  class as a string — useful for log messages.
- Catching multiple exception types in ONE
  except block: `except (KeyError, TypeError):`
  avoids duplicate handler code.
- The `else` block makes the success path
  visually obvious and prevents accidentally
  catching exceptions raised AFTER the risky
  operation.
- When an exception is re-raised, the original
  traceback is preserved. Read it from the
  BOTTOM up: the last line names the exception,
  the lines above show where it came from.

-------------------------------------------------
Input Example:
records = [
   {"name": "Alice", "age": "25",   "score": "88.5"},
   {"name": "Bob",   "age": "abc",  "score": "70"},
   {"name": "Carol", "age": "30"},                       # missing "score"
   "not a dict",                                          # wrong type
   {"name": "Dan",   "age": "40",   "score": "55.5"},
]

Output Example:
Clean Records:
[
  {'name': 'Alice', 'age': 25, 'score': 88.5},
  {'name': 'Dan',   'age': 40, 'score': 55.5}
]
Error Log:
[
  (1, 'ValueError', "invalid literal for int() with base 10: 'abc'"),
  (2, 'KeyError',   'score'),
  (3, 'TypeError',  'string indices must be integers')
]
Strict mode raised: RuntimeError: 3 record(s) failed to process

-------------------------------------------------
Explanation:
- Record at index 1 ("Bob") has a non-numeric
  age, so int("abc") raises ValueError.
- Record at index 2 ("Carol") is missing the
  "score" key, so record["score"] raises
  KeyError.
- Record at index 3 ("not a dict") is a plain
  string, so record["name"] raises TypeError.
- Records at indices 0 and 4 succeed, so the
  `else` block runs and they are appended to
  clean_records.
- The strict version re-raises a RuntimeError
  summarising the total number of failures.
=================================================

"""

def process_records(records):
    """
    Processes a list of raw dictionaries, cleaning the data and logging any errors.
    """
    clean_records = []
    error_log = []

    # Iterate through the list with an index counter
    for index, record in enumerate(records):
        try:
            # Attempt to access keys (raises KeyError if missing, TypeError if record isn't a dict)
            name = record["name"]
            age_str = record["age"]
            score_str = record["score"]

            # Attempt to convert types (raises ValueError if strings aren't numbers)
            age = int(age_str)
            score = float(score_str)

        # Technique 1 & 2: Catching multiple errors at once AND inspecting the error object (e)
        except (KeyError, TypeError) as e:
            error_class = type(e).__name__
            error_log.append((index, error_class, str(e)))

        # Catching the conversion error separately
        except ValueError as e:
            error_class = type(e).__name__
            error_log.append((index, error_class, str(e)))

        # Technique 4: The 'else' block
        # This ONLY runs if the 'try' block finished perfectly without triggering any exceptions
        else:
            clean_records.append({"name": name, "age": age, "score": score})

    return clean_records, error_log


def process_strict(records):
    """
    Calls process_records, but acts strictly by throwing a fatal error if ANY records failed.
    """
    clean_records, error_log = process_records(records)
    
    # Technique 3: Re-raising a fatal error if the log is not empty
    if len(error_log) > 0:
        # We explicitly raise a RuntimeError, detailing the number of failures
        raise RuntimeError(f"{len(error_log)} record(s) failed to process")
        
    return clean_records


# --- Testing the Functions ---

records_list = [
    {"name": "Alice", "age": "25",   "score": "88.5"},
    {"name": "Bob",   "age": "abc",  "score": "70"},          # ValueError: "abc" is not an int
    {"name": "Carol", "age": "30"},                           # KeyError: missing "score"
    "not a dict",                                             # TypeError: string indices must be integers
    {"name": "Dan",   "age": "40",   "score": "55.5"},
]

# 1. Test standard processing
clean_res, errors = process_records(records_list)

print("Clean Records:")
for rec in clean_res:
    print(f"  {rec}")

print("\nError Log:")
for err in errors:
    print(f"  {err}")

print("\n" + "-"*40 + "\n")

# 2. Test strict processing
try:
    process_strict(records_list)
except RuntimeError as e:
    print(f"Strict mode raised: {type(e).__name__}: {str(e)}")