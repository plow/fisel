import os

for i in os.listdir(os.getcwd()):
    if os.path.isdir(i):

        # Create tar ball for each directory.
        from subprocess import call
        command = "tar -cf " + i + ".tar " + i + "/"
        print "Executing shell command: " + command
        call(command.split(' '))

print "Finished creating tar balls."

