class laptop:
    def __init__(self, nm, ram, rom):
        self.name = nm
        self.ram = ram
        self.rom = rom

    def display(self):
        print(f"Laptop name is {self.name}, ram is {self.ram}gb, and rom is {self.rom}tb.")

l1 = laptop("HP", 16, 1)
l1.display()

l2 = laptop("dell", 32, 1)
l2.display()