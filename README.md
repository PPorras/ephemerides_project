# 🚀 Mars Ephemerides Data Pipeline

This project fetches **ephemerides data** for **Mars** from NASA's JPL Horizons API, stores it in an SQLite database, and visualizes it using **Pandas and Matplotlib**.

## 📌 Features
- **Fetches ephemerides from NASA's JPL Horizons API** 🌍
- **Stores Mars' physical and ephemerides data in SQLite** 📂
- **Provides SQL queries for retrieving ephemerides data** 🔎
- **Visualizes distance, velocity, and phase angle of Mars** 📈

## 📦 Project Structure

/your_project/ │── /data/ # Stores the SQLite database │── init.py # Marks this as a package │── main.py # Runs the full process │── database.py # Database setup and insertion functions │── fetch_data.py # Fetches data from NASA API │── queries.py # SQL queries for retrieving stored data │── visualization.py # Displays and plots ephemerides data │── README.md # Project documentation


## 🛠️ Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/mars-ephemerides.git
cd ephemerides_project

2️⃣ Install Dependencies

Make sure you have Python installed, then install required packages:

pip install pandas matplotlib requests certifi

🚀 Usage

Simply run the main script:

python main.py

What Happens?

    Initializes the SQLite database 📂
    Fetches Mars' ephemerides data from NASA 🌍
    Stores data in the database 🔢
    Displays stored ephemerides 📅
    Plots distance, velocity, and phase angle graphs 📊

📊 Sample Output

🚀 Initializing database...
📡 Fetching and storing ephemerides data...
🔭 Mars Planet Data:
{name: 'Mars', mean_radius_km: 3389.92, density_g_cm3: 3.933, ...}
📅 Latest Ephemerides Entry:
(date: '2025-06-05', distance_AU: 1.728, velocity_km_s: 14.08, ...)
📈 Generating Plots...
✅ Process completed successfully!

🛠️ Custom Queries

You can run custom queries using queries.py:

from queries import get_ephemerides_by_date

data = get_ephemerides_by_date("2025-06-01", "2025-06-05")
print(data)

📝 License

This project is open-source and available.

🚀 Enjoy tracking Mars' movements with this ephemerides pipeline!


---

## **🔹 What’s Included?**
✅ **Project Overview**  
✅ **Installation Steps**  
✅ **Usage Instructions**  
✅ **Expected Output**  
✅ **Custom Queries**  

