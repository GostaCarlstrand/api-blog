import threading
import time


def counter(name, count):
    while count < 10:
        count += 1
        print(name + "counts" + str(count))
        time.sleep(2)
    print(name + "is done")


def create_thread(thread):
    thread = threading.Thread(target=counter, args=("Thread 2", 1))
    thread.start()


def main():
    create_thread(threading.Thread)


if __name__ == "__main__":
    main()
