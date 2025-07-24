class calculator:

    def input (self):
        try:
            self.x = float(input("Enter the first value.."))
            self.y = float(input("Enter the second value.."))
            self.opr = input("Operation that you want.. +,-,x,/__")

        except ValueError:
            print("Invalid input. Please enter numeric values.")
            self.opr = None

        self.u_choice = {
            "+": lambda: self.x+self.y,
            "-": lambda: self.x-self.y,
            "x": lambda: self.x*self.y,
            "/": lambda: self.x/self.y
        }
    
    def conditional (self):
        if self.opr in self.u_choice:
            if self.opr == "/" and self.y == 0:
                print("Cannot divide by zero.")
            else:
                result =(self.u_choice[self.opr]())
                print(f"Required result is: {result}")
        else:
            print("Invalid operation")


    def loop (self):
        while True:
            self.input()
            self.conditional()
            x = input("Do you want to perform another calculation? (y/n):").lower()
            if x == "y":
                continue
            else:
                print("Thanks for using the calculator!")
                break
    
     
obj = calculator()
obj.loop()