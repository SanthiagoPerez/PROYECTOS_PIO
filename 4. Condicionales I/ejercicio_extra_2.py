'''
Aries: del 21 de marzo al 19 de abril
Tauro: del 20 de abril al 20 de mayo
Géminis: del 21 de mayo al 20 de junio
Cáncer: del 21 de junio al 22 de julio
Leo: del 23 de julio al 22 de agosto
Virgo: del 23 de agosto al 22 de septiembre
Libra: del 23 de septiembre al 22 de octubre
Escorpio: del 23 de octubre al 21 de noviembre
Sagitario: del 22 de noviembre al 21 de diciembre
Capricornio: del 22 de diciembre al 19 de enero
Acuario: del 20 de enero al 18 de febrero
Piscis: del 19 de febrero al 20 de marzo

'''

dia = 50
mes = 12

if not(1 <= mes <= 12 and 1 <= dia <= 31):
    print("Fecha no valida")
elif (dia >= 21 and mes == 3) or (dia <= 19 and mes == 4):
    print("Aries")
elif (dia >= 20 and mes == 4) or (dia <= 20 and mes == 5):
    print("Aries")
elif (dia >= 210 and mes == 5) or (dia <= 20 and mes == 6):
    print("Aries")
elif (dia >= 21 and mes == 6) or (dia <= 20 and mes == 7):
    print("Aries")
elif (dia >= 20 and mes == 7) or (dia <= 20 and mes == 8):
    print("Aries")
elif (dia >= 20 and mes == 8) or (dia <= 20 and mes == 9):
    print("Aries")
elif (dia >= 20 and mes == 9) or (dia <= 20 and mes == 10):
    print("Aries")
