import threading
from queue import Queue

class MessageProcessor:
    def __init__(self):
        self.queue = Queue()
        self.processed = set()
        self.lock = threading.Lock()  

    def add_message(self, message):
        with self.lock:
            if message not in self.processed:
                self.queue.put(message)
                self.processed.add(message)

    def process_next(self):
        with self.lock:
            if not self.queue.empty():
                message = self.queue.get()
                print(f"Processing message: {message}")
                return message
        return None

def worker(processor, thread_id):
    while True:
        message = processor.process_next()
        if message is None: 
            break
        print(f"Thread-{thread_id} processed: {message}")

if __name__ == "__main__":
    processor = MessageProcessor()

    print("Enter messages one by one. Type 'STOP' to end input.")
   
    while True:
        msg = input("Enter message: ").strip()
        if msg.upper() == "STOP":
            break
        processor.add_message(msg)

    threads = []
    num_threads = int(input("Enter the number of threads to process messages: "))

    for i in range(num_threads):
        thread = threading.Thread(target=worker, args=(processor, i))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

    print("All messages processed.")
