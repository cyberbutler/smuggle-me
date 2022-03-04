# smuggle-me
A Python HTML Smuggling 
```bash
python3 smuggle-me.py -h
usage: smuggle-me.py [-h] -p PAYLOAD [-t TEMPLATE] [-m MIMETYPE] [-o OUTPUT] [--filename FILENAME] [-e {xor,rc4,plaintext}] [-k KEY]

Generate an HTML Smuggled Delivery Payload

optional arguments:
  -h, --help            show this help message and exit
  -p PAYLOAD, --payload PAYLOAD
                        The payload to smuggle in the resulting HTML file
  -t TEMPLATE, --template TEMPLATE
  -m MIMETYPE, --mimetype MIMETYPE
                        Force the mimetype of the file
  -o OUTPUT, --output OUTPUT
                        Write the output to a file, default is STDOUT
  --filename FILENAME   The filename to save the payload as on the victim's filesystem. If not specified, will use the payload name
  -e {xor,rc4,plaintext}, --encrypt {xor,rc4,plaintext}
                        Encrypt using one of the available encryption modules
  -k KEY, --key KEY     Encrytpion Key
```
