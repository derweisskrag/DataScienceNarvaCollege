from typing import Callable, Union
from functools import wraps

class Result[T, E]:
    def __init__(self, value: Union[T, None] = None, error: Union[T, None] = None):
        self.value = value
        self.error = error

    def is_ok(self) -> bool:
        return self.error is None
    
    def is_err(self) -> bool:
        return self.error is not None
    
    def unwrap(self) -> T:
        if self.error:
            raise self.error
        return self.value
    
    def unwrap_or(self, default_value: T) -> T:
        return self.value if self.is_ok() else default_value
    
    def __repr__(self):
        return f"Ok({self.value})" if self.is_ok() else f"Err({self.error})"
    

def result_wrapper[T, E](func: Callable[..., T]) -> Callable[..., Result[T, E]]:
    @wraps(func)
    def wrapper(*args, **kws):
        try:
            return Result(value=func(*args, **kws))
        except Exception as e:
            return Result(error=e)
    return wrapper
