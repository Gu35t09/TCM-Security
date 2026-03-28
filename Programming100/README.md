# Python

- Python virtual environment
  collapsed:: true
	- print("""This string runs
	- multiple lines!""")
	- CTRL+SHIFT+p on visual studio, search environment and select Python: create virtual environment
- "#" is used for comment
- print("""This string runs
- multiple lines!""") -> using triple quote you can print multi-line
- you need to indent in some situation (link function)
-
# Best practies
- If we are not running the script directly this script won't work
- if for example we do import scanner.py in another script, the **name** variable would container "scanner"
- if **name** == "**main**":
      main()  
-
- Check the scanner.py for a lot of imformation about socket and threads. It also enlight a lot about printing output and endling error
-
- Pseudocode -> simplified, high-level description of a program or algorithm
- ![image.png](../assets/image_1774710391992_0.png)
- ### Best Practice for Variable Naming:   **snake_case**
	-
	  ```
	  total_amount = 100
	  user_name = "JohnDoe"
	  is_valid = True
	  ```
- **Constants in All Uppercase**:
	- Example:
	    
	  ```
	  MAX_SIZE = 100
	  DEFAULT_TIMEOUT = 30
	  ```
### Type Hinting in Python (Optional Static Typing)
  
  To bridge the gap between static and dynamic typing, Python introduced **type hinting** (since Python 3.5). Type hinting allows you to specify types without enforcing them, providing the best of both worlds: the flexibility of dynamic typing with the clarity of static typing.  
  
#### Example of Type Hinting in Python:
  
  ```
  def atm_withdrawal(balance: float, amount: float) -> float:
    if amount > balance:
        return balance
    return balance - amount
  ```
- The `balance: float` and `amount: float` specify that these parameters are expected to be `float` values, and `-> float` indicates the return type is also a `float`.
- Python doesn’t enforce these types, but using them can improve readability and enable tools like linters or type checkers (e.g., `mypy`) to detect type mismatches before runtime.

### Python Debugging Basics
- The `assert` statement is a simple way to check if something is true. If the condition you’re testing isn’t true, Python will stop the program and give you an error. You can use `assert` to make sure your variables have the correct values while your program is running.
- #### Example:
  
  ```
  def square_number(n):
    result = n * n
    assert result >= 0, "Result should never be negative"
    return result
  
  print(square_number(5))
  ```
  
  In this case, the `assert` checks that the result is never negative. If something goes wrong, Python will raise an error and stop the program.  
  
  **Why is this useful?**: `assert` helps you catch problems early by making sure that certain conditions are always true. This is great for catching mistakes in your code before they cause bigger
  
#### **Basic Debugging with Python's Built-in Debugger (** `<strong>pdb</strong>` **)**
  
  Python comes with a built-in tool called **pdb** that lets you pause your program and step through it line by line. This might sound tricky, but you only need to know a couple of basic commands to get started.  
  
#### Example:
  
  ```
  import pdb
  
  def add_numbers(a, b):
    pdb.set_trace()  # This is where the program will pause
    result = a + b
    return result
  
  print(add_numbers(2, 3))
  ```
  
  When the program reaches `pdb.set_trace()`, it will pause, and you can enter commands to inspect the program.  
  
  Here are some basic commands:  
- `n` (next): Go to the next line of code.
- `p <variable>`: Print the value of a variable (e.g., `p a` to see the value of `a`).
- `c` (continue): Resume running the program.
  
  **Why is this useful?**: Using `pdb` lets you check what’s happening in your program at each step, which makes it easier to find where things go wrong. It’s like pausing a movie to take a closer look at the details.
  
#### **Using Debugging Tools in Your IDE**
  
  If you’re using an IDE like **VSCode** or **PyCharm**, there are built-in tools that make debugging even easier. These tools let you set **breakpoints** (places where the program will pause), inspect variables, and step through the code—just like `pdb`, but with a graphical interface.  
  
  **How to set breakpoints in VSCode**:  
- Open your Python file.
- Click next to the line numbers to add a breakpoint (a red dot will appear).
- Run your program in "debug mode."
- When the program hits the breakpoint, it will pause, and you can inspect what’s happening.
  
  **Why is this useful?**: IDE debugging tools give you a visual way to see what’s going on in your code without needing to use print statements or manually check variables.  
-
