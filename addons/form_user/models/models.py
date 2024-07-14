# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Client(models.Model):
    _name = 'form_user.form_user'
    _description = 'Información del cliente '
    
    name = fields.Char(string='Name')
    last_name = fields.Char(string='Last name')
    email = fields.Char(string= 'Name')
    telefono = fields.Char(string='Name')
    fecha_nacimiento = fields.Date( 'Fecha Nacimiento')
    genero = fields. Char (string='Genero')
    estado_civil = fields.Char(string='Estado civil')
    direccion = fields.Char(string='Dirección')
    ciudad = fields.Char(string='Ciudad')
    estado_provincia = fields.Char(string='Estado provincia')
    pais = fields.Char(string='País')
    codigo_postal = fields.Char (string='Codigo postal')