from escpos.printer import Serial

# https://github.com/python-escpos/python-escpos
# https://python-escpos.readthedocs.io/en/latest/

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


def printList(id, project, sections, tasks):

    # Print Header
    printer.set(align="center")
    printer.text(project)
    printer.text(" To Do")
    printer.text("\n")
    printer.text("\n")
    printer.qr("https://todoist.com/app/?lang=en#project%2F" + str(id))
    printer.text("\n")
    printer.text("\n")

    printer.set(align="left")

    # Print Section
    if sections != []:
        for i in range(len(sections)):
            section_id = str(sections[i]["id"])

            printer.text(str(sections[i]["name"]))
            printer.text("\n")
            printer.text("------------------------------")
            printer.text("\n")
            # Print tasks
            if tasks != []:
                for index in range(len(tasks)):
                    task_section = str(tasks[index]["section_id"])
                    if section_id in task_section:
                        printer.text("[]  ")
                        printer.text(str(tasks[index]["content"]))
                        printer.text("\n")
                        printer.text("\n")
            else:
                printer.text("No tasks for this section.\n")
                printer.text("\n")

    else:
        # Print tasks
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
            printer.text("\n")

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
