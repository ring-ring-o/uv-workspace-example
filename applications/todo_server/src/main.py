from logger import Logger
from fastapi import FastAPI
from libs.usecases.todo.router import todo_router
app = FastAPI()

app.include_router(todo_router)
def main():
    logger = Logger("todo-server")
    logger.info("Hello from todo-server!")
    print("Hello from todo-server!")


if __name__ == "__main__":
    main()
