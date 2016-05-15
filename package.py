import os

env_var_name = 'FISEL_KEY'

def package():

    encr_key = os.environ.get(env_var_name)
    if not encr_key:
        print 'ERROR: Encryption key cannot be read from environment variable ' + env_var_name
        return

    gpg_cmd = 'gpg --passphrase ' + encr_key + ' -c --no-use-agent --cipher-algo AES256 --symmetric '

    for i in os.listdir(os.getcwd()):
        if os.path.isdir(i):

            # Create tar ball for each directory
            exec_command('tar -cf ' + i + '.tar ' + i)

            # Remove original directory
            exec_command('rm -rf ' + i)

            # Symmetrically encrypt tar ball using AES-256
            exec_command(gpg_cmd + i + '.tar')

            # Remove unencrypted tar ball
            exec_command('rm ' + i + '.tar')

        else:
            # Symmetrically encrypt file using AES-256
            exec_command(gpg_cmd + i)

            # Remove unencrypted tar ball 
            exec_command('rm ' + i)

        print 'Encrypted ' + i

    print "Finished."

def exec_command(command):
    from subprocess import call
    #print "Executing shell command: " + command
    call(command.split(' '))

