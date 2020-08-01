from escpos.printer import Serial

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
    for i in tasks.keys():
        for j in tasks[i].keys():
            printer.text(str(j))

    printer.text("\n")

    # Generic Spacing After List
    printer.text("\n")
    printer.text("\n")
    printer.text("\n")
    printer.text("\n")


def printError(error):
    printer.text("Whoopsies, got an error :(\n")
    printer.text(str(error))
    printer.cut()
