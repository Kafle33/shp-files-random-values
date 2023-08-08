import geopandas as gpd
import pandas as pd
import numpy as np
from datetime import datetime
date= datetime.today().strftime('%Y-%m-%d_%H-%M-%S')
import random
import string

def replace():

    # Step 1: Read the shapefile
    input_shapefile = 'dummy_building/dummy_building.shp'
    print("file read vayo..")

    gdf = gpd.read_file(input_shapefile)

    # Step 2: Converting the GeoDataFrame to a DataFrame for easy manipulation
    df = gdf.drop(columns='geometry')
    # df = gdf

    informant_type_choices = ["John Snow","John Cena" "The Undertaker", "Tony Stark", "Arya Stark",
    "Michael Scott", "Walter White", "Diva Paige", "Dexter Morgan", "Eleven", "Sherlock Holmes",
    "Lara Croft", "Chandler Bing", "Elliot Alderson", "Katniss Everdeen", "Barney Stinson",
    "Daenerys Targaryen", "Leslie Knope", "Rick Grimes", "Don Draper", "Meredith Grey",
    "John Cena", "Roman Reigns", "Sasha Banks", "Seth Rollins","Annie Drling",
    "Charlotte Flair", "Brock Lesnar", "Drew McIntyre", "Bayley Biyoatch", "AJ Styles",
    "Lady Anuska", "Randy Orton", "Ronda Rousey", "Braun Strowman", "Alexa Bliss",
    # "The Rock", "Kofi Kingston", "Shinsuke Nakamura", "Paige", "Bobby Lashley",
    # "Kevin Owens", "Trish Stratus", "Edge", "Samoa Joe",
    # "Nikki Bella", "Daniel Bryan", "Carmella", "Lita",
    # "Bray Wyatt", "Jeff Hardy", "Nia Jax", "Big E", "Mickie James",
    # "Eddie Guerrero", "Sami Zayn", "Naomi", "Finn Bálor", "Beth Phoenix",
    # "Shane McMahon", "Aleister Black", "Lana", "Sheamus", "Natalya",
    # "CM Punk", "Andrade", "Mandy Rose", "Dolph Ziggler", "Lacey Evans"
]

    road_type_choices = ['black_topped', 'gravel', 'concrete', 'earthen', 'unpaved', 'others']

    ROAD_CATEGORY_CHOICES = ['major', 'minor', 'subsidiary']

    ROAD_CLASS_CHOICES = ['national_highway', 'feeder_road', 'district_road', 'other_urban_road']

    ASSOCIATION_TYPE_CHOICES = ['main', 'associate', 'dissociate']

    ROOF_TYPE_CHOICES = ['rcc', 'tile', 'cgi_sheet', 'straw', 'others']

    STRUCTURE_CHOICES = ['rcc', 'framed', 'load_bearing', 'timber', 'earthen_masonry', 'wood/bamboo', 'compressed_mud', 'mud_block', 'other']

    REGISTRATION_TYPE_CHOICES = ['registered_and_completed', 'registered_and_under_construction', 'not_registered', 'not_aware', 'archived', 'others']

    USE_CAT = ['residential', 'commercial', 'multi_use', 'institutional', 'unused', 'other']

    OWNER_STATUS_CHOICES = ['governmental', 'non_governmental']

    TEMPRORARY_STATUS_CHOICES = ['permanent', 'temporary']

    ROAD_LANE_CHOICES = ['alley', 'single_lane', 'double_lane', 'four_lane']

    building_use_remarks_choices = ["Historic Charm", "Modern Design", "Stunning Views", "Cozy Ambiance", "Spacious Interiors", "Rustic Elegance", "Charming Details", "Luxurious Amenities", "Central Location", "Spectacular Landscape", "Urban Oasis", "Tranquil Retreat", "Open Floorplan", "Elegant Finishes", "Quaint Neighborhood", "Smart Features", "Efficient Layout", "Lively Atmosphere", "Secluded Hideaway", "Vibrant Community"]

    image = ["test image", "photograph name", "image name","picture","test image name"]

    image_url = ["https://www.youtube.com/"]

    USE_CHOICES = ["hospitality","smes","retails","residential", "ce","agriculture", "pharmacy"   "education", "healthcare","financial","religious","unused", "other",]

    owner_names = ["Rohit Gautam", "Nishon Tandukar", "Royal Silwal", "Anish Chand", "Nishit Suwal", "Sanjip Chaudhary", "Sovas Tiwari", "Sabitri Ghimire", "Samir Dangal", "Sijan Dhungana", "Sumit Dangal", "Sumitra Dhungana", "Mahesh-Wor Dhakal", "Aakash KC", "Sumit Basnet", "Sandesh Sharma", "Aadarsha Dhakal", "Anusha Pandey", "Gyapan Neupane", "Krish Shrestha", "Prabin Pathak", "Raj Bhattarai", "Elina Singh Thapa", "Manjita Pandey", "Nirmal A. C.", "Sambrina Raut", "Nischal Shrestha", "Sujan Bhandari", "Biddya Bhandari", "Niraj Adhikari", "Sakun Napit", "Shushila Budhathoki", "Amit Chaudhary", "Anita Pulami Magar", "Susmina Manandar", "Sujit Karki", "Sudeep Puri", "Kailash Shrestha", "Aditya Kushwaha", "Rukmani Acharya", "Manju Limbu", "Pramish Bhandari", "Abhishek Shah", "Uttam Pudasaini", "Arun Bhandari", "Upendra Oli", "Monika Thapa", "Deepak Pradhan", "Rakshya Bhetwal", "Sushil Koirala", "Laxman Pokhrel", "Aayam Ojha", "Tshering Sherpa", "Mridul Gelal", "Roshan Kafle", "Sujan Adhikari", "Sonu Tamang"]

    janakpur_local_roads = ["Taraiya Road", "Dhalkebar Road", "Phulbari Road", "Devdaha Road", "Narayanpur Road", "Sitamadhi Road", "Sarlahi Road", "Lakshmipur Road", "Bhittamod Road", "Dhamaura Road", "Dhanushadham Road", "Jaleshwor Road", "Kamalamai Road", "Sindhuli Road", "Mukhiyapatti Road", "Bhagawatipur Road", "Loharpatti Road", "Bateshwar Road", "Dargah Road", "Prasunabagh Road", "Bijalpur Road", "Bariyarpatti Road", "Bhuteshwor Road", "Kankalini Road", "Mauwahi Road", "Mahinathpur Road", "Siktaur Road", "Mahamanjushri Road", "Nariyani Road", "Patel Road"]

    tole_names = [
    "Taraiya Tole", "Dhalkebar Tole", "Phulbari Tole", "Devdaha Tole", "Narayanpur Tole",
    "Sitamadhi Tole", "Sarlahi Tole", "Lakshmipur Tole", "Bhittamod Tole", "Dhamaura Tole",
    "Dhanushadham Tole", "Jaleshwor Tole", "Kamalamai Tole", "Sindhuli Tole", "Mukhiyapatti Tole",
    "Bhagawatipur Tole", "Loharpatti Tole", "Bateshwar Tole", "Dargah Tole", "Prasunabagh Tole",
    "Bijalpur Tole", "Bariyarpatti Tole", "Bhuteshwor Tole", "Kankalini Tole", "Mauwahi Tole",
    "Mahinathpur Tole", "Siktaur Tole", "Mahamanjushri Tole", "Nariyani Tole", "Patel Tole",
    "Ramnagar Tole", "Sagarnath Tole", "Birgunj Tole", "Dhanukharka Tole", "Lalbandi Tole",
    "Kushaha Tole", "Ekadar Tole", "Krishnanagar Tole", "Kamala Tole", "Janakpurdham Tole",
]


    # Step 3: Replacing attribute data with random values

    field_data_types = {
    'informant': str,
    'ph_no': str,
    'road_id': int,
    'road_name': str,
    'road_wd': float,
    'road_lane': str,
    'count': int,
    'latitude': float,
    'longitude': float,
    'owner_name': str,
    'assoc_type': str,
    'ownr_stat': str,
    'structure': str,
    'roof_type': str,
    'floor': int,
    'reg_type': str,
    'b_use_rmk' : str,
    'image': str,
    'image_URL': str,
    'temp_type':str,
    'b_use_cat':str,
    'b_use_spc':str,
    'img_side':str,
    'side_URL':str,
    'main_b_id':int,
    'road_type': str,
    'build_id':int,
    'tole_name':str,
    }


    # Loop through each field and replace its data with random values
    for field, data_type in field_data_types.items():

        if field == 'road_type':
            df[field] = np.random.choice(road_type_choices, len(df))

        elif field == 'latitude' or field == 'longitude':
            latitudes = []
            longitudes = []
            for index, row in gdf.iterrows():
                centroid = row['geometry'].centroid
                latitudes.append(centroid.y)
                longitudes.append(centroid.x)

            df['latitude'] = latitudes
            df['longitude'] = longitudes

        elif field == 'floor' or field == 'build_id':
            pass

        elif field == 'tole_name':
            df[field] = np.random.choice(tole_names, len(df))

        elif field == 'assoc_type':
            df[field] = np.random.choice(ASSOCIATION_TYPE_CHOICES, len(df))

        elif field == 'road_lane':
            df[field] = np.random.choice(ROAD_LANE_CHOICES, len(df))

        elif field == 'informant':
            df[field] = np.random.choice(informant_type_choices, len(df))

        elif field == 'structure':
            df[field] = np.random.choice(STRUCTURE_CHOICES, len(df))

        elif field == 'roof_type':
            df[field] = np.random.choice(ROOF_TYPE_CHOICES, len(df))

        elif field == 'temp_type':
            df[field] = np.random.choice(TEMPRORARY_STATUS_CHOICES, len(df))

        elif field == 'reg_type':
            df[field] = np.random.choice(REGISTRATION_TYPE_CHOICES, len(df))

        elif field == 'b_use_cat':
            df[field] = np.random.choice(USE_CAT, len(df))

        elif field == 'b_use_rmk':
            df[field] = np.random.choice(building_use_remarks_choices, len(df))

        elif field == 'image':
            df[field] = np.random.choice(image, len(df))

        elif field == 'image_URL':
            df[field] = np.random.choice(image_url, len(df))

        elif field == 'main_b_id':
            df[field] = np.random.randint(1, 61330, len(df))

        elif field == 'ph_no':
            df[field] = np.random.randint(9840000000, 9860000000, len(df))

        elif field == 'road_name':
            df[field] = np.random.choice(janakpur_local_roads, len(df))

        elif field == 'road_wd':
            df[field] = np.random.uniform(2.5, 10.1, len(df))

        elif field == 'count':
            df[field] = np.random.randint(1, 69, len(df))

        elif field == 'owner_name':
            df[field] = np.random.choice(owner_names, len(df))

        elif field == 'ownr_stat':
            df[field] = np.random.choice(OWNER_STATUS_CHOICES, len(df))

        elif field == 'road_id':
            # df[field] = np.random.randint(1, 200, len(df))
            df[field] = np.random.permutation(len(df)) + 1

        elif field == 'b_use_spc':
            df[field] = np.random.choice(USE_CHOICES, len(df))

        elif field == 'road_category':
            df[field] = np.random.choice(ROAD_CATEGORY_CHOICES, len(df))

        elif field == 'road_class':
            df[field] = np.random.choice(ROAD_CLASS_CHOICES, len(df))


        elif data_type == int:
            df[field] = np.random.randint(1, 1000, len(df))
        elif data_type == float:
            df[field] = np.random.uniform(0, 10, len(df))
        elif data_type == str:
            df[field] = [''.join(random.choice(string.ascii_letters) for _ in range(10)) for _ in range(len(df))]
        else:
            df[field] = [str(np.random.randint(1000)) for _ in range(len(df))]


    # Step 4: Combine the modified DataFrame with the original geometry to create a new GeoDataFrame
    gdf_random = gpd.GeoDataFrame(df, geometry=gdf.geometry)
    # print("gdf geometry \n",gdf.geometry)
    # print("df \n",df)
    # print("gdf \n",gdf)


    output_shapefile = f'output/output_{date}'

    # Step 5: Save the new GeoDataFrame as a new shapefile
    gdf_random.to_file(output_shapefile)

    print(f"Shapefile with random attribute data saved: {output_shapefile}")


