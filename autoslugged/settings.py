# coding: utf-8
#
#  Copyright (c) 2008—2015 Andy Mikhailenko
#
#  This file is part of django-autoslugged.
#
#  django-autoslugged is free software under terms of the GNU Lesser
#  General Public License version 3 (LGPLv3) as published by the Free
#  Software Foundation. See the file README for copying conditions.
#
"""
Django settings that affect django-autoslugged:

`AUTOSLUG_SLUGIFY_FUNCTION`
  Allows to define a custom slugifying function.

  The function can be repsesented as string or callable, e.g.::

      # custom function, path as string:
      AUTOSLUG_SLUGIFY_FUNCTION = 'some_app.slugify_func'

      # custom function, callable:
      AUTOSLUG_SLUGIFY_FUNCTION = some_app.slugify_func

      # custom function, defined inline:
      AUTOSLUG_SLUGIFY_FUNCTION = lambda slug: 'can i haz %s?' % slug

  If no value is given, default value is used.

  Default value is one of these depending on availability in given order:

  * `unidecode.unidecode()` if Unidecode_ is available;
  * `pytils.translit.slugify()` if pytils_ is available;
  * `django.template.defaultfilters.slugify()` bundled with Django.

  django-autoslugged also ships a couple of slugify functions that use
  the translitcodec_ Python library, e.g.::

     # using as many characters as needed to make a natural replacement
     AUTOSLUG_SLUGIFY_FUNCTION = 'autoslugged.utils.translit_long'

     # using the minimum number of characters to make a replacement
     AUTOSLUG_SLUGIFY_FUNCTION = 'autoslugged.utils.translit_short'

     # only performing single character replacements
     AUTOSLUG_SLUGIFY_FUNCTION = 'autoslugged.utils.translit_one'

.. _Unidecode: http://pypi.python.org/pypi/Unidecode
.. _pytils: http://pypi.python.org/pypi/pytils
.. _translitcodec: http://pypi.python.org/pypi/translitcodec

`AUTOSLUG_MODELTRANSLATION_ENABLE`
  Django-autoslugged support of modeltranslation_ is still experimental.
  If you wish to enable it, please set this option to `True` in your project
  settings.  Default is `False`.

.. _modeltranslation: http://django-modeltranslation.readthedocs.org

"""
from django.conf import settings

try:
    from django.urls.utils import get_callable
except ImportError:  # < django 2.0
    from django.core.urlresolvers import get_callable

# use custom slugifying function if any
slugify_function_path = getattr(settings, 'AUTOSLUGGED_SLUGIFY_FUNCTION', 'autoslugged.utils.slugify')
slugify = get_callable(slugify_function_path)

# enable/disable modeltranslation support
autoslug_modeltranslation_enable = getattr(settings, 'AUTOSLUGGED_MODELTRANSLATION_ENABLE', False)
