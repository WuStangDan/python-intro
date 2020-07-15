# Classes are used to group functions and variables together.
class AddOne():
    # The init or initializer function is where you declare variables.
    def __init__(self, count):
        # Preface all variables with "self."
        self.count = count

    # Member functions can be defined below.
    # Be sure to also include the self in the arguments.
    def increase(self):
        self.count += 1


class AddTwo(AddOne):
    # The init or initializer function is where you declare variables.
    def __init__(self, count):
        # Create AddOne class inside this class and pass count into AddOne class.
        AddOne.__init__(self, count)

    def increase_by_two(self):
        # You can either call the function as if it was declared in this class.
        self.increase()
        # Or specify the derived class directly.
        AddOne.increase(self)

first_number = AddOne(10)
second_number = AddTwo(10)

first_number.increase()
second_number.increase()
second_number.increase_by_two()


# Print the number of students and teachers.
print('First Number: ' + str(first_number.count))
print('Second Number: ' + str(second_number.count))

