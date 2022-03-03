# -*- coding: utf-8 -*-


from setuptools import Require
from odoo import models, fields, api


class Film(models.Model):
    _name = 'open_cinema.film'
    description = 'Open cinema films'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    release_date = fields.Date(string='Release')
    year = fields.Char(required=True)
    duration = fields.Integer()
    sinopsis = fields.Char(string="Sinopse")
    screening = fields.One2many('open_cinema.screening', )
    
class Screening(models.Model):
    _name = 'open_cinema.screening'
    _descrition = 'Open cinema Screening'
    
    film_id = fields.Many2one('open_cinema.film', ondelete = 'cascade', string = 'Film', required = True)
    screening_date = fields.Date(string='Screening Date')
    seats = fields.Integer()
    prize = fields.Float()
    
class Director(models.Model):
    _name = 'open_cinema.director'
    _description = 'Open Cinema Director'
    
    name = fields.Char(string = 'Name', required = True)
    nacionality = fields.Char(string = 'Nacionality')