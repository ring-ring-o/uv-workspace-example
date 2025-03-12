class Logger:
    def __init__(self, name: str):
        self.name = name

    def info(self, message: str):
        print(f"[{self.name}] {message}")

