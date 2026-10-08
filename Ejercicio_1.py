Nombre =input("Ingresa tu nombre ")
DiasTrabajados = int(input ("¿Cuantos dias ha trabajado? "))
PagoMes = DiasTrabajados * 75000
Arl = 350000
AuxilioTransporte = 210000
Bruto =  PagoMes + Arl + AuxilioTransporte
print(f"{Nombre} tu salario seria {Bruto}, sin las deducciones son {PagoMes}")