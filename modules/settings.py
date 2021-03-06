#!/usr/bin/env python
#############################################################
# ubi_reader
# (c) 2013 Jason Pruitt (jrspruitt@gmail.com)
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

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#############################################################

import os

output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'output')

error_action = True             # if 'exit' on any error exit program.
fatal_traceback = False          # Print traceback on fatal errors.

ignore_block_errors = False      # Ignore block errors.
logging_on = False               # Print debug info on.
logging_on_verbose = False      # Print verbose debug info on.

use_dummy_socket_file = False   # Create regular file place holder.
