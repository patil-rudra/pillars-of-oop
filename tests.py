class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_info(self):
        print(f"name is {self.name} \n ande age is {self.age}")
    
nam=person("rudra",19)
nam.display_info()