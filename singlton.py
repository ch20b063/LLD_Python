"""
Multiple classes using same instance 
example: thread pools, caches, loggers etc.

The **Singleton Design Pattern** is a **creational pattern** that ensures a class has only **one instance** and provides a **global point of access** to it.

---

### 🔑 Key Features:

1. **Single Instance**: Only one instance of the class can exist.
2. **Global Access**: The instance can be accessed globally.
3. **Lazy Initialization**: The instance is created when it's needed.

---

### 🧠 Real-world Analogy:

Think of the **president of a country** — there can be only one at a time, and everyone refers to that single person when talking about “the president.”

---

### ✅ Use Cases:

* Database connections
* Configuration managers
* Logger classes
* Cache systems

---

### 🧱 Structure:

+---------------------+
|     Singleton       |
|---------------------|
| - instance: static  |
|---------------------|
| + getInstance():    |
|   Singleton         |
+---------------------+
```

---

### ⚠️ Pros and Cons:

#### ✅ Pros:

* Controlled access to the sole instance
* Saves memory (especially when the object is heavy)
* Thread-safe (if implemented properly)

#### ❌ Cons:

* Global state can lead to hidden dependencies
* Harder to test (mocking a singleton is tricky)
* Often considered an **anti-pattern** in large systems if overused

---

### 🛠 Variants:

* **Thread-safe Singleton**
* **Eager Initialization**
* **Lazy Initialization**
* **Double-checked Locking** (in multithreaded contexts)

---

Class1 ---> Object  <---- Class2
             ^
             |
             |
           Class3

""" 

# Coding part

class signleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super(signleton,cls).__new__(cls)
            print("creating new instance")
        return cls._instance



class Student:
    __instance = None  # Singleton instance

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Student, cls).__new__(cls)
            cls.__instance.__student_list = []  # initialize only once
        return cls.__instance

    def add_student(self, student):
        self.__student_list.append(student)

    def getlist(self):
        return self.__student_list

# shareing one siglton with multiclass

class secondyear:
        def addstudent(self,name):
            check = Student()
            check.add_student(name)
        def getlist(self):
            check = Student()
            return check.getlist()

class firstyear:
        def addstudent(self,name):
            check = Student()
            check.add_student(name)
        def getlist(self):
            check = Student()
            return check.getlist()


if __name__ == "__main__":
    A = Student()
    B = Student()
    C = Student()
    E  = secondyear()
    F = firstyear()

    E.addstudent("Manish")
    F.addstudent("Kumar")
    A.add_student("Alice")
    B.add_student("Bob")

    print(F.getlist())
    print(A.getlist())  # ['Alice', 'Bob']
    print(B.getlist())  # ['Alice', 'Bob']
    print(A is B is C)  # True => Singleton confirmed
    print(A,B,C,E,F)
    P = signleton()
    Q = signleton()
    R = signleton()
    # print("hello")
    print(P, Q,R)


    