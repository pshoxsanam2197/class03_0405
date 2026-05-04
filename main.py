# 16-m
class Sportchi:
    def __init__(self, ism, ochko):
        self.ism = ism
        self.ochko = ochko

    def gol_ur(self):
        self.ochko += 1
        print("Gol urildi!")

    def info(self):
        print("Ism:", self.ism)
        print("Ochko:", self.ochko)


sp = Sportchi("Messi", 10)
sp.gol_ur()
sp.gol_ur()
sp.info()

# 17-m
class Oyin:
    def __init__(self, nomi, level):
        self.nomi = nomi
        self.level = level

    def level_oshir(self):
        self.level += 1
        print("Level oshdi")

    def level_tushir(self):
        self.level -= 1
        print("Level tushdi")

    def info(self):
        print("O‘yin:", self.nomi)
        print("Level:", self.level)


o = Oyin("Subway", 3)
o.level_oshir()
o.level_tushir()
o.info()

# 18-m
class Kutubxona:
    def __init__(self, nomi, kitob_soni):
        self.nomi = nomi
        self.kitob_soni = kitob_soni

    def qoshish(self, n):
        self.kitob_soni += n
        print(f"{n} ta kitob qo‘shildi")

    def olish(self, n):
        self.kitob_soni -= n
        print(f"{n} ta kitob olindi")

    def info(self):
        print("Kutubxona:", self.nomi)
        print("Kitoblar soni:", self.kitob_soni)


k = Kutubxona("Milliy kutubxona", 10000)
k.qoshish(500)
k.olish(200)
k.info()
