import os

env_var_name = 'FISEL_KEY'

def package():

    encr_key = os.environ.get(env_var_name)
    if not encr_key:
        print 'ERROR: Encryption key cannot be read from environment variable ' + env_var_name
        return

    gpg_cmd = 'gpg --passphrase ' + encr_key + ' --no-use-agent --cipher-algo AES256 --symmetric '

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

    print "Finished encryption."


directory_map_name = 'directory_mapping.out'
file_hashes_name = 'file_hashes.out'

def unpackage():

    decr_key = os.environ.get(env_var_name)
    if not decr_key:
        print 'ERROR: Decryption key cannot be read from environment variable ' + env_var_name
        return

    gpg_cmd = 'gpg -d --passphrase ' + decr_key + ' --no-use-agent --output '

    # decrypt directory mapping
    exec_command(gpg_cmd + directory_map_name + ' ' + directory_map_name + '.gpg')
    exec_command('rm ' + directory_map_name + '.gpg')

    # decrypt file hashes
    exec_command(gpg_cmd + file_hashes_name + ' ' + file_hashes_name + '.gpg')
    exec_command('rm ' + file_hashes_name + '.gpg')

    for i in os.listdir(os.getcwd()):
        if i.endswith('.tar.gpg'):
            filename = i[:-4]
            # Decrypt file using AES-256
            exec_command(gpg_cmd + filename + ' ' + i)
            # Remove encrypted tar ball 
            exec_command('rm ' + i)
            # Extract tar ball
            exec_command('tar -xf ' + filename)
            # Remove tar ball
            exec_command('rm ' + filename)            
            print 'Decrypted ' + i

    with open(directory_map_name) as dirmap:
        for line in dirmap:
            rename = line.split(' -> ')
            # Restore original folder name
            exec_command_args(['mv', rename[1].strip(), rename[0].strip()])

    # Extract root files to root
    #exec_command('mv root_files/* .')
    #exec_command('rm -d root_files')

    print "Finished decryption."


def exec_command(command):
    exec_command_args(command.split(' '))

def exec_command_args(args):
    from subprocess import call
    #print "Executing shell command: " + command
    call(args)

