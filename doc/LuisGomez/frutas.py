frutas = {
    'manzana': 500,
    'pera' : 400,
    'banano': 300,
    'guayaba': 40,
    'maracuya': 700,
    'mango': 300,
}
res = True
while res == True:
    fru = str(input("ingrese la fruta que desea comprar "))
    if fru not in frutas:
        print ("esa fruta no esta a la venta")
    else:
        can = int(input("ingre la cantidad de veces quese a vendido la fruta seleccionada "))
        pre = can * (frutas[fru])
        print (f"el precio final es de la fruta {fru} es {pre}")
        cas = str(input("es la ultima fruta? (si, no) "))
        if cas == "si":
            res = False