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


def printList(id, project, list):
    # Print Header
    printer.text(project)
    printer.text(" To Do")
    printer.text("\n")
    printer.set(align="center")
    printer.qr("https://todoist.com/app/?lang=en#project%2F" + project)
    printer.text("\n")
    printer.text("\n")

    # Print tasks
    



def printError(error):
    printer.text("Whoopsies, got an error :(\n")
    printer.text(error)
    printer.cut()
