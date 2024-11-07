class Robot:
    def __init__(self, name):
        self.name  = name
        self.position = [0, 0]
        print('My name is', name)
        
    def walk(self, x):
        self.position[0] = self.position[0] + x
        print('current position' , self.position)
        
    def eat(self):
        print('I am hungry !')

# inherited from Robot
class Robot_Dog(Robot):
    def Make_noise(self):
        print('wof wof !')
    
    def eat(self):
        # super lets to call the parent class implementation of eat method
        super().eat()
        print('I like chicken !')
        
def main():
    my_robot_dog = Robot_Dog('lucky')
    my_robot_dog.walk(10)
    my_robot_dog.Make_noise()
    
    # overriden method from parent class
    my_robot_dog.eat()
    
main()