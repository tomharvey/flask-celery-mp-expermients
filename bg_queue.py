from multiprocessing import Queue, Process

def handle_queue(queue):
    BATCH_SIZE = 3
    batch = []
    while True:
        msg = queue.get()
        batch.append(msg)
        if len(batch) >= BATCH_SIZE:
            print(batch)
            batch = []


def start_q_handler():
    queue = Queue()
    q_handler = Process(target=handle_queue, args=((queue),))
    q_handler.daemon = True
    q_handler.start()
    return queue
