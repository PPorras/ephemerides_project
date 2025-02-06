import sqlite3

DB_NAME = "data/ephemerides.db"

def get_planet_data():
    """Retrieve Mars' physical data from the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM planet WHERE name = 'Mars'")
    planet = cursor.fetchone()
    
    conn.close()
    
    if planet:
        return {
            "id": planet[0],
            "name": planet[1],
            "mean_radius_km": planet[2],
            "density_g_cm3": planet[3],
            "mass_x10e23_kg": planet[4],
            "flattening": planet[5],
            "volume_x10e10_km3": planet[6],
            "sidereal_rotation_period_hr": planet[7],
            "mean_temperature_K": planet[8],
            "equatorial_gravity_m_s2": planet[9],
            "atmospheric_pressure_bar": planet[10]
        }
    else:
        return None

def get_all_ephemerides():
    """Retrieve all ephemerides from the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM ephemerides")
    ephemerides = cursor.fetchall()
    
    conn.close()
    
    return ephemerides

def get_ephemerides_by_date(start_date, end_date):
    """Retrieve ephemerides within a specific date range."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT * FROM ephemerides
        WHERE date BETWEEN ? AND ?
        ORDER BY date, time
    """, (start_date, end_date))
    
    ephemerides = cursor.fetchall()
    
    conn.close()
    
    return ephemerides

def get_latest_ephemerides():
    """Retrieve the most recent ephemerides entry."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM ephemerides ORDER BY date DESC, time DESC LIMIT 1")
    latest_entry = cursor.fetchone()
    
    conn.close()
    
    return latest_entry

if __name__ == "__main__":
    # Example usage
    print("Mars Planet Data:")
    print(get_planet_data())

    print("\nLatest Ephemerides Entry:")
    print(get_latest_ephemerides())

