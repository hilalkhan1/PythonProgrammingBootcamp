"""
Week 7 Project: Custom Decorators
Demonstrates: Decorators, function modification
Decorators: @log_transaction, @timer, @validate_member
"""

import time
from datetime import datetime
from functools import wraps


def log_transaction(func):
    """
    Decorator to log library transactions

    Logs function calls with timestamp and results
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        func_name = func.__name__

        print(f"[LOG {timestamp}] {func_name} called")

        try:
            result = func(*args, **kwargs)
            print(f"[LOG {timestamp}] {func_name} completed: {result[1] if isinstance(result, tuple) else 'Success'}")
            return result
        except Exception as e:
            print(f"[LOG {timestamp}] {func_name} failed: {str(e)}")
            raise

    return wrapper


def timer(func):
    """
    Decorator to measure execution time

    Prints how long the function took to execute
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        elapsed = end_time - start_time
        print(f"⏱ {func.__name__} took {elapsed:.4f} seconds")

        return result

    return wrapper


def validate_member(func):
    """
    Decorator to validate that member exists before operation

    Expects first argument after self to be member_id
    """
    @wraps(func)
    def wrapper(self, member_id, *args, **kwargs):
        if not hasattr(self, 'members') or member_id not in self.members:
            return False, f"Member {member_id} not found"

        return func(self, member_id, *args, **kwargs)

    return wrapper


def validate_book(func):
    """
    Decorator to validate that book exists before operation

    Expects argument 'isbn' in args or kwargs
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        # Try to find ISBN in args or kwargs
        isbn = None

        if len(args) >= 2:
            isbn = args[1]  # Second argument after member_id
        elif 'isbn' in kwargs:
            isbn = kwargs['isbn']

        if isbn and (not hasattr(self, 'books') or isbn not in self.books):
            return False, f"Book {isbn} not found"

        return func(self, *args, **kwargs)

    return wrapper


def cache_results(func):
    """
    Decorator to cache function results

    Useful for expensive operations like statistics
    """
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Create a cache key from arguments
        key = str(args) + str(kwargs)

        if key in cache:
            print(f"📦 Cache hit for {func.__name__}")
            return cache[key]

        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper


def retry(max_attempts=3, delay=1):
    """
    Decorator to retry function on failure

    Args:
        max_attempts: Maximum number of retry attempts
        delay: Delay between retries in seconds
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0

            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        print(f"❌ {func.__name__} failed after {max_attempts} attempts")
                        raise
                    print(f"⚠ {func.__name__} failed (attempt {attempts}/{max_attempts}), retrying in {delay}s...")
                    time.sleep(delay)

        return wrapper

    return decorator


def require_permission(permission_level):
    """
    Decorator to check member permission level

    Args:
        permission_level: Required permission (e.g., "teacher")
    """
    def decorator(func):
        @wraps(func)
        def wrapper(self, member_id, *args, **kwargs):
            if not hasattr(self, 'members') or member_id not in self.members:
                return False, "Member not found"

            member = self.members[member_id]

            # Check permission
            if permission_level == "teacher" and member._member_type != "Teacher":
                return False, "This operation requires teacher privileges"

            return func(self, member_id, *args, **kwargs)

        return wrapper

    return decorator
