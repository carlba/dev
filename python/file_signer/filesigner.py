import M2Crypto
import re
import sys

from exceptions import IOError
from exceptions import Exception


class FileSigner(object):
    def __init__(self, key_file, cert_chain_file,cert_file):
        self.key_file = key_file
        self.cert_chain_file = cert_chain_file
        self.cert_file = cert_file
    
    def load(self):
        self.stack_certs_from_chain(self.cert_chain_file)
        self.create_signer(self.key_file, self.cert_file)
    
    def stack_certs_from_chain(self, cert_chain_file):
        certstack = M2Crypto.X509.X509_Stack()
        
        
        with open(cert_chain_file, "rb") as textfile:
            certdata = textfile.read()
        
        certs = re.finditer(r'-----BEGIN CERTIFICATE-----.*?-----END CERTIFICATE-----', certdata, re.S)
        
        is_match = False
        for match in certs:
            is_match = True
            certstack.push(M2Crypto.X509.load_cert_string(match.group(0)))
        
        if not is_match:
            raise Exception("The certificate chain-file doesn't contain any certs")
        
        self.certstack = certstack
    
    def create_signer(self, key_file, cert_file):
        self.signer= M2Crypto.SMIME.SMIME()
        self.signer.set_x509_stack(self.certstack)
        self.signer.load_key(key_file, cert_file)
    
    def sign(self,cleartext_file_path,output_file_path):
        
        with open(cleartext_file_path) as cleartext_file:
            cleartext = cleartext_file.read()
        
        print cleartext
        
        
        
        
            
        membuff = M2Crypto.BIO.MemoryBuffer(cleartext)
        p7 = self.signer.sign(membuff, flags=M2Crypto.SMIME.PKCS7_SIGNED_ENVELOPED)
        out = M2Crypto.BIO.MemoryBuffer()
        p7.write_der(out)
        
        with open(output_file_path,"w+") as output_file:
            output_file.write(out.getvalue())
        
            

if __name__ == "__main__":
    fs = FileSigner( key_file = "tigger.birdstep.com.key",
                     cert_chain_file = "test.pem",
                     cert_file = 'tigger_birdstep_com.crt')
    
    fs.load()
    fs.sign("TestConfig.mobileconfig", "signed.mobileconfig")

