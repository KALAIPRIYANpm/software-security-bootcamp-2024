import time
from functools import wraps
from collections import deque

def rate_limit(max_requests, window_seconds):
    """
    A decorator for rate limiting using the sliding window algorithm.

    :param max_requests: int - Maximum number of requests allowed within the window
    :param window_seconds: int - Time window in seconds
    :return: decorator function
    """
    def decorator(func):
        user_access_logs = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            user_identifier = args[0]  
            current_time = time.time()

            if user_identifier not in user_access_logs:
                user_access_logs[user_identifier] = deque()

            access_log = user_access_logs[user_identifier]
            while access_log and access_log[0] < current_time - window_seconds:
                access_log.popleft()

            if len(access_log) < max_requests:
                access_log.append(current_time)
                return func(*args, **kwargs)
            else:
                return {"error": "Rate limit exceeded"}

        return wrapper

    return decorator

@rate_limit(max_requests=5, window_seconds=60)
def login_attempt(username, password):
    return {"success": True}


if __name__ == "__main__":
    test_user = "user1"

    print("Time 0:00 -", login_attempt(test_user, "pass1"))  
    time.sleep(10)  
    print("Time 0:10 -", login_attempt(test_user, "pass2"))  
    time.sleep(10)
    print("Time 0:20 -", login_attempt(test_user, "pass3"))  
    time.sleep(10)
    print("Time 0:30 -", login_attempt(test_user, "pass4"))  
    time.sleep(10)
    print("Time 0:40 -", login_attempt(test_user, "pass5"))  
    time.sleep(10)
    print("Time 0:50 -", login_attempt(test_user, "pass6"))  
