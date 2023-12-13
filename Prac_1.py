import multiprocessing
import os

def execute_same_code():
    print(f"Process {os.getpid()} executing same code")

def execute_different_code():
    print(f"Process {os.getpid()} executing different code")

def child_process():
    execute_same_code()

def main():
    print(f"Parent process ID: {os.getpid()}")

    # a) Same program, same code
    process_a = multiprocessing.Process(target=child_process)
    process_a.start()
    process_a.join()

    # b) Same program, different code
    process_b = multiprocessing.Process(target=execute_different_code)
    process_b.start()
    process_b.join()

    print("Parent process finished.")

if __name__ == "__main__":
    main()
