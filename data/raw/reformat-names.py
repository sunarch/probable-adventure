#!/usr/bin/env python3

# This file is part of 'Probable Adventure'.
#
# 'Probable Adventure' is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# 'Probable Adventure' is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with 'Probable Adventure'.  If not, see <http://www.gnu.org/licenses/>.

import argparse

# Parse command line arguments

parser = argparse.ArgumentParser(description="Process CLI args.")
parser.add_argument("-m", "--mode", help="check mode", required=True)
parser.add_argument("-p", "--part", help="check mode", required=True)
args = parser.parse_args()

# Constants

FILENAME_NAMES_FIRST_FEMALE = "names-first-female"
FILENAME_NAMES_FIRST_MALE = "names-first-male"
FILENAME_NAMES_LAST = "names-last"

VARNAME_NAMES_FIRST_FEMALE = "first_names_female"
VARNAME_NAMES_FIRST_MALE = "first_names_male"
VARNAME_NAMES_LAST = "last_names"

KEYNAME_NAME = "name"
KEYNAME_FREQUENCY = "freq"
KEYNAME_CUMULATIVE_FREQUENCY = "cumulFreq"
KEYNAME_RANK = "rank"

# Function to determine last line
def determine_last_line(arg_file_name):
    last_line = None
    infile = open(str(arg_file_name) + ".txt", "r")
    for line in infile:
        last_line = line
    infile.close()
    return last_line

# Formatting functions

def format_name(arg_value):
    return_part = '{"'
    return_part += KEYNAME_NAME
    return_part += '": "'
    return_part += arg_value
    return_part += '",'
    return return_part

def format_frequency(arg_value):
    return_part = ' "'
    return_part += KEYNAME_FREQUENCY
    return_part += '": '
    return_part += arg_value
    return_part += ','
    return return_part

def format_cumulative_frequency(arg_value):
    return_part = ' "'
    return_part += KEYNAME_CUMULATIVE_FREQUENCY
    return_part += '": '
    return_part += arg_value
    return_part += ','
    return return_part

def format_rank(arg_value):
    return_part = ' "'
    return_part += KEYNAME_RANK
    return_part += '": '
    return_part += arg_value
    return_part += '}'
    return return_part

def format_line_end(arg_line, arg_last_line):
    if arg_line == arg_last_line:
        return "\n"
    else:
        return ",\n"

# Function to write line format test to console
def test_to_console(arg_file_name):
    print("Reformatting file '" + arg_file_name + "'", end="\n\n")

    # Call to function to determine last line
    last_line = determine_last_line(arg_file_name)

    # Open file
    infile = open(arg_file_name + ".txt", "r")

    # Write lines
    for line in infile:
        print(str(line), end="")

        parts = line.split()

        print(format_name(parts[0]), end="")
        print(format_frequency(parts[1]), end="")
        print(format_cumulative_frequency(parts[2]), end="")
        print(format_rank(parts[3]), end="")

        print(format_line_end(line, last_line), end="")

    # Print last line
    print("", end="\n")
    print("Last line as determined on start:", end="\n")
    print(last_line, end="")
    print("", end="\n")

    # Close file
    infile.close()

# Function to write final full format to file
def write_to_file(arg_file_name, arg_var_name):
    print("Reformatting file '" + arg_file_name + "'", end="\n\n")

    # Call to function to determine last line
    last_line = determine_last_line(arg_file_name)

    # Open files
    print("Opening files", end="\n")
    infile = open(str(arg_file_name) + ".txt", "r")
    outfile =  open(str(arg_file_name) + ".py", "w")

    # Write intro part
    print("Writing intro part", end="\n")

    outfile.write("# This file is part of 'Probable Adventure'.\n")
    outfile.write("#\n")
    outfile.write("# 'Probable Adventure' is free software: you can redistribute it and/or modify\n")
    outfile.write("# it under the terms of the GNU General Public License as published by\n")
    outfile.write("# the Free Software Foundation, either version 3 of the License, or\n")
    outfile.write("# (at your option) any later version.\n")
    outfile.write("#\n")
    outfile.write("# 'Probable Adventure' is distributed in the hope that it will be useful,\n")
    outfile.write("# but WITHOUT ANY WARRANTY; without even the implied warranty of\n")
    outfile.write("# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n")
    outfile.write("# GNU General Public License for more details.\n")
    outfile.write("#\n")
    outfile.write("# You should have received a copy of the GNU General Public License\n")
    outfile.write("# along with 'Probable Adventure'.  If not, see <http://www.gnu.org/licenses/>.\n")
    outfile.write("\n")
    outfile.write("#  From the U.S. Census Bureau (1990 census)\n")
    outfile.write("\n")

    # Write list start
    outfile.write(arg_var_name)
    outfile.write(" = [\n")
    outfile.write("\n")

    # Write lines
    print("Writing lines", end="\n")

    for line in infile:
        print(".", end="")

        parts = line.split()

        outfile.write(format_name(parts[0]))
        outfile.write(format_frequency(parts[1]))
        outfile.write(format_cumulative_frequency(parts[2]))
        outfile.write(format_rank(parts[3]))

        outfile.write(format_line_end(line, last_line))

    print("", end="\n")

    # Write list end
    outfile.write("\n")
    outfile.write("]\n")

    # Close files
    print("Closing files", end="\n\n")
    infile.close()
    outfile.close()

# Action

print("Starting...", end="\n\n")

if args.mode in ["file", "write"]:

    if args.part == "female":
        write_to_file(FILENAME_NAMES_FIRST_FEMALE, VARNAME_NAMES_FIRST_FEMALE)
    elif args.part == "male":
        write_to_file(FILENAME_NAMES_FIRST_MALE, VARNAME_NAMES_FIRST_MALE)
    elif args.part == "first":
        write_to_file(FILENAME_NAMES_FIRST_FEMALE, VARNAME_NAMES_FIRST_FEMALE)
        write_to_file(FILENAME_NAMES_FIRST_MALE, VARNAME_NAMES_FIRST_MALE)
    elif args.part == "last":
        write_to_file(FILENAME_NAMES_LAST, VARNAME_NAMES_LAST)
    elif args.part == "all":
        write_to_file(FILENAME_NAMES_FIRST_FEMALE, VARNAME_NAMES_FIRST_FEMALE)
        write_to_file(FILENAME_NAMES_FIRST_MALE, VARNAME_NAMES_FIRST_MALE)
        write_to_file(FILENAME_NAMES_LAST, VARNAME_NAMES_LAST)
    else:
        print("ERROR: Bad option value for part")

elif args.mode in ["console", "test"]:

    if args.part == "female":
        test_to_console(FILENAME_NAMES_FIRST_FEMALE)
    elif args.part == "male":
        test_to_console(FILENAME_NAMES_FIRST_MALE)
    elif args.part == "first":
        test_to_console(FILENAME_NAMES_FIRST_FEMALE)
        test_to_console(FILENAME_NAMES_FIRST_MALE)
    elif args.part == "last":
        test_to_console(FILENAME_NAMES_LAST)
    elif args.part == "all":
        test_to_console(FILENAME_NAMES_FIRST_FEMALE)
        test_to_console(FILENAME_NAMES_FIRST_MALE)
        test_to_console(FILENAME_NAMES_LAST)
    else:
        print("ERROR: Bad option value for part")

else:
    print("ERROR: Bad option value for mode")

print("Done.", end="\n")
