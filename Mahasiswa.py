class Mahasiswa:
  def __init__ (self, name, nim, prodi):
    self.name = name
    self.nim = nim
    self.prodi = prodi
    
  def info(self):
    print(f"Nama : {self.name}")
    print(f"Prodi : {self.prodi}")
    
mizz = Mahasiswa("Misbah", "23.1.9.0044", "TI")

mizz.info()

