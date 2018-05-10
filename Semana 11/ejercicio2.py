#Ejercicio2

class Empleado():

    def __init__(self,nombre,horasTrabajadas,salarioHora,horasExtras,labores):
        self.nombre=nombre
        self.horasTrabajadas=horasTrabajadas
        self.salarioHora=salarioHora
        self.horasExtras=horasExtras
        self.labores = labores

    def SalarioOrdinario(self):
        if(self.horasTrabajadas<=40):
            return self.horasTrabajadas*self.salarioHora
        else:
            residuo=self.horasTrabajadas-40
            self.horasExtras=self.horasExtras+residuo
            self.horasTrabajadas=self.horasTrabajadas-residuo
            return self.horasTrabajadas * self.salarioHora

    def SalarioExtra(self):
        return (self.horasExtras*(self.salarioHora+(self.salarioHora*0.5)))

    def SalarioFinal(self):
        return self.SalarioOrdinario()+self.SalarioExtra()

    def BoletaPago(self):
        print("La mejor boleta del mundo")
        print("------------------------------------------------------")
        print("Pago")
        print("El salario ordinario",self.SalarioOrdinario())
        print("El salario extra", self.SalarioExtra())
        print("El salario final", self.SalarioFinal())
        print("------------------------------------------------------")
        print("Labores")
        for item in self.labores:
            print(item)

empleado1=Empleado("Carlitos",41,2,10000,["Limpieza de chanchos","Masajes"])
empleado1.BoletaPago()

empleado2=Empleado("Coco",80,1,15000,["Tocador","ING."])
empleado2.BoletaPago()
