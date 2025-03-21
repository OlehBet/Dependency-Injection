from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass


class ConsoleLogger(Logger):
    def log(self, message: str):
        print(f"[INFO] {message}")


class FileLogger(Logger):
    def log(self, message: str):
        with open("logs.txt", "a") as f:
            f.write(f"[INFO] {message}\n")
