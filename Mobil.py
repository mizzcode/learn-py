class Mobil:
  def __init__(self, merk, model, warna, tahun):
    self.merk = merk
    self.model = model
    self.warna = warna
    self.tahun = tahun
  
  def info(self):
    print(f"Mobil {self.merk} Model {self.model} Warna {self.warna}, Tahun {self.tahun}")
    
toyota = Mobil("Toyota", "Skye", "Hijau", 2085)
avanza = Mobil("Avanza", "Raze", "Kuning", 2085)
honda = Mobil("Honda", "Yoru", "Biru", 2085)

toyota.info()
avanza.info()
honda.info()