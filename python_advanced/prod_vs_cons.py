import concurrent.futures
import logging
import queue
import random
import threading
import time

# 생산자
def producer():
    ''' 네트워크 대기 상태라 가정(서버)'''
    while not event.is_set():
        message = random.randint(1, 11)
        logging.info('Producer get message : %s', message)
        queue.put(message)
        
    logging.info('Producer receive event : %s', message)

# 소비자
def consumer():
    ''' 응답 받고 소비하는 것으로 가정 or DB 저장'''
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info('Producer receive event : %s (size=%d', message, queue.qsize())

    logging.info('Consumer received event Exiting')


if __name__ == '__main__':
    
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread : before crating and running thread")

    # queue 사이즈
    pipeline = queue.Queue(maxsize=10)
    
    # 이벤트 플래그 초기값 0
    event = threading.Event()
    
    # with context 시작
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as excutor:
        excutor.submit(producer, pipeline, event)
        excutor.submit(consumer, pipeline, event)

        # 실행시간 조정
        time.sleep(0.2)
        
        logging.info("Main : about to set event")
        
        # 이벤트 종료
        event.set()