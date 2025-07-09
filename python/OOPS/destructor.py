class Example:
    def __del__(self):
        print("Destructor called")

e = Example()
del e  # Destructor called
