class Counter:
    def __init__(self):
        self.count = 0

    def inc_count(self):
        self.count += 1

    def dec_count(self):
        self.count -= 1

    def display_count(self):
        print(self.count)

c1 = Counter()
c1.display_count()
c1.inc_count()
c1.inc_count()
c1.inc_count()
c1.inc_count()
c1.inc_count()
c1.inc_count()
c1.inc_count()
c1.display_count()
c1.dec_count()
c1.dec_count()
c1.dec_count()
c1.display_count()
c1.count = 777
c1.inc_count()
c1.display_count()
c1.inc_count()
c1.inc_count()
c1.inc_count()
c1.display_count()