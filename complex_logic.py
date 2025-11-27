import os
import random
import math

# Global state to test 'modifies_globals' and 'mutates_state'
GLOBAL_COUNTER = 0

class ResourceManager:
    """
    A class to test state mutation and I/O side effects.
    """
    def __init__(self, db_path):
        self.db_path = db_path
        self.connected = False
        self.cache = {}

    def connect(self):
        """
        Simulates I/O and state mutation.
        """
        print(f"Connecting to {self.db_path}...") # performs_io (print)
        self.connected = True # mutates_state (attribute)
        global GLOBAL_COUNTER
        GLOBAL_COUNTER += 1 # modifies_globals

    def save_data(self, key, value):
        """
        Simulates I/O and potential exceptions.
        """
        if not self.connected:
            raise ConnectionError("Not connected to DB") # raises_exceptions
        
        # performs_io (file write)
        with open(self.db_path, 'a') as f:
            f.write(f"{key}:{value}\n")
        
        self.cache[key] = value # mutates_state

    def delete_data(self, key):
        """
        Simulates deleting data.
        """
        if not self.connected:
            raise ConnectionError("Not connected to DB")
        
        if key in self.cache:
            del self.cache[key] # mutates_state
            print(f"Deleted {key}") # performs_io

def calculate_factorial(n):
    """
    Pure computation function (mostly).
    """
    if n < 0:
        raise ValueError("Negative input") # raises_exceptions
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)

def process_data_stream(data_list):
    """
    Complex control flow and data transformation.
    """
    results = []
    for item in data_list: # Loop
        if item is None: # Branch
            continue
        
        if isinstance(item, int):
            if item % 2 == 0: # Nested branch
                results.append(item * 2)
            else:
                results.append(item + 1)
        elif isinstance(item, str):
            try:
                val = int(item)
                results.append(val)
            except ValueError: # Exception handling
                pass
    return results

def complex_workflow():
    """
    Orchestrator function to test call graph linking.
    """
    manager = ResourceManager("test.db")
    manager.connect() # Calls connect
    
    data = [1, 2, "3", "four", 5]
    processed = process_data_stream(data) # Calls process_data_stream
    
    for val in processed:
        try:
            fact = calculate_factorial(val) # Calls calculate_factorial
            manager.save_data(f"fact_{val}", fact) # Calls save_data
        except Exception as e:
            print(f"Error processing {val}: {e}")

if __name__ == "__main__":
    complex_workflow()
