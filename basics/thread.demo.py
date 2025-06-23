from concurrent.futures import ThreadPoolExecutor
import time


def task(name):
    print(f"Task {name} started")
    time.sleep(2)  # Simulate some work
    print(f"Task {name} completed")


def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        for i in range(5):
            executor.submit(task, i)
    print("All tasks completed")


if __name__ == "__main__":
    main()
