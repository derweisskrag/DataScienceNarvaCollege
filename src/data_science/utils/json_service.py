import json
import os
from contextlib import contextmanager
from typing import Union
from types_for_my_app.data import BusSchedule
from types_for_my_app.result import Result, result_wrapper

class JsonService:
    def __init__(self, path: str):
        self.path = path
        self.data: Union[BusSchedule, None] = None

    def __enter__(self):
        if not os.path.exists(self.path):
            with open(self.path, "w", encoding="utf-8") as file:
                json.dump({}, file)  # Create an empty JSON file if missing
        
        try:
            with open(self.path, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError as e:
            self.data = {}
        except json.JSONDecodeError as e:
            raise ValueError("blabla")
        
        return self

    def __exit__(self, exc_type, exc, exc_tb): 
        if exc_type is not None:
            print(f"Error happened okay")

        return False
    
    def save(self):
        with open(self.path, "w") as file:
            json.dump(self.data, file, indent=4)

    def get_data(self):
        return self.data
    
    def update_data(self, key: str, val: str | int):
        self.data[key] = val
        self.save()


@contextmanager
def json_service(path: str):
    """
    A function-based API for JsonService, acting like a controller.
    - Automatically opens and closes the JSON service.
    - Yields only the `.data` dictionary for direct manipulation.
    """
    with JsonService(path) as service:
        yield service.get_data()  # ✅ Expose only the data dict

        # 🔥 After exiting the `with` block, it automatically saves the updated JSON.
        service.save() 