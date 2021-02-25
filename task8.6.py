class Store:
    def __init__(self, name, obj, copies):
        self.name = name
        self.obj = obj
        self.copies = copies
        self.inventory = []

    def storage_department(self):
        print(self.inventory)


class Printer(Store):
    def __init__(self, name, obj, copies, takes_external_flash):
        super().__init__(name, obj, copies)
        self.takes_external_flash = takes_external_flash

    def printer_method(self):
        printed = {'Person': self.name, 'Printed': self.obj,
                   'Copies': self.copies, 'External_Device': self.takes_external_flash}
        if type(printed['Copies']) not in [int, float]:
            print('Please check your input and enter an integer value of copies')
        else:
            self.inventory.append(printed)
            self.storage_department()


class Scanner(Store):
    def __init__(self, name, obj, copies, scan_resolution):
        super().__init__(name, obj, copies)
        self.scan_resolution = scan_resolution

    def scanner_method(self):
        scanned = {'Person': self.name, 'Scanned': self.obj,
                   'Copies': self.copies, 'Scan_resolution': self.scan_resolution}
        if type(scanned['Copies']) not in [int, float] or (scanned['Scan_resolution'].lower()) not in ['high', 'medium', 'low']:
            print('Please check your input')
        else:
            self.inventory.append(scanned)
            self.storage_department()


class Xerox(Store):
    def __init__(self, name, obj, copies, xerox):
        super().__init__(name, obj, copies)
        self.xerox = xerox

    def xerox_method(self):
        xeroxed = {'Person': self.name, 'Xeroxed': self.obj,
                   'Copies': self.copies, 'Xerox-model': self.xerox}
        if type(xeroxed['Copies']) not in [int, float]:
            print('Please check your input')

        else:
            self.inventory.append(xeroxed)
            self.storage_department()


new_print = Printer('Olaokun', "printer", 10, True)
new_print.printer_method()

new_scan = Scanner('Rali', 'scanner', 10, 'High')
new_scan.scanner_method()

new_xerox = Xerox('Rali', 'scanner', 25, 'Xerox-green')
new_xerox.xerox_method()
