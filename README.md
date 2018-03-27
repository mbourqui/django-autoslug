# django-autoslugged

![image](https://img.shields.io/coveralls/mbourqui/django-autoslugged.svg%0A%20:target:%20https://coveralls.io/r/mbourqui/django-autoslugged)

![image](https://img.shields.io/travis/mbourqui/django-autoslugged.svg%0A%20:target:%20https://travis-ci.org/mbourqui/django-autoslugged)

![image](https://img.shields.io/pypi/format/django-autoslugged.svg%0A%20:target:%20https://pypi.python.org/pypi/django-autoslugged)

![image](https://img.shields.io/pypi/status/django-autoslugged.svg%0A%20:target:%20https://pypi.python.org/pypi/django-autoslugged)

![image](https://img.shields.io/pypi/v/django-autoslugged.svg%0A%20:target:%20https://pypi.python.org/pypi/django-autoslugged)

![image](https://img.shields.io/pypi/pyversions/django-autoslugged.svg%0A%20:target:%20https://pypi.python.org/pypi/django-autoslugged)

![image](https://img.shields.io/pypi/dd/django-autoslugged.svg%0A%20:target:%20https://pypi.python.org/pypi/django-autoslugged)

![image](https://readthedocs.org/projects/django-autoslug/badge/?version=stable%0A%20:target:%20http://django-autoslug.readthedocs.org/en/stable/)

![image](https://readthedocs.org/projects/django-autoslug/badge/?version=latest%0A%20:target:%20http://django-autoslug.readthedocs.org/en/latest/)

Django-autoslugged is a reusable Django library that provides an
improved slug field which can automatically:

a)  populate itself from another field,
b)  preserve uniqueness of the value and
c)  use custom slugify() functions for better i18n.

The field is highly configurable.

Requirements
============

*Python 2.7, 3.5 or PyPy*.

*Django 1.7.10* or higher.

It may be possible to successfully use django-autoslugged in other
environments but they are not tested.

> **note**
>
> PyPy3 is not officially supported only because there were some
> problems with permissions and \_\_pycache\_\_ on CI unrelated to
> django-autoslugged itself.

Examples
========

A simple example:

``` {.sourceCode .python}
from django.db.models import CharField, Model
from autoslugged import AutoSlugField

class Article(Model):
    title = CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
```

More complex example:

``` {.sourceCode .python}
from django.db.models import CharField, DateField, ForeignKey, Model
from django.contrib.auth.models import User
from autoslugged import AutoSlugField

class Article(Model):
    title = CharField(max_length=200)
    pub_date = DateField(auto_now_add=True)
    author = ForeignKey(User)
    slug = AutoSlugField(populate_from=lambda instance: instance.title,
                         unique_with=['author__name', 'pub_date__month'],
                         slugify=lambda value: value.replace(' ','-'))
```

Documentation
=============

See the [complete documentation](http://django-autoslug.readthedocs.org)
on ReadTheDocs. It is built automatically for the latest version.

Community
=========

This application was initially created by Andy Mikhailenko and then
improved by other developers. They are listed in AUTHORS.rst.

Please feel free to file issues and/or submit patches.

See CONTRIBUTING.rst for hints related to the preferred workflow.

Since the original project
([django-autoslug](<https://github.com/neithere/django-autoslug>)) was
not maintained anymore but I was using it in several projects, I forked
it and renamed it in order to publish a new release on PyPI.

Licensing
=========

Django-autoslugged is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation; either version 3 of the
License, or (at your option) any later version.

Django-autoslugged is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser
General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program; see the file COPYING.LESSER. If not, see [GNU
licenses](http://gnu.org/licenses/).