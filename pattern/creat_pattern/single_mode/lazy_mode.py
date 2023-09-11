from threading import Lock


class Lazy:
    _instance = None
    _lock = Lock()

    # 使用多线程中的锁
    @classmethod
    def get_instance_by_lock(cls) -> 'Lazy':
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = Lazy()
        return cls._instance
