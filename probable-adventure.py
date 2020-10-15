# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


# imports ######################################################################

import argparse

# parse command line arguments #################################################

parser = argparse.ArgumentParser(description="Process CLI args.")
parser.add_argument("-m", "--mode", help="check mode", required=False)
args = parser.parse_args()

# MAIN #########################################################################

if __name__ == '__main__':

    if args.mode == "a":
        print("a.")

# END ##########################################################################
