import logging
from concurrent.futures import ThreadPoolExecutor
import time


def task(name):
    logging.info("Sub-Thread %s: starting", name)

    result = 0

    for i in range(10001):
        result = i + result

    logging.info("Sub-Thread %s : finishing results : %d", name, result)

    return result


def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main-Thread : before crating and running thread")

    # # 실행방법 1
    # # max_workers : 작업의 개수가 넘어가면 직접 설정이 유리
    # excutor = ThreadPoolExecutor(max_workers=3)
    # task1 = excutor.submit(task, ("First",))
    # task2 = excutor.submit(task, ("Second",))

    # print(task1.result())
    # print(task2.result())

    # 실행방법 2
    with ThreadPoolExecutor(max_workers=3) as excutor:
        tasks = excutor.map(task, ["First", "Second"])

        print(list(tasks))


if __name__ == "__main__":
    main()
