class Punto:
    x = 0
    y = 0
    def muovi(self,dx,dy):
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

        

oggetto = Punto()
oggetto.muovi(2,4)
oggetto.distanza_da_origile()