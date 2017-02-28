# coding: utf-8

import datetime

from ckan.plugins.toolkit import Invalid
from ckan.common import _

def xsd_date(date_text):
    if len(date_text) > 0:
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
        except ValueError:
            raise Invalid(_('Date format incorrect'))
    return date_text

