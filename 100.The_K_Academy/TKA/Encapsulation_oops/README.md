**Encapsulation** :- </br>
-> Wrapping of data and methods together in oe entity(class) is called encapsulaton.</br>
</br>
    Encapsulation ----> information hiding
</br>

-> You can hide internal state of object from outside. This is known as information hiding.

**Access modifiers in Python :-**</br>
-> Access modifirers linit access to the variable and methods of a class
-> Python provides **three types of access modifiers** </br>
        1) Public Member-</br>
            -> Accessible anywhere from the outside class.</br>
        2) Private Member-</br>
            -> Accessible in within the class.</br>
        3) Protected Member-</br>
            -> Accessible within the class and it's sub-class.</br>

**1) Public Member:-**
e.g.

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