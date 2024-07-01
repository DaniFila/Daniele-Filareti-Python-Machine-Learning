class Punto:
    x = 0
    y = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def muovi(self):
        dx = int(input("Inserire valore per dx"))
        dy = int(input("Inserire valore per dy"))
        self.x = dx
        self.y = dy
    def distanza_da_origile(self):
        if self.x > 0 and self.y >0:
            print("La distanza da zero è: ")
            print(self.x,self.y)
        if self.x > 0:
            print("La distanza da zero è: ")
            print(self.x)
        if self.y > 0:
            print("La distanza da zero è: ")
            print(self.y)
        
        