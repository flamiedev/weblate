# -*- coding: utf-8 -*-
#
# Copyright © 2012 - 2013 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <http://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from django.core.management.base import BaseCommand
from trans.requirements import get_versions
from weblate import GIT_VERSION


class Command(BaseCommand):
    help = 'lists versions of required software components'

    def handle(self, *args, **options):
        '''
        Prints versions of dependencies.
        '''
        print ' * Weblate %s' % GIT_VERSION
        for version in get_versions():
            print ' * %s %s' % (
                version[0],
                version[2],
            )
