import os

hashdeep_out_file = "hashdeep.out"

# Check for an already existing directory mapping file. Delete it if it exists.
if os.path.isfile(hashdeep_out_file):
    os.remove(hashdeep_out_file)
    print "Removed existing hashdeep index file " + hashdeep_out_file

# Execute hashdeep recursively on currend work directory.
from subprocess import call
command = "hashdeep -c md5 -v -r -l -W " + hashdeep_out_file + " ."
print "Executing shell command: " + command
call(command.split(' '))
print "Finished computing hashes."


