# encoding: utf-8

from genera_layout import genera_layout

class Factura():

    def __init__(self):
        """ Valores predeterminados """
        
        self.encabezado = {
            "forma_de_pago":"Transferencia",
            "metodo_de_pago":"Pago en una sola exhibicion",
            "condiciones":"Contado",
            "NumCtaPago":"",
            "lugarDeExpedicion":"Victoria de Durango",
            "subtotal":None,
            "total":None,
            "notas":""
            }
        self.emisor = {
            "domicilio_calle":"Lic. Alberto Terrones Benitez #101 NTE",
            "domicilio_noExterior":"101 NTE",
            "domicilio_noInterior":"",
            "domicilio_colonia":"Durango",
            "domicilio_localidad":"Victoria de Durango",
            "domicilio_municipio":"Durango",
            "domicilio_estado":"Durango",
            "domicilio_pais":"Mexico",
            "domicilio_cp":"34000",
            "expedidoen_calle":"Av. 20 de Noviembre",
            "expedidoen_noExterior":"1002 Ote",
            "expedidoen_noInterior":"",
            "expedidoen_colonia":"Centro",
            "expedidoen_localidad":"Victoria de Durango",
            "expedidoen_municipio":"Durango",
            "expedidoen_estado":"Durango",
            "expedidoen_pais":"Mexico",
            "expedidoen_cp":"34000",
            "emisor_rfc":"ESI920427886",
            "emisor_nombre":"Rectificaciones Avina SA de CV",
            "regimen_fiscal":"Regimen general de personas morales",
            }
        self.receptor = {
            "rfc_receptor":"",
            "nombre_fiscal":"",
            "calle":"",
            "noExterior":"",
            "noInterior":"",
            "colonia":"",
            "localidad":"",
            "municipio":"",
            "estado":"",
            "pais":"",
            "cp":"",
            "noCliente":"",
            "email":"",
            }
        self.factura = {
            "fecha_factura":"",
            "serie":"",
            "folio":""
            }
        self.impuesto = {
            "impuesto":"IVA",
            "importe_impuesto":None,
            "tasa":None
            }
        self.lineas_factura = []

    def agrega_linea(self,cantidad,unidad,noIdentificacion,descripcion,valorUnitario, \
                         importe):
            self.lineas_factura.append( {
                    "cantidad":cantidad,
                    "unidad":unidad,
                    "noIdentificacion":noIdentificacion,
                    "descripcion":descripcion,
                    "valorUnitario":valorUnitario,
                    "importe":importe
                    })


    ###
    #
    # Mutador Factura
    #
    ###
    def edita_factura_fecha_factura(self, fecha_factura):
        self.factura["fecha_factura"] = fecha_factura
    def edita_factura_serie(self, serie):
        self.factura["serie"] = serie
    def edita_factura_folio(self, folio):
        self.factura["folio"] = folio

    
    ###
    #
    # Mutador Impuesto
    #
    ###
    def edita_impuesto(self, impuesto):
        self.impuesto["impuesto"] = impuesto
    def edita_importe_impuesto(self, importe_impuesto):
        self.impuesto["importe_impuesto"] = importe_impuesto
    def edita_impuesto_tasa(self, tasa):
        self.impuesto["tasa"] = tasa

    

    ###
    #
    # Mutadores encabezado
    #
    ###
    def edita_encabezado_notas(self, notas):
        self.encabezado["notas"] = notas
    def edita_encabezado_subtotal(self, subtotal):
        self.encabezado["subtotal"] = subtotal
    def edita_encabezado_total(self, total):
        self.encabezado["total"] = total
    def edita_encabezado_forma_de_pago(self, forma_de_pago):
        self.encabezado["forma_de_pago"] = forma_de_pago
    def edita_encabezado_metodo_de_pago(self, metodo_de_pago):
        self.encabezado["metodo_de_pago"] = metodo_de_pago
    def edita_encabezado_condiciones(self, condiciones):
        self.encabezado["condiciones"] = condiciones
    def edita_encabezado_NumCtaPago(self, NumCtaPago):
        self.encabezado["NumCtaPago"] = NumCtaPago
    def edita_encabezado_lugarDeExpedicion(self, lugarDeExpedicion):
        self.encabezado["lugarDeExpedicion"] = lugarDeExpedicion

    ###
    #
    # Mutadores receptor
    #
    ###
    def edita_rfc_receptor(self, rfc_receptor):
        self.receptor["rfc_receptor"] = rfc_receptor
    def edita_receptor_nombre_fiscal(self, nombre_fiscal):
        self.receptor["nombre_fiscal"] = nombre_fiscal
    def edita_receptor_calle(self, calle):
        self.receptor["calle"] = calle
    def edita_receptor_noExterior(self, noExterior):
        self.receptor["noExterior"] = noExterior
    def edita_receptor_noInterior(self, noInterior):
        self.receptor["noInterior"] = noInterior
    def edita_receptor_colonia(self, colonia):
        self.receptor["colonia"] = colonia
    def edita_receptor_municipio(self, municipio):
        self.receptor["municipio"] = municipio
    def edita_receptor_estado(self, estado):
        self.receptor["estado"] = estado
    def edita_receptor_pais(self, pais):
        self.receptor["pais"] = pais
    def edita_receptor_cp(self, cp):
        self.receptor["cp"] = cp
    def edita_receptor_noCliente(self, noCliente):
        self.receptor["noCliente"] = noCliente
    def edita_receptor_email(self, email):
        self.receptor["email"] = email


    def __str__(self):
        return genera_layout(encabezado = self.encabezado,
                             receptor = self.receptor, 
                             factura = self.factura, 
                             lineas_factura = self.lineas_factura, 
                             impuesto = self.impuesto,
                             emisor = self.emisor)

    def __unicode__(self):
        return genera_layout(encabezado = self.encabezado,
                             receptor = self.receptor, 
                             factura = self.factura, 
                             lineas_factura = self.lineas_factura, 
                             impuesto = self.impuesto,
                             emisor = self.emisor)
