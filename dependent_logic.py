import complex_logic

def run_dependency_test():
    """
    Function to test cross-file dependencies.
    It calls functions and uses classes from complex_logic.py.
    """
    print("Testing dependency...")
    
    # Call a function from complex_logic (should link to complex_logic.calculate_factorial)
    result = complex_logic.calculate_factorial(5)
    print(f"Factorial of 5 is {result}")
    
    # Use a class from complex_logic (should link to complex_logic.ResourceManager)
    manager = complex_logic.ResourceManager("dependent.db")
    manager.connect() # Should link to ResourceManager.connect
    manager.save_data("test_key", "test_value") # Should link to ResourceManager.save_data
    
    # Call another function (should link to complex_logic.process_data_stream)
    data = [10, "20", None]
    processed = complex_logic.process_data_stream(data)
    print(f"Processed data: {processed}")

if __name__ == "__main__":
    run_dependency_test()
