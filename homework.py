class operation():
    def __init__(self,num1,num2):
        self.number1= num1
        self.number2=num2

    def display_result(self,result):
        print('The result is {}'.format(result))

    def add_numbers(self):
        sum = self.number1 + self.number2
        self.display_result(sum)
    def sub_numbers(self):
        diff = self.number1 - self.number2
        self.display_result(diff)
    def mul_numbers(self):
        product = self.number1 * self.number2
        self.display_result(product)
    def div_numbers(self):
        div = self.number1 / self.number2
        self.display_result(div)

o = operation(5,1)
o.add_numbers()
