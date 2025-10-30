from abc import ABC, abstractmethod


class ILogger(ABC):
    @abstractmethod
    def log(self, message):
        pass



class FileLogger(ILogger):
    def log(self, message):
        print(f" Logging to File: {message}")


class DatabaseLogger(ILogger):
    def log(self, message):
        print(f" Logging to Database: {message}")


class ConsoleLogger(ILogger):
    def log(self, message):
        print(f" Logging to Console: {message}")



class Application:
    def __init__(self, logger: ILogger):
        self.logger = logger  

    def start(self):
        self.logger.log("Application started successfully!")



if __name__ == '__main__':
    # File logger
    file_logger = FileLogger()
    app1 = Application(file_logger)
    app1.start()

    # Database logger
    db_logger = DatabaseLogger()
    app2 = Application(db_logger)
    app2.start()

    # Console logger
    console_logger = ConsoleLogger()
    app3 = Application(console_logger)
    app3.start()
