import requests
##import certifi
from database import insert_ephemerides



def get_ephemerides():
    """Fetch ephemerides data from JPL Horizons API and format it."""
    params = {
        "format": "json",
        "COMMAND": "'499'",  # Mars
        "EPHEM_TYPE": "OBSERVER",
        "CENTER": "'500'",  # Earth
        "START_TIME": "'2025-06-01'",
        "STOP_TIME": "'2025-06-05'",
        "STEP_SIZE": "'1 d'",
        "QUANTITIES": "'1,20,23,24'"  # Position, distance, magnitude
    }
    url = "https://ssd.jpl.nasa.gov/api/horizons.api"
    
    ##response = requests.get(url, params=params, verify=True, timeout=10, verify=certifi.where())
    response = requests.get(url, params=params, verify=False)
    if response.status_code == 200:
        data = response.json()
        if "result" in data:
            return parse_ephemerides(data["result"])
        else:
            raise ValueError("Unexpected response format")
    else:
        raise ConnectionError(f"Error fetching data: {response.status_code}")

def parse_ephemerides(raw_data):
    """Parse the ephemerides data and extract relevant fields."""
    lines = raw_data.splitlines()
    data = []

    in_data_section = False
    for line in lines:
        if "$$SOE" in line:  # Start of data
            in_data_section = True
            continue
        if "$$EOE" in line:  # End of data
            break
        
        if in_data_section:
            cols = line.split()
            if len(cols) < 12:  # Ensure enough columns are present
                continue  

            try:
                date = cols[0]
                time = cols[1]
                ra_hms = " ".join(cols[2:5])  # Right Ascension (HH MM SS)
                dec_dms = " ".join(cols[5:8])  # Declination (DD MM SS)

                # Ensure numeric values only
                distance_au = float(cols[8])
                velocity_km_s = float(cols[9])
                solar_elongation = float(cols[10])

                # The phase angle might be at index 11 or 12, depending on the presence of '/T'
                phase_angle_index = 11 if cols[11] not in ["/T", "/L"] else 12
                phase_angle = float(cols[phase_angle_index])

                data.append((date, time, ra_hms, dec_dms, distance_au, velocity_km_s, solar_elongation, phase_angle))

            except ValueError as e:
                print(f"Skipping line due to parsing error: {line} - Error: {e}")
                continue  # Skip invalid rows
    
    return data


#def parse_ephemerides(raw_data):
#    """Parse the ephemerides data and extract relevant fields."""
#    lines = raw_data.splitlines()
#    data = []
#
#    in_data_section = False
#    for line in lines:
#        if "$$SOE" in line:  # Start of data
#            in_data_section = True
#            continue
#        if "$$EOE" in line:  # End of data
#            break
#        
#        if in_data_section:
#            cols = line.split()
#            if len(cols) < 8:
#                continue  # Skip incomplete lines
#            
#            date = cols[0]
#            time = cols[1]
#            ra_hms = cols[2] + " " + cols[3] + " " + cols[4]
#            dec_dms = cols[5] + " " + cols[6] + " " + cols[7]
#            distance_au = float(cols[8])
#            velocity_km_s = float(cols[9])
#            solar_elongation = float(cols[10])
#            phase_angle = float(cols[11])
#            
#            data.append((date, time, ra_hms, dec_dms, distance_au, velocity_km_s, solar_elongation, phase_angle))
#    
#    return data

def fetch_and_store_ephemerides():
    """Fetch ephemerides and store them in the database."""
    try:
        ephemerides = get_ephemerides()
        if ephemerides:
            insert_ephemerides(ephemerides)
            print("Ephemerides data inserted into database.")
        else:
            print("No ephemerides data retrieved.")
    except Exception as e:
        print(f"Error: {e}")

