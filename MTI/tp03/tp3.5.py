from abc import ABC, abstractmethod

# Abstract Interface
class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass


# Concrete Implementations
class EmailService(NotificationService):
    def send(self, message):
        print(f"Sending Email: {message}")


class SMSService(NotificationService):
    def send(self, message):
        print(f"Sending SMS: {message}")


class PushNotificationService(NotificationService):
    def send(self, message):
        print(f"Sending Push Notification: {message}")


# High-Level Module
class Notification:
    def __init__(self, service: NotificationService):
        self.service = service

    def send(self, message):
        self.service.send(message)


# Main call to test all services (after DIP)
if __name__ == '__main__':
    # Send an Email
    email_service = EmailService()
    notification = Notification(email_service)
    notification.send("Hello via Email!")

    # Send an SMS
    sms_service = SMSService()
    notification = Notification(sms_service)
    notification.send("Hello via SMS!")

    # Send a Push Notification
    push_service = PushNotificationService()
    notification = Notification(push_service)
    notification.send("Hello via Push Notification!")
