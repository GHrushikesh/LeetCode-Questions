class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:

        for event in self.events:
            oldStart, oldEnd = event

            if startTime < oldEnd and endTime > oldStart:
                return False

        self.events.append((startTime, endTime))
        return True