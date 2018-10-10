"""Extending CRUDLFAP features."""

from crudlfap import crudlfap
from .models import Post

crudlfap.Router(model=Post).register()
