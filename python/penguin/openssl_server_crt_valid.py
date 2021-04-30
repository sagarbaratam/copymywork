
from VIPvalidation import validate
import ssl


def crt_format():
    cert_file_name=str(input("Enter the location: ")) #sys.argv  #'/etc/httpd/ssl/ssl.crt'
    cert = ssl._ssl._test_decode_cert(cert_file_name)
    cert_dict = []
    cert_dict.append(cert)
    return validate.display(cert_dict)

crt_format()
#validate.display(cert_dict) 


#code = input("Enter Python Expression: ")
#exec(code)




