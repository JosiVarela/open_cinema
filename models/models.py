# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Film(models.Model):
    _name = 'open_cinema.film'
    description = 'Open cinema films'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    release_date = fields.Date(string='Release')
    year = fields.Char(required=True)
    duration = fields.Integer()