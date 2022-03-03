# -*- coding: utf-8 -*-


from attr import field
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
    screening_id = fields.One2many('open_cinema.screening', 'film_id', string = 'Screenings')
    director_id = fields.Many2one('open_cinema.director', ondelete = 'cascade', string = 'Director', required = True)
    
class Screening(models.Model):
    _name = 'open_cinema.screening'
    _descrition = 'Open cinema Screening'
    
    name = fields.Char(string = 'Name', required = 'true')
    film_id = fields.Many2one('open_cinema.film', ondelete = 'cascade', string = 'Film', required = True)
    screening_date = fields.Date(string='Screening Date')
    responsible_id = fields.Many2one('res.users', ondelete = 'cascade', string = 'Responsible', required = True)
    seats = fields.Integer()
    prize = fields.Float()
    
class Director(models.Model):
    _name = 'open_cinema.director'
    _description = 'Open Cinema Director'
    
    name = fields.Char(string = 'Name', required = True)
    nacionality = fields.Char(string = 'Nacionality')
    film_director_id = fields.One2many('open_cinema.film', 'director_id', string = "Films")