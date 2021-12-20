import time

class ExcuteTimer(object):
    def __init__(self, msg):
        self._msg = msg
        
    def __enter__(self):
        self._start = time.monotonic()
        return self._start
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print('Logging exception {}'.format((exc_type, exc_value, exc_traceback)))
        else:
            print('{} : {} s'.format(self._msg, time.monotonic() - self._start))
            
        return True
    
with ExcuteTimer('Start! job') as v:
    print('Received start monotonic1 : {}'.format(v))
    
    # excute job
    for i in range(10000000):
        pass
    raise Exception('Raise! Excpetion!!') # 강제로 발생ㅡ