volar  = {}
volar["Aerolínea"] = "Avianca" 
volar["vuelo"] = "AV3102" 
volar["Origen"] = "CTG" ,
volar["Destino"]= "MDE" ,
volar["TipodeMaleta"] = [ 'Cabina' , 'Mano' , 'Bodega' ]
print( "Datos del diccionario: " )


for  key , value in volar.items ():
  print ( f" { key } : { value } " )


print ( " \n Valores del tipo de maleta: " )
for  tipodemaleta in volar [ "TipodeMaleta" ]:
    print ( tipodemaleta )