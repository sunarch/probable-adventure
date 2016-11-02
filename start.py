#!/usr/bin/env python3

'''
This file is part of 'Probable Adventure'.

'Probable Adventure' is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

'Probable Adventure' is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with 'Probable Adventure'.  If not, see <http://www.gnu.org/licenses/>.
'''

# Imports

import argparse

# Parse command line arguments

parser = argparse.ArgumentParser(description="Process CLI args.")
parser.add_argument("-m", "--mode", help="check mode", required=False)
args = parser.parse_args()

# MAIN #

if __name__ == '__main__':

    if args.mode == "a":
        print("a.")
