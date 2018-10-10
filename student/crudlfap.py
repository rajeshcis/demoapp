"""Extending CRUDLFAP features."""

from crudlfap import crudlfap
from .models import Student

crudlfap.Router(model=Student).register()
