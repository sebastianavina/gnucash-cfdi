# encoding: utf-8

from facturacion_moderna import facturacion_moderna
from datetime import datetime
import base64
from M2Crypto import RSA
from lxml import etree as ET
import sha
import os
import re

import gnucash
from gnucash.gnucash_business import Customer, Employee, Vendor, Job, \
    Address, Invoice, Entry, TaxTable, TaxTableEntry, BillTerm

from factura import Factura
from mail import mail

input_url = "./gnucash/prueba.gnucash"

try:
    session = gnucash.Session(input_url,ignore_lock=True)
except Exception as exception:
    print "Problem opening input."
    print exception

factura = session.book.InvoiceLookupByID("125")

registro = Factura()


#emisor
#conf.agrega_cta_pago(factura.GetOwner().GetAddr().GetFax())
#conf.agrega_metodo_de_pago(factura.GetOwner().GetNotes())

#receptor
registro.edita_receptor_nombre_fiscal(factura.GetOwner().GetName())
registro.edita_receptor_calle(factura.GetOwner().GetAddr().GetAddr1())
registro.edita_receptor_colonia(factura.GetOwner().GetAddr().GetAddr2())
registro.edita_receptor_municipio(factura.GetOwner().GetAddr().GetAddr3())   
registro.edita_rfc_receptor(factura.GetOwner().GetAddr().GetAddr4())
registro.edita_receptor_email(factura.GetOwner().GetAddr().GetEmail())
registro.edita_receptor_pais("Mexico")

#print dir(factura)
from datetime import datetime
fecha = factura.GetDatePosted()
registro.edita_factura_fecha_factura(datetime(fecha.year,
                                     fecha.month, 
                                     fecha.day).isoformat())


#print factura.GetNotes()
#print factura.GetTotalTax()
#print factura.GetTotalSubtotal()
#print factura.GetTotal()
registro.edita_encabezado_condiciones(factura.GetTerms().GetName())

for concepto in factura.GetEntries():
    concepto = Entry(instance=concepto)
    registro.agrega_linea(
        cantidad=gnucash.GncNumeric(instance=concepto.GetQuantity()),
        unidad=concepto.GetAction(),
        noIdentificacion="N/D",
        descripcion=concepto.GetDescription(),
        valorUnitario=gnucash.GncNumeric(instance=concepto.GetInvPrice()),
        importe="92.00",
        )
    #print 
    #print gnucash.GncNumeric(instance=www.ReturnValue(www.GetInvTaxable()))

impuesto="IVA",#gnucash.GncNumeric(instance=concepto.ReturnTaxValue(concepto.GetInvTaxable())),
importe_impuesto=106.72,#concepto.GetInvTaxIncluded(),
tasa=16.00#TaxTable(instance=concepto.GetInvTaxTable())
    
    
    
#from genera_layout import genera_layout
#print genera_layout(registro.encabezado, registro.receptor, registro.factura, \
#                        registro.lineas_factura, registro.emisor)

# RFC utilizado para el ambiente de pruebas
rfc_emisor = registro.emisor["emisor_rfc"]

# Datos de acceso al ambiente de pruebas
url_timbrado = "https://t1demo.facturacionmoderna.com/timbrado/wsdl"
user_id = "UsuarioPruebasWS";
user_password = "b9ec2afa3361a59af4b4d102d3f704eabdf097d4"

cfdi = str(registro)

params = {'emisorRFC': rfc_emisor, 'UserID': user_id, 'UserPass': user_password}
options = {'generarCBB': True, 'generarPDF': True, 'generarTXT': True}
cliente = facturacion_moderna.Cliente(url_timbrado, params, False)

if cliente.timbrar(cfdi, options):
  folder = 'comprobantes'
  if not os.path.exists(folder): os.makedirs(folder)
  comprobante = os.path.join(folder, cliente.uuid)
  for extension in ['xml', 'pdf', 'png', 'txt']:
    if hasattr(cliente, extension):
      with open(("%s.%s" % (comprobante, extension)), 'w') as f: f.write(getattr(cliente, extension))
      print("%s almacenado correctamente en %s.%s" % (extension.upper(), comprobante, extension))
  print 'Timbrado exitoso'
  os.popen("./run_viewer.sh "+comprobante+".pdf")
  print "Preparando para mandar por correo"


  info = open(comprobante + ".txt","r")
  txt = ""
  for line in info:
      txt += line

  
  factura.SetNotes(txt)
  session.save()
  try:
      email_a_mandar = str(registro.receptor["email"])
  
      correo_env = mail(email_a_mandar,
                        "Factura electronica",
                        "A continuacion anexo factura electronica.",
                        comprobante+".pdf",
                        comprobante+".xml")
      print str(correo_env)

  except Exception as e:
      print str(e)
      print "Correo no enviado"

  print "Programa finalizado"
  

else:
  print("[%s] - %s" % (cliente.codigo_error, cliente.error))
