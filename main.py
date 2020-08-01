#!/usr/bin/env python3

from hardware import greenLED, pollButtons
from todoist import getProjectID


def main():
    while True:
        # Just indicating we are alive
        greenLED(1)

        buttonStatus = pollButtons()

        if buttonStatus != 0:
            getProjectID(buttonStatus)


if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        pass
