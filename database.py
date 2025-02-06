import sqlite3

DB_NAME = "data/ephemerides.db"

###print(sqlite3.version)

def create_db():
    """Create SQLite database and tables if they do not exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Table for planet data
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS planet (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        mean_radius_km REAL,
        density_g_cm3 REAL,
        mass_x10e23_kg REAL,
        flattening REAL,
        volume_x10e10_km3 REAL,
        sidereal_rotation_period_hr REAL,
        mean_temperature_K REAL,
        equatorial_gravity_m_s2 REAL,
        atmospheric_pressure_bar REAL
    )
    """)

    # Table for ephemerides
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ephemerides (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        time TEXT,
        ra_hms TEXT,
        dec_dms TEXT,
        distance_au REAL,
        velocity_km_s REAL,
        solar_elongation REAL,
        phase_angle REAL
    )
    """)
    
    conn.commit()
    conn.close()

def insert_planet():
    """Insert Mars' physical data into the database (if not already exists)."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT OR IGNORE INTO planet (name, mean_radius_km, density_g_cm3, mass_x10e23_kg, 
                                  flattening, volume_x10e10_km3, sidereal_rotation_period_hr, 
                                  mean_temperature_K, equatorial_gravity_m_s2, atmospheric_pressure_bar) 
    VALUES ('Mars', 3389.92, 3.933, 6.4171, 1/169.779, 16.318, 24.622962, 210, 3.71, 0.0056)
    """)
    
    conn.commit()
    conn.close()

def insert_ephemerides(data):
    """Insert ephemerides data into the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    for row in data:
        try:
            cursor.execute("""
                INSERT INTO ephemerides (date, time, ra_hms, dec_dms, distance_au, velocity_km_s, solar_elongation, phase_angle)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, row)
        except Exception as e:
            print(f"Error inserting data: {e}")
            continue
    
    conn.commit()
    conn.close()

