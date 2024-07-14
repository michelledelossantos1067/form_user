# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Client(models.Model):
    _name = 'form_user.form_user'
    _description = 'Información del cliente '
    
    name = fields.Char(string='Name')
    last_name = fields.Char(string='Last name')
    email = fields.Char(string= 'Email')
    telefono = fields.Char(string='Teléfono')
    fecha_nacimiento = fields.Date(string='Fecha Nacimiento')
    genero = fields.Selection([ ('mujer', 'Mujer'),('hombre', 'Hombre') ], string='Genero')
    estado_civil = fields.Selection( [ ('soltero', 'Soltero'),('casado', 'Casado') ], string='Estado civil')
    pais = fields.Char(string='País')
    ciudad = fields.Char(string='Ciudad')
    estado_provincia = fields.Char(string='Estado o provincia')
    direccion = fields.Char(string='Dirección')
    codigo_postal = fields.Char (string='Codigo postal')