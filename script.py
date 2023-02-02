import os
import platform
import argparse

parser = argparse.ArgumentParser(description='Scannear um site Wordpress com a ferramente WPScan')
parser.add_argument('-u', '--url', type=str, required=True, help='URL do site. É preciso que seja a URL final, se houver redirects pelo caminho o WPScan não funciona.')
parser.add_argument('-api', '--api-token', type=str, required=True, help='Api token da sua conta')
args = parser.parse_args()

if platform.system() == "Ubuntu":
    os.system("sudo apt-get update && sudo apt-get install git ruby ruby-dev libxml2 libxml2-dev libxslt1-dev libxslt1-dev libcurl4-openssl-dev make -y")
    os.system("sudo gem install bundler && bundle install --without test")
elif platform.system() == "CentOS":
    os.system("sudo yum install git ruby ruby-devel libxml2 libxml2-devel libxslt libxslt-devel -y")
    os.system("sudo gem install bundler && bundle install --without test")
else:
    print("Unsupported operating system")
    exit(1)

if args.api_token:
    os.system(f"wpscan --url {args.url} --api-token {args.api_token}")
else:
    os.system(f"wpscan --url {args.url}")
