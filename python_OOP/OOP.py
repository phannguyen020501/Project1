from builtins import print


class Car:
    loaixe = "O to"

    def __init__(self, tenxe, mausac, nguyenlieu):
        self.tenxe = tenxe
        self.mausac = mausac
        self.nguyenlieu = nguyenlieu
    # phuong thuc: method
    def dungxe(self, mucdich):
        return "{} dang dung xe de {}".format(self.tenxe, mucdich)

    def chayxe(self):
        return "{} ddang chay tren duong".format(self.tenxe)

    def nomay(self):
        return "{} dang no may".format(self.tenxe)


#instance the Car class

toyota = Car("Toyota", "Do", "Dien")
lamborghini = Car("Lamborghini", "Vang", "Deisel")
porche = Car("Porche", "Xanh", "Gas")

#access the class attribute

print("Porche : {}" .format(porche.__class__.loaixe))
print("Toyota : {}" .format(toyota.__class__.loaixe))
print("Lamborghini : {}" .format(lamborghini.__class__.loaixe))

print("Xe: {}, mau: {},nguyenlieu: {}".format(toyota.tenxe, toyota.mausac, toyota.nguyenlieu))
print("Xe: {}, mau: {},nguyenlieu: {}".format(porche.tenxe, porche.mausac, porche.nguyenlieu))
print("Xe: {}, mau: {},nguyenlieu: {}".format(lamborghini.tenxe, lamborghini.mausac, lamborghini.nguyenlieu))

print(toyota.dungxe("nap dien"))
print(lamborghini.chayxe())
print(porche.nomay())
