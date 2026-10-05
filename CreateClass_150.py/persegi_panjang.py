class PersegiPanjang:
    
    def init(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

   
    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def luas(self):
        return self.panjang * self.lebar

    
    def str(self):
        return f"persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"