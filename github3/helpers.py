# -*- coding: utf-8 -*-

"""
github3.helpers
~~~~~~~~~~~~~~~~

This module provides various helper functions to the rest of the package.
"""

import inspect
from datetime import datetime

from dateutil.parser import parse as parse_datetime


def is_collection(obj):
    """Tests if an object is a collection."""

    col = getattr(obj, '__getitem__', False)
    val = False if (not col) else True

    if isinstance(obj, basestring):
        val = False

    return val


def key_diff(source, update, pack=False):
    """Given two dictionaries, returns a list of the changed keys."""

    source = dict(source)
    update = dict(update)

    changed = []

    for (k, v) in source.items():
        u_v = update.get(k)

        if (v != u_v) and (u_v is not None):
            changed.append(k)

    if pack is False:
        return changed

    d = dict()

    for k in changed:
        d[k] = update[k]

    return d


# from arc90/python-readability-api
def to_python(obj,
    in_dict,
    str_keys=None,
    date_keys=None,
    int_keys=None,
    object_map=None,
    bool_keys=None, **kwargs):
    """Extends a given object for API Consumption.

    :param obj: Object to extend.
    :param in_dict: Dict to extract data from.
    :param string_keys: List of in_dict keys that will be extracted as strings.
    :param date_keys: List of in_dict keys that will be extrad as datetimes.
    :param object_map: Dict of {key, obj} map, for nested object results.
    """

    d = dict()

    if str_keys:
        for in_key in str_keys:
            d[in_key] = in_dict.get(in_key)

    if date_keys:
        for in_key in date_keys:
            in_date = in_dict.get(in_key)
            try:
                out_date = datetime.strptime(in_date, '%Y-%m-%dT%H:%M:%SZ')
            except TypeError:
                out_date = None

            d[in_key] = out_date

    if int_keys:
        for in_key in int_keys:
            if (in_dict is not None) and (in_dict.get(in_key) is not None):
                d[in_key] = int(in_dict.get(in_key))

    if bool_keys:
        for in_key in bool_keys:
            if in_dict.get(in_key) is not None:
                d[in_key] = bool(in_dict.get(in_key))

    if object_map:
        for (k, v) in object_map.items():
            if in_dict.get(k):
                d[k] = v.new_from_dict(in_dict.get(k))

    obj.__dict__.update(d)
    obj.__dict__.update(kwargs)

    # Save the dictionary, for write comparisons.
    obj._cache = d
    obj.__cache = in_dict

    return obj


# from arc90/python-readability-api
def to_api(in_dict, int_keys=None, date_keys=None, bool_keys=None):
    """Extends a given object for API Production."""

    # Cast all int_keys to int()
    if int_keys:
        for in_key in int_keys:
            if (in_key in in_dict) and (in_dict.get(in_key, None) is not None):
                in_dict[in_key] = int(in_dict[in_key])

    # Cast all date_keys to datetime.isoformat
    if date_keys:
        for in_key in date_keys:
            if (in_key in in_dict) and (in_dict.get(in_key, None) is not None):

                _from = in_dict[in_key]

                if isinstance(_from, basestring):
                    dtime = parse_datetime(_from)

                elif isinstance(_from, datetime):
                    dtime = _from

                in_dict[in_key] = dtime.isoformat()

            elif (in_key in in_dict) and in_dict.get(in_key, None) is None:
                del in_dict[in_key]

    # Remove all Nones
    for k, v in in_dict.items():
        if v is None:
            del in_dict[k]

    return in_dict



# from kennethreitz/showme
def get_scope(f, args=None):
    """Get scope of given function for Exception scopes."""

    if args is None:
        args=list()

    scope = inspect.getmodule(f).__name__
    # guess that function is a method of it's class
    try:
        if f.func_name in dir(args[0].__class__):
            scope += '.' + args[0].__class__.__name__
            scope += '.' + f.__name__
        else:
            scope += '.' + f.__name__
    except IndexError:
        scope += '.' + f.__name__

    # scrub readability.models namespace
    scope = scope.replace('readability.api.', '')

    return scope