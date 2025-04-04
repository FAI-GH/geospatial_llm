import geopandas as gpd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()

# Read GeoJSON file
gdf = gpd.read_file("data/sample.geojson")  # Adjust path if needed

# Ensure it's using EPSG:4326 (WGS84) for compatibility
gdf = gdf.to_crs(epsg=4326)

# Create SQLAlchemy connection string
conn_str = (
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

# Create engine
engine = create_engine(conn_str)

# Upload to PostGIS (this creates a table called 'geojson_data')
gdf.to_postgis("geojson_data", engine, if_exists="replace", index=False)

print("✅ GeoJSON uploaded to PostGIS successfully!")
