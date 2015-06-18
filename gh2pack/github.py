# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Matwey V. Kornilov <matwey.kornilov@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program (see the file COPYING); if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

import requests

class GitHub(object):
	def __init__(self):
		self._verify = '/etc/ssl/ca-bundle.pem'
		self._headers = {'accept': 'application/vnd.github.drax-preview+json'}
		self._api = 'https://api.github.com'

	def get_repo(self, owner, repo):	
		r = requests.get('{0}/repos/{1}/{2}'.format(self._api, owner, repo), verify=self._verify, headers=self._headers)
		return r.json()
