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

__doc__ = 'Generate distribution packages from GitHub'
__author__ = 'Matwey V. Kornilov <matwey.kornilov@gmail.com>'
__version__ = '0.1.0'

import argparse
import jinja2
import os
import pprint

import gh2pack.github

github = gh2pack.github.GitHub()

def show(args):
	info = github.get_repo(args.owner, args.repo)
	pprint.pprint(info)

def generate(args):
	template_path = ["templates"]

	if not args.filename:
		args.filename = args.template

	info = github.get_repo(args.owner, args.repo)
	if "language" in info:
		template_path.insert(0, os.path.join("templates", info["language"]))

	env = jinja2.Environment(loader=jinja2.ChoiceLoader([jinja2.PackageLoader("gh2pack", x) for x in template_path]))
	template = env.get_template(args.template)
	outfile = open(args.filename, 'wb')
	outfile.write(template.render(info).encode('utf-8'))

def main():
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument('--version', action='version', version='%(prog)s {0}'.format(__version__))
	subparsers = parser.add_subparsers(title='commands')
	
	parser_show = subparsers.add_parser('show', help='show metadata for package')
	parser_show.add_argument('owner', help='repo owner')
	parser_show.add_argument('repo', help='repo name')
	parser_show.set_defaults(func=show)
	
	parser_generate = subparsers.add_parser('generate', help='generate RPM spec or DEB dsc file for a package')
	parser_generate.add_argument('owner', help='repo owner')
	parser_generate.add_argument('repo', help='repo name')
	parser_generate.add_argument('-t', '--template', help='file template')
	parser_generate.add_argument('-f', '--filename', help='spec filename (optional)')
	parser_generate.set_defaults(func=generate)

	parser_help = subparsers.add_parser('help', help='show this help')
	parser_help.set_defaults(func=lambda args: parser.print_help())

	args = parser.parse_args()
	args.func(args)
