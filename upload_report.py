import requests
import json
import argparse


url_api = "http://18.218.244.166:8080/api/v2/{method}"
api_key = "Token edaf1740e048924e2f817fb6436a803b690c6900"
 
    
def upload_report(file_report, type_scan):
    headers = {
        'accept' : 'application/json',
        'Authorization' : api_key 
    }
    
    reports = {
        'file': open(file_report, 'rb')
    }
    
    body = {
        'minimum_severity' : 'Info',
        'active': True,
        'verified': True,
        'scan_type': type_scan,
        'close_old_findings': False,
        'test_title': 'pruebaFG',
        'product_name': 'WebGoat',
        'engagement_name': 'bryan'
    } 
     
    t = requests.post(url_api.format(method='import-scan/'), data = body, files = reports, headers = headers, verify = False)

    print(t.status_code)
    if t.status_code == 201:
        print(json.dumps(t.json(), indent=4))
        
 
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', dest='file', help='Nombre del reporte', required=True)
    parser.add_argument('--type-scan', '-t', dest='type_scan', help='Nombre del escaner', required=True)
    
    args = parser.parse_args()
    
    upload_report(args.file, args.type_scan)


