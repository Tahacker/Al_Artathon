import sys , os , argparse , random , time , re
import requests


def print_logo():
    clear = "\x1b[0m"
    colors = [34 , 37]

    x = '''
	==================================
	|            WTA_95              |
	|--------------------------------|
	|          AI Artathon           |
	|--------------------------------|
	'''
    for N , line in enumerate ( x.split ( "\n" ) ):
        sys.stdout.write ( "\x1b[1;%dm%s%s\n" % (random.choice ( colors ) , line , clear) )
        time.sleep ( 0.03 )


def self():
    self.r = '\033[31m'
    self.g = '\033[32m'
    self.y = '\033[33m'
    self.b = '\033[34m'
    self.m = '\033[35m'
    self.c = '\033[36m'
    self.w = '\033[37m'
    self.rr = '\033[39m'



def arta():
    self.y = '\033[33m'
    image_url = raw_input (self.y + "Your image File => " )
    style_url = raw_input ( self.y +"your Style => " )
    r = requests.post (
        "https://api.deepai.org/api/fast-style-transfer" ,
        files={
            'content': open ( image_url , 'rb' ) ,
            'style': open ( style_url , 'rb' ) ,
        } ,
        headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    )
    print(r.json ( ))

if __name__ == '__main__':
    print_logo ( )
    arta ( )
    self ( )
    
