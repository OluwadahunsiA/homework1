class Store:
    def __init__(self, name, obj, copies):
        self.name = name
        self.obj = obj
        self.copies = copies


class Printer(Store):
    def __init__(self, name, obj, copies, takes_external_flash):
        super().__init__(name, obj, copies)
        self.takes_external_flash = takes_external_flash


class Scanner(Store):
    def __init__(self, name, obj, copies, scan_resolution):
        super().__init__(name, obj, copies)
        self.scan_resolution = scan_resolution


class Xerox(Store):
    def __init__(self, name, obj, copies, xerox_model):
        super().__init__(name, obj, copies)
        self.xerox_model = xerox_model
