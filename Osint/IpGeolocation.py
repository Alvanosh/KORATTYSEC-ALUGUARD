import requests

def main(ip):
    try:
        response = requests.get(f"https://geolocation-db.com/json/{ip}&position=true").json()
        print(f'County Code : {response.get("country_code")}')
        print(f'Country Name : {response.get("country_name")}')
        print(f'City Name : {response.get("city")}')
        print(f'Postal Code : {response.get("postal")}')
        print(f'Latitude : {response.get("latitude")}')
        print(f'Longityde  : {response.get("longitude")}')
        print(f'State : {response.get("state")}')
        print(response)
    except Exception as e:
        print(f"Error in Geolocation : {e}")
        

    
