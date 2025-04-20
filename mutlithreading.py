import threading


def printnumbers():
    name1 = threading.current_thread().name
    for i in range(10):
        print(f"{name1}:{i}")


t1 = threading.Thread(target=printnumbers, name="T1")
t2 = threading.Thread(target=printnumbers, name="T2")
t1.start()  # Starting
t2.start()
t1.join()  # Waiting to be finished.
t2.join()
print("Threads completed\n")

global balance
lock = threading.Lock()


def deposit():
    balance = 0
    for _ in range(10000):
        lock.acquire()
        balance += 1
        lock.release()


t1 = threading.Thread(target=deposit)
t2 = threading.Thread(target=deposit)
t1.start()
t2.start()
t1.join()
t2.join()
print(f"Final Balance={balance}\n")


import time


def fetch_api(api_link):
    print(f"Fetching Data from {api_link}")
    time.sleep(3)


apis = ["api1", "api2", "api3"]
threads = []

for api in apis:
    thread = threading.Thread(target=fetch_api, args=(api,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()

print("API fetched!\n")
