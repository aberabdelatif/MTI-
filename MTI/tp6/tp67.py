class Calendar:
    def __init__(self):
        self._observers = set()
        self._events = []

    def attach(self, observer):
        observer._subject = self
        self._observers.add(observer)

    def detach(self, observer):
        observer._subject = None
        self._observers.discard(observer)

    def _notify(self, event):
        for observer in self._observers:
            observer.update(event)

    def add_event(self, title, event_date):
        event = {'title': title, 'date': event_date}
        self._events.append(event)
        print(f"\n[Calendar] Nouvel événement ajouté : {title} le {event_date}")
        self._notify(event)


class UserObserver:
    def __init__(self, name):
        self._subject = None
        self.name = name
        self.notifications = []

    def update(self, event):
        reminder = f"{self.name}, rappel : '{event['title']}' prévu le {event['date']}"
        self.notifications.append(reminder)
        print(f"[Notification] {reminder}")

    def show_notifications(self):
        print(f"\n=== Notifications pour {self.name} ===")
        for n in self.notifications:
            print(f"- {n}")


def main():
    calendar = Calendar()
    alice = UserObserver("Alice")
    bob = UserObserver("Bob")
    calendar.attach(alice)
    calendar.attach(bob)
    calendar.add_event("Réunion projet", "10-12-2025 10:00")
    calendar.add_event("Examen final", "15-12-2025 08:00")
    calendar.detach(bob)
    calendar.add_event("Conférence AI", "20-12-2025 14:00")
    alice.show_notifications()
    bob.show_notifications()


if __name__ == "__main__":
    main()
