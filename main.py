from database import create_db, insert_planet
from fetch_data import fetch_and_store_ephemerides
from queries import get_planet_data, get_latest_ephemerides, get_all_ephemerides, get_ephemerides_by_date
#from visualization import display_ephemerides, plot_ephemerides



def main():
    """Main function to initialize database and fetch data."""
    print("Initializing database...")
    create_db()
    insert_planet()
    
    print("Fetching and storing ephemerides data...")
    fetch_and_store_ephemerides()

    print("Process completed successfully.")

    print("🔭 Mars Planet Data:")
    print(get_planet_data())

    ##print("\n📅 All Ephemerides:")
    ##print(get_all_ephemerides())

    print("\n📅 Get Ephemeride from '2025-Jun-02'up to '2025-Jun-03':")
    print(get_ephemerides_by_date('2025-Jun-02','2025-Jun-03'))

    #print("\n📊 Displaying Ephemerides Data...")
    #df = display_ephemerides()

    #if not df.empty:
    #    print("\n📈 Generating Plots...")
    #    plot_ephemerides()

    ##print("\n📅 Latest Ephemerides Entry:")
    ##print(get_latest_ephemerides())

if __name__ == "__main__":
    main()

