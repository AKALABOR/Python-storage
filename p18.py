import threading
import time
import random

def countdown():
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)
    print("Відлік завершено")

def simulate_download(file_id):
    duration = random.randint(3, 5)
    time.sleep(duration)
    print(f"Завантаження {file_id} завершено")

def sum_part(numbers, result, index):
    result[index] = sum(numbers)

if __name__ == "__main__":
    t1 = threading.Thread(target=countdown)
    t1.start()

    threads = []
    for i in range(1, 4):
        t = threading.Thread(target=simulate_download, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    numbers = [random.randint(1, 100) for _ in range(1000)]
    chunk_size = len(numbers) // 4
    results = [0]*4
    threads = []

    for i in range(4):
        part = numbers[i*chunk_size:(i+1)*chunk_size] if i < 3 else numbers[i*chunk_size:]
        t = threading.Thread(target=sum_part, args=(part, results, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(sum(results))
    t1.join()
