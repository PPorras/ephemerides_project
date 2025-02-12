from fastapi import FastAPI, HTTPException
from queries import get_planet_data, get_all_ephemerides, get_latest_ephemerides#, get_ephemerides_by_date
#from fetch_data import fetch_and_store_ephemerides

app = FastAPI()

@app.get("/")
async def root():
    """Root endpoint returning a simple greeting."""
    return {"message": "Hello World"}

@app.get("/planet")
async def planet():
    """
    Retrieve Mars physical data.
    """
    data = get_planet_data()
    if data:
        return data
    raise HTTPException(status_code=404, detail="Planet data not found")

@app.get("/ephemerides")
async def ephemerides():
    """
    Retrieve all ephemerides data.
    """
    data = get_all_ephemerides()
    return data

@app.get("/ephemerides/latest")
async def latest_ephemerides():
    """
    Retrieve the most recent ephemerides entry.
    """
    data = get_latest_ephemerides()
    if data:
        return data
    raise HTTPException(status_code=404, detail="No ephemerides data found")

@app.get("/ephemerides/date")
async def ephemerides_by_date(start_date: str, end_date: str):
    """
    Retrieve ephemerides data between the specified start and end dates.
    - **start_date**: start date in 'YYYY-MM-DD' format.
    - **end_date**: end date in 'YYYY-MM-DD' format.
    """
    data = get_ephemerides_by_date(start_date, end_date)
    return data

##@app.post("/update")
##async def update_ephemerides():
##    """
##    Trigger an update of the ephemerides data by fetching new data
##    from the JPL Horizons API and storing it in the database.
##    """
##    try:
##        fetch_and_store_ephemerides()
##        return {"message": "Ephemerides updated successfully"}
##    except Exception as e:
##        raise HTTPException(status_code=500, detail=str(e))
##
