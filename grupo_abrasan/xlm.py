from xml.dom import minidom
import pandas as pd


def leer(file):
    with open("././media/"+file) as f:
            tree = minidom.parse(f)
            tags=tree.getElementsByTagName('cfdi:Concepto')
            desc = []
            cant = []
            
            for tagname in tags:
                
                descripcion= tagname.attributes['Descripcion'].value
                print(descripcion)
                desc.append(descripcion)
                cantidad= tagname.attributes['Cantidad'].value
                cant.append(cantidad)
                print(cantidad)
                importe= tagname.attributes['Importe'].value
                print(importe)

            df = pd.DataFrame({'Descripcion':desc, 'Cantidad':cant})

#archivos=Archivos.objects.filter(solicitud=50).values('ruta')
rutas=['xml/ejemplo.xml','xml/FacCFDI_GMU160422511_GBT-67150081.xml']
for a in rutas:
    leer(a)
    
    
