import time

timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5minutes

while True:
    # Every 5 seconds:
    if time.time() > timeout:
        print(time.time())
        print(timeout)
        timeout = time.time() + 10