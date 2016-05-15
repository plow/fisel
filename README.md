# fisel
File System Encryption Layer

A set of Python scripts wich recursively encrypt a whole file system directory such that it can be safely copied e.g. to a public cloud storage without relinquish privacy. The encryption ensures that not even the storage provider can analyse your data - neither the the directory structure, nor the filenames, nor the file contents.

## Usage

Encrypt a file:

``export FISEL_KEY=`cat /path/to/encr.key` `` <br />
``cd /path/to/folder`` <br />
``python /my/fisel/fisel.py``

Decrypt a file:

``gpg -d --passphrase `cat /path/to/encr.key` --output out_file.tar --no-use-agent ngiynzmz.tar.gpg``
