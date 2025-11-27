import threading
import time
import random
import os
from pathlib import Path

# Import your module in the same folder
import complex_logic as mod


SHARED_STATE = {"runs": 0, "errors": 0}


def randomized_factorial_calls():
    for _ in range(8):
        n = random.choice([5, 3, -1, "bad", None, 7])
        try:
            if isinstance(n, int):
                print(f"[Thread] factorial({n}) = {mod.calculate_factorial(n)}")
            else:
                raise TypeError("Invalid type for factorial")
        except Exception as e:
            SHARED_STATE["errors"] += 1
            print(f"[Thread] factorial error: {e}")


def file_spam_workflow(manager: mod.ResourceManager):
    test_data = ["10", 2, "xyz", 11, None, 6, "7"]
    processed = mod.process_data_stream(test_data)

    for item in processed:
        try:
            fact = mod.calculate_factorial(item)
            manager.save_data(f"spam_{item}", fact)
        except Exception as e:
            print(f"[FileWorkflow] Process item failed {item}: {e}")
            SHARED_STATE["errors"] += 1


def simulate_disconnect_midway(manager: mod.ResourceManager):
    if random.random() > 0.5:
        manager.connected = False
        print("[Simulate] Forced disconnect!")

    key = f"key_{random.randint(1, 9)}"
    try:
        manager.delete_data(key)
    except Exception as e:
        print(f"[Simulate] delete_data() failure: {e}")
        SHARED_STATE["errors"] += 1


def complex_super_workflow():
    SHARED_STATE["runs"] += 1
    print(f"\n========== Run #{SHARED_STATE['runs']} ==========")

    manager = mod.ResourceManager("super_test.db")
    manager.connect()

    t = threading.Thread(target=randomized_factorial_calls)
    t.start()

    file_spam_workflow(manager)
    simulate_disconnect_midway(manager)

    t.join()

    try:
        mod.complex_workflow()
    except Exception as e:
        print(f"[Main] complex_workflow() failed: {e}")
        SHARED_STATE["errors"] += 1

    print("Cache:", manager.cache)
    print("Shared:", SHARED_STATE)


def create_junk_files():
    base = Path("junk_data")
    base.mkdir(exist_ok=True)

    for i in range(3):
        with open(base / f"junk_{i}.txt", "w") as f:
            f.write(f"junk_{i}:{random.random()}\n")
    print("[Junk] junk files created.")


if __name__ == "__main__":
    create_junk_files()

    for _ in range(3):
        complex_super_workflow()
        time.sleep(0.2)
