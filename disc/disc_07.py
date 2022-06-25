
class Student:
    students = 0
    def __init__(self, name, ta):
        self.name = name
        self.understanding = 0
        Student.students += 1
        print("There are now", Student.students, "students")
        ta.add_student(self)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)


class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1

# 1.1
snape = Professor("Snape")   
harry = Student("Harry", snape)
# There are now 1 students

harry.visit_office_hours(snape)
# Thanks, Snape

harry.visit_office_hours(Professor("Hagrid"))
# THanks, Hagrid

print(harry.understanding)
# 2

[print(name) for name in snape.students]
# Harry

x = Student("Hermione", Professor("McGonagall")).name
# There are now 2 students

print(x)
# Hermione

[print(name) for name in snape.students]
# Harry

# 1.2
class Email:
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name

class Server:
    def __init__(self):
        self.clients = {}

    def send(self, email):
        self.clients[email.recipient_name].receive(email)

    def register_client(self, client, client_name):
        self.clients[client_name] = client

class Client:
    def __init__(self, server, name):
        self.inbox = []
        self.server = server
        self.server.register_client(self, name)
        self.name = name
    
    def compose(self, msg, recipient_name):
        self.server.send(Email(msg, self.name, recipient_name))
    
    def receive(self, email):
        self.inbox.append(email)

s = Server()

huayang = Client(s, "Huayang")
dog = Client(s, "Dog")

dog.compose("你好Huayang", "Huayang")

[print(email.msg) for email in huayang.inbox]

# 2.1
class Pet():
    def __init__(self, name, owner):
        self.is_alive = True
        self.name = name
        self.owner = owner
    
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    
    def talk(self):
        print(self.name + " says woof!")

class Dog(Pet):
    def talk(self):
        print(self.name + " says woff!")

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner)
        self.lives = 9
    
    def talk(self):
        print(self.name, 'says meow!')
    
    def lose_life(self):
        if self.lives == 0:
            print(self.name, " has no no more lives to lose")
        self.lives -= 1
        if self.lives == 0:
            self.is_alive = False

d = Dog("dog1", "S")
d.talk()
c = Cat("cat1", "S")
c.talk()
# 2.2
class NoisyCat(Cat):
    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner, lives)
    
    def talk(self):
        super().talk()
        super().talk()

nc = NoisyCat("c2", "S")
nc.talk()

# 2.3

class A:
    def f(self):
        return 2

    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x - 1)

class B(A):
    def f(self):
        return 4

x, y = A(), B()
print(x.f())
# 2
# print(B.f())
# error f() is instance method

print(x.g(x, 1))
# 4

print(y.g(x, 2))
# 2 + 4 + 2

print(A.f(y))
# 2


class Link:
    empty = ()
    def __init__(self, first, rest = empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    
    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

# 3.1
def sum_nums(lnk):
    if lnk is Link.empty:
        return 0
    return lnk.first + sum_nums(lnk.rest)

a = Link(1, Link(6, Link(7)))
print(sum_nums(a))

# 3.2
def multiply_links(lst_of_links):
    def get_length(lst):
        len = 0
        while lst is not Link.empty:
            len += 1
            lst = lst.rest
        return len
    len = 999
    for lst in lst_of_links:
        len = min(len, get_length(lst))


    res = Link(1)
    tmp = res
    for i in range(1, len):
        tmp.rest = Link(1)
        tmp = tmp.rest

    for lst in lst_of_links:
        tmp = res
        for i in range(len):
            tmp.first *= lst.first
            tmp = tmp.rest
            lst = lst.rest
    return res
    

a = Link(2, Link(3, Link(5)))
b = Link(6, Link(4, Link(2)))
c = Link(4, Link(1, Link(0, Link(2))))
p = multiply_links([a, b, c])

print(p.first) # 48
print(p.rest.first) # 12
print(p.rest.rest.rest is Link.empty) # True


def filter_link(link, f):
    t = link
    while t is not Link.empty:
        if f(t.first):
            yield t.first
        t = t.rest

link = Link(1, Link(2, Link(3)))
g = filter_link(link, lambda x: x % 2 == 0)
print(next(g))
# print(next(g))

def filter_no_iter(link, f):
    if link is Link.empty:
        return
    if f(link.first):
        yield link.first
    yield from filter_no_iter(link.rest, f)

print(link)
print(list(filter_no_iter(link, lambda x: x % 2 != 0)))