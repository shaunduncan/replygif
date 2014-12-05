"""
replygif.py - API client for replygif.net
"""
from collections import namedtuple
from itertools import ifilter

import requests

REPLYGIF_API_ENDPOINT = 'http://replygif.net/api'
REPLYGIF_API_KEY = '39YAprx5Yi'

# Valid operators
AND = 'and'
OR = 'or'
NOT = 'not'
OPERATORS = (AND, OR, NOT)

# Data types
Gif = namedtuple('Gif', ('id', 'caption', 'file', 'tags', 'url'))
Reply = namedtuple('Reply', ('id', 'title', 'url', 'count'))


def _base_params(**kwargs):
    base = {'api-key': REPLYGIF_API_KEY}
    base.update(kwargs)
    return base


def _make_gifs_params(name, value, operator):
    params = {}

    if isinstance(value, list):
        value = ','.join(value)
    params[name] = value

    if operator in OPERATORS:
        params['{0}-operator'.format(name)] = operator

    return params


def _filter(data):
    copy = data.copy()
    for key, value in ifilter(lambda x: not x[1], data.iteritems()):
        del copy[key]
    return copy


def gifs(id=None, tag=None, tag_operator=None, reply=None, reply_operator=None):
    if not any((id, tag, reply)):
        raise AssertionError('Requesting gifs must have at least one id, tag, or reply')

    # Request params and endpoint
    endpoint = '{0}/gifs'.format(REPLYGIF_API_ENDPOINT)
    params = _base_params(id=id)

    if tag:
        params.update(_make_gifs_params('tag', tag, tag_operator))

    if reply:
        params.update(_make_gifs_params('reply', reply, reply_operator))

    resp = requests.get(endpoint, params=_filter(params))
    return [Gif(**data) for data in resp.json()]


def replies():
    endpoint = '{0}/replies'.format(REPLYGIF_API_ENDPOINT)
    return [Reply(**data) for data in requests.get(endpoint, params=_base_params()).json()]
