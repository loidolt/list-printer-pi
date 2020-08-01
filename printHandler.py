from escpos.printer import Serial

from hardware import yellowLED

""" 9600 Baud, 8N1, Flow Control Enabled """
printer = Serial(
    devfile="/dev/serial0",
    baudrate=9600,
    bytesize=8,
    parity="N",
    stopbits=1,
    timeout=1.00,
    dsrdtr=True,
)

printer.set(align="center")
printer.text("List Printer Pi\n")
printer.qr("https://github.com/loidolt/list-printer-pi.git")
printer.cut()


def printList(id, project, tasks):

    # Print Header
    printer.set(align="center")
    printer.text(project)
    printer.text(" To Do")
    printer.text("\n")
    printer.text("\n")
    printer.qr("https://todoist.com/app/?lang=en#project%2F" + str(id))
    printer.text("\n")
    printer.text("\n")

    # Print tasks
    printer.set(align="left")

    # Iterate through tasks
    if tasks != []:
        for index in range(len(tasks)):
            printer.text("[]  ")
            printer.text(str(tasks[index]["content"]))
            printer.text("\n")
            printer.text("\n")
    else:
        printer.text("No tasks right now.\n")
        printer.text("\n")
        printer.text("Have a great day! :)")
        printer.text("")

    # Generic Spacing After List
    printer.text("\n")
    printer.text("\n")
    printer.text("\n")
    printer.text("\n")

    # Turn off yellow LED
    yellowLED(0)


def printError(error):
    printer.text("Whoopsies, got an error :(\n")
    printer.text(str(error))
    printer.cut()

    # Turn off yellow LED
    yellowLED(0)
