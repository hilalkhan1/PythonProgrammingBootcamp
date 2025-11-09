"""
Week 3: Variable Scope Examples
Topics: Local, global, nonlocal scope
"""

# Global variable
global_var = "I am global"

def demonstrate_scope():
    # Local variable
    local_var = "I am local"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")

print("=== Variable Scope ===")
demonstrate_scope()
print(f"Outside function - Global: {global_var}")
# print(local_var)  # This would cause an error

# Modifying global variable
counter = 0

def increment_global():
    global counter
    counter += 1
    print(f"Counter inside function: {counter}")

print("\n=== Global Keyword ===")
print(f"Counter before: {counter}")
increment_global()
increment_global()
print(f"Counter after: {counter}")

# Nonlocal scope
def outer_function():
    x = "outer"

    def inner_function():
        nonlocal x
        x = "inner"
        print(f"Inside inner: x = {x}")

    print(f"Before inner: x = {x}")
    inner_function()
    print(f"After inner: x = {x}")

print("\n=== Nonlocal Keyword ===")
outer_function()

# LEGB Rule (Local, Enclosing, Global, Built-in)
x = "global x"

def outer():
    x = "outer x"

    def inner():
        x = "inner x"
        print(f"Inner: {x}")

    inner()
    print(f"Outer: {x}")

print("\n=== LEGB Rule ===")
outer()
print(f"Global: {x}")
