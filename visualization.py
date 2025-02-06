import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_NAME = "data/ephemerides.db"

def load_ephemerides():
    """Load ephemerides data from the database into a Pandas DataFrame."""
    conn = sqlite3.connect(DB_NAME)
    
    query = """
    SELECT date, time, ra_hms, dec_dms, distance_au, velocity_km_s, solar_elongation, phase_angle 
    FROM ephemerides
    ORDER BY date, time
    """
    
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    return df

def display_ephemerides():
    """Display ephemerides data in a structured format."""
    df = load_ephemerides()
    
    if df.empty:
        print("No ephemerides data found in the database.")
        return
    
    print("\n📅 Ephemerides Data (First 5 Entries):")
    print(df.head())  # Display first 5 rows
    
    return df

def plot_ephemerides():
    """Plot Mars' distance, velocity, and phase angle over time."""
    df = load_ephemerides()
    
    if df.empty:
        print("No ephemerides data available for plotting.")
        return
    
    df["datetime"] = pd.to_datetime(df["date"] + " " + df["time"])
    
    fig, ax = plt.subplots(3, 1, figsize=(10, 12))
    
    # Plot Distance (AU)
    ax[0].plot(df["datetime"], df["distance_au"], marker="o", linestyle="-", color="blue")
    ax[0].set_title("Mars Distance from Earth (AU)")
    ax[0].set_xlabel("Date")
    ax[0].set_ylabel("Distance (AU)")
    ax[0].grid()

    # Plot Velocity (km/s)
    ax[1].plot(df["datetime"], df["velocity_km_s"], marker="o", linestyle="-", color="red")
    ax[1].set_title("Mars Velocity (km/s)")
    ax[1].set_xlabel("Date")
    ax[1].set_ylabel("Velocity (km/s)")
    ax[1].grid()

    # Plot Phase Angle (degrees)
    ax[2].plot(df["datetime"], df["phase_angle"], marker="o", linestyle="-", color="green")
    ax[2].set_title("Mars Phase Angle")
    ax[2].set_xlabel("Date")
    ax[2].set_ylabel("Phase Angle (degrees)")
    ax[2].grid()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = display_ephemerides()
    
    if not df.empty:
        plot_ephemerides()

