import copy


class Person:
    def __init__(self, position):
        self.position = position


class FreePerson(Person):
    def __init__(self, position):
        super().__init__(position)

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist


class Prisoner(Person):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super(Prisoner, self).__init__(copy.copy(self.PRISON_LOCATION))   # copy to change the copy not the original 
        self.is_free = False


prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")


"""
------------------------------------ Problem to resolve --------------------------------

You are provided with a code containing a class Prisoner and a class Person. A prisoner is obviously a 
person, but since a prisoner is not free to move an arbitrary distance, the Person class can be named 
FreePerson, then the idea that a Prisoner inherits FreePerson is wrong. Rewrite the code and apply the LSP 
(Liskov Substitution Principle).

-------------------------------------- Example inputs ----------------------------------
Code Before: 

class Worker:

    def work(self):
        print("I'm working!!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, Worker), '`worker` must be of type {}'.format(Worker)

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()

class SuperWorker:

    def work(self):
        print("I work very hard!!!")



worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
except AssertionError:
    print("manager fails to support super_worker....")


-------------------------------------------------------------------------------------
Test Code Before:                                                   Output Before:
prisoner = Prisoner()                                               The prisoner trying to walk to north by 10 and east by -3.
print("The prisoner trying to walk to north by 10 and east by -3.") The location of the prison: [3, 3]
                                                                    The current position of the prisoner: [0, 13]
try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")

-------------------------------------------------------------------------------------
Test Code After:                                                    Output Before:
prisoner = Prisoner()                                               The prisoner trying to walk to north by 10 and east by -3.
print("The prisoner trying to walk to north by 10 and east by -3.") The location of the prison: (3, 3)
                                                                    The current position of the prisoner: (3, 3)
try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")

"""
