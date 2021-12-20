import threading
import time
import queue


def thread_fun(name, interval):
    for i in range(11):
        print("I am", name)
        time.sleep(interval)
    print(name, "is done")


def main():
    send_queue = queue.Queue()

    def consumer():
        for _ in range(10):
            value = send_queue.get()
            print(value)
            send_queue.task_done()

    def producer():
        for i in range(10):
            send_queue.put(i)
            time.sleep(2)


    pt1 = threading.Thread(target=consumer)


    pt1.start()
    pt2 = threading.Thread(target=producer)
    pt2.start()


    #pt1.join()
    #pt2.join()

    send_queue.join()
    print("Main is done")

if __name__ == "__main__":
    main()
