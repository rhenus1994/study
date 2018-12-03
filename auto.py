import time

start_time = time.time()
print(10)
num = 10
sentinel = 1
while True:
    if time.time() - start_time == sentinel:
        if num - sentinel == 0:
            print('bomb')
            break
        print(num - sentinel)
        sentinel += 1

