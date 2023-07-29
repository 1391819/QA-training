# https://github.com/agray998/oop-exercise-2


"""
Task: create a clock class. Each clock should have the attributes hours, minutes and seconds.
The class should have methods to:
 - initialise these attributes upon instance creation
 - update the clock's time by one second when called (remembering to wrap appropriately after every 60 seconds)
 - return a string representation of the current clock time
 Create a subclas of this class for 12-hour clocks, and override the methods appropriately
"""


# Clock class
class Clock:
    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0) -> None:
        """Initialise a Clock instance.

        Args:
            hours (int, optional): Number representing the hour of the Clock. Defaults to 0.
            minutes (int, optional): Number representing the minutes of the Clock. Defaults to 0.
            seconds (int, optional): Number representing the seconds of the Clock. Defaults to 0.
        """

        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def tick(self) -> None:
        """Update the Clock's time by one second."""

        # wrap seconds using %
        self.seconds = (self.seconds + 1) % 60
        if self.seconds == 0:
            # wrap minutes using %
            self.minutes = (self.minutes + 1) % 60
            if self.minutes == 0:
                # wrap hours using %
                self.hours = (self.hours + 1) % 24

    def __str__(self) -> str:
        """Return a string representation of the Clock

        Returns:
            str: A string representation of the Clock
        """

        hours_str = "{:02d}".format(self.hours)
        minutes_str = "{:02d}".format(self.minutes)
        seconds_str = "{:02d}".format(self.seconds)

        return f"{hours_str}:{minutes_str}:{seconds_str}"


class TwelveHourClock(Clock):
    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0) -> None:
        """Initialise a TwelveHourClock instance.

        Args:
            hours (int, optional): Number representing the hour of the TwelveHourClock. Defaults to 0.
            minutes (int, optional): Number representing the minutes of the TwelveHourClock. Defaults to 0.
            seconds (int, optional): Number representing the seconds of the TwelveHourClock. Defaults to 0.
        """

        # calling parent class __init__()
        super().__init__(hours, minutes, seconds)
        # adding extra variable to keep track of AM and PM
        self.meridian = "AM" if self.hours < 12 else "PM"

    def tick(self) -> None:
        """Update the TwelveHourClock's time by one second."""

        # wrap seconds using %
        self.seconds = (self.seconds + 1) % 60
        if self.seconds == 0:
            # wrap minutes using %
            self.minutes = (self.minutes + 1) % 60
            if self.minutes == 0:
                # wrap hours using %
                self.hours = (self.hours + 1) % 12
                # updating meridian
                if self.hours == 0:
                    self.meridian = "AM" if self.meridian == "PM" else "PM"

    def __str__(self) -> str:
        """Return a string representation of the TwelveHourClock

        Returns:
            str: A string representation of the TwelveHourClock
        """
        hours12 = self.hours if self.hours != 12 else 12

        hours_str = "{:02d}".format(hours12)
        minutes_str = "{:02d}".format(self.minutes)
        seconds_str = "{:02d}".format(self.seconds)

        return f"{hours_str}:{minutes_str}:{seconds_str} {self.meridian}"
