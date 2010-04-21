# -*- coding: utf-8 -*-
# $Id$
#
# Blip! (http://blip.pl) communication library.
# Author: Marcin Sztolcman <marcin /at/ urzenia /dot/ net>
# Version: 0.02.05
# Copyright: (r) 2009 Marcin Sztolcman
# License: http://opensource.org/licenses/gpl-license.php GNU Public License v.2

import os.path

from _utils import arr2qstr, make_post_data

def create (**args):
    """ Create new private message. """

    if not args.get ('body') or not args.get ('user'):
        raise ValueError ('Private_message body or recipient is missing.')

    fields = {
        'private_message[body]':      args['body'],
        'private_message[recipient]': args['user'],
    }
    if args.get ('image') and os.path.isfile (args['image']):
        fields['private_message[picture]'] = (args['image'], args['image'], )

    data, boundary = make_post_data (fields)

    return dict (
        url         = '/private_messages',
        method      = 'post',
        data        = data,
        boundary    = boundary,
    )

def read (**args):
    """ Read user's private messages. """

    if args.get ('since_id'):
        url = '/private_messages/since/' + str (args['since_id'])
    elif args.get ('id'):
        url = '/private_messages/' + str (args['id'])
    else:
        url = '/private_messages'

    params = dict ()
    params['limit']     = args.get ('limit', 10)
    params['offset']    = args.get ('offset', 0)
    params['include']   = ','.join (args.get ('include', ''))
    params              = arr2qstr (params)

    if params:
        url += '?' + params

    return dict (
        url         = url,
        method      = 'get',
    )

def delete (**args):
    """ Delete specified private message. """

    if not args.get ('id'):
        raise ValueError ('Private_message ID is missing.')

    return dict (
        url         = '/private_messages/' + str (args['id']),
        method      = 'delete',
    )

