import csv
import requests
import time
def busqueda(folio):
    url = f"https://infracciones.lapaz.gob.mx/infracciones/json?f=getList&q={folio}"
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.7",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://infracciones.lapaz.gob.mx/infracciones/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"'
    }

    response = requests.get(url, headers=headers)
    time.sleep(1)

    if response.status_code == 200:
        size = len(response.json())

        if size == 0:
            return "no se encontro"
        elif size == 1:
            print(type(response.json()[0]['status'])) 
            print(response.json()[0]['status']) 
            if response.json()[0]['status'] == 'P':
                return "pagado"
            elif response.json()[0]['status'] == 'C':
                return "cancelado"
            else:
                return "sin pago"
        else: return "duplicado"

    else:
        return f"Error: {response.status_code}"

def modificador_csv():
    with open('archivo.csv', mode='r', newline='') as infile:
        reader = csv.DictReader(infile)
        rows = []    
        for row in reader:
            folio = list(row.values())[0]
            print(folio)
            row['status'] = busqueda(folio)
            rows.append(row)

    with open('archivo_verificado.csv', mode='w', newline='') as outfile:
        fieldnames = reader.fieldnames + ['status']
        
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        writer.writerows(rows)

    print("CSV modificado con éxito.")
modificador_csv()
