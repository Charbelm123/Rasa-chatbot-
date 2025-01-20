

import psycopg2
from typing import List, Optional

def restaurant_db():
    """Expanded database of restaurants with details."""
    
    return [
        # Caribbean
        {"restaurant_name": "Island Breeze", "cuisine": "caribbean", "remaining_places": "5", "outdoor_seating": "yes", "view": "beach"},
        {"restaurant_name": "Tropical Flavors", "cuisine": "caribbean", "remaining_places": "7", "outdoor_seating": "yes", "view": "garden"},
        {"restaurant_name": "Palm Paradise", "cuisine": "caribbean", "remaining_places": "4", "outdoor_seating": "no", "view": "ocean"},
        
        # Chinese
        {"restaurant_name": "Golden Dragon", "cuisine": "chinese", "remaining_places": "8", "outdoor_seating": "no", "view": "city"},
        {"restaurant_name": "Panda Garden", "cuisine": "chinese", "remaining_places": "6", "outdoor_seating": "yes", "view": "park"},
        {"restaurant_name": "Wok Wonders", "cuisine": "chinese", "remaining_places": "5", "outdoor_seating": "no", "view": "street"},
        
        # French
        {"restaurant_name": "Le Gourmet", "cuisine": "french", "remaining_places": "3", "outdoor_seating": "yes", "view": "river"},
        {"restaurant_name": "Maison Blanche", "cuisine": "french", "remaining_places": "4", "outdoor_seating": "no", "view": "city"},
        {"restaurant_name": "Parisian Table", "cuisine": "french", "remaining_places": "6", "outdoor_seating": "yes", "view": "garden"},
        
        # Greek
        {"restaurant_name": "Olympus Tavern", "cuisine": "greek", "remaining_places": "7", "outdoor_seating": "yes", "view": "mountains"},
        {"restaurant_name": "Santorini Grill", "cuisine": "greek", "remaining_places": "5", "outdoor_seating": "yes", "view": "ocean"},
        {"restaurant_name": "Hellenic Haven", "cuisine": "greek", "remaining_places": "3", "outdoor_seating": "no", "view": "city"},
        
        # Indian
        {"restaurant_name": "Spice Symphony", "cuisine": "indian", "remaining_places": "10", "outdoor_seating": "no", "view": "city"},
        {"restaurant_name": "Taj Tandoor", "cuisine": "indian", "remaining_places": "8", "outdoor_seating": "yes", "view": "street"},
        {"restaurant_name": "Curry Palace", "cuisine": "indian", "remaining_places": "6", "outdoor_seating": "no", "view": "river"},
        
        # Italian
        {"restaurant_name": "Trattoria Bella", "cuisine": "italian", "remaining_places": "2", "outdoor_seating": "yes", "view": "garden"},
        {"restaurant_name": "Pasta Perfection", "cuisine": "italian", "remaining_places": "5", "outdoor_seating": "yes", "view": "city"},
        {"restaurant_name": "La Dolce Vita", "cuisine": "italian", "remaining_places": "4", "outdoor_seating": "no", "view": "river"},
        
        # Mexican
        {"restaurant_name": "Casa Mexicana", "cuisine": "mexican", "remaining_places": "6", "outdoor_seating": "yes", "view": "street"},
        {"restaurant_name": "El Sombrero", "cuisine": "mexican", "remaining_places": "4", "outdoor_seating": "yes", "view": "garden"},
        {"restaurant_name": "Baja Grill", "cuisine": "mexican", "remaining_places": "8", "outdoor_seating": "no", "view": "beach"},
        
        # Lebanese
        {"restaurant_name": "Beirut Bites", "cuisine": "lebanese", "remaining_places": "4", "outdoor_seating": "yes", "view": "ocean"},
        {"restaurant_name": "Cedar Grove", "cuisine": "lebanese", "remaining_places": "7", "outdoor_seating": "no", "view": "city"},
        {"restaurant_name": "Lebanese Lounge", "cuisine": "lebanese", "remaining_places": "6", "outdoor_seating": "yes", "view": "garden"},
        
        # Thai
        {"restaurant_name": "Bangkok Delight", "cuisine": "thai", "remaining_places": "9", "outdoor_seating": "no", "view": "city"},
        {"restaurant_name": "Thai Fusion", "cuisine": "thai", "remaining_places": "5", "outdoor_seating": "yes", "view": "street"},
        {"restaurant_name": "Lotus Thai", "cuisine": "thai", "remaining_places": "3", "outdoor_seating": "yes", "view": "garden"},
        
        # Vietnamese
        {"restaurant_name": "Saigon Flavors", "cuisine": "vietnamese", "remaining_places": "5", "outdoor_seating": "yes", "view": "lake"},
        {"restaurant_name": "Pho Paradise", "cuisine": "vietnamese", "remaining_places": "6", "outdoor_seating": "no", "view": "city"},
        {"restaurant_name": "Hanoi Haven", "cuisine": "vietnamese", "remaining_places": "4", "outdoor_seating": "yes", "view": "river"},
    ]




def insert_restaurants_to_db(data):
    """Insert restaurant data into PostgreSQL."""
    connection = psycopg2.connect(
            dbname="restaurant_db",
            user="postgres",
            password="mysecretpassword",
            host="localhost",
            port="5435"
        )
    try:
        
        cursor = connection.cursor()

        for restaurant in data:
            query = """
            INSERT INTO restaurants (restaurant_name, cuisine, remaining_places, outdoor_seating, view)
            VALUES (%s, %s, %s, %s, %s);
            """
            values = (
                restaurant["restaurant_name"],
                restaurant["cuisine"],
                int(restaurant["remaining_places"]),
                True if restaurant["outdoor_seating"].lower() == "yes" else False,
                restaurant["view"]
            )

            cursor.execute(query, values)

        connection.commit()
        print("Data inserted successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

# Insert the data
data = restaurant_db()
insert_restaurants_to_db(data)




def get_restaurants_by_criteria(
    cuisine: str,
    outdoor_seating: str,
    min_places: int,
    view: Optional[str] = None,
) -> List[dict]:
    try:
        # Connect to PostgreSQL database
        connection = psycopg2.connect(
            dbname="restaurant_db",
            user="postgres",
            password="mysecretpassword",
            host="localhost",
            port="5435"
        )
        cursor = connection.cursor()

        # Base query
        query = """
        SELECT restaurant_name, cuisine, remaining_places, outdoor_seating, view
        FROM restaurants
        WHERE cuisine = %s
        AND outdoor_seating = %s
        AND remaining_places >= %s
        """
        params = [cuisine, outdoor_seating== "yes", min_places]

        # Add optional view filter
        if view:
            query += " AND view = %s"
            params.append(view)

        # Execute query
        cursor.execute(query, params)
        rows = cursor.fetchall()

        # Parse results into a list of dictionaries
        restaurants = [
            {
                "restaurant_name": row[0],
                "cuisine": row[1],
                "remaining_places": row[2],
                "outdoor_seating": "yes" if row[3] else "no",
                "view": row[4],
            }
            for row in rows
        ]
        return restaurants

    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        if connection:
            cursor.close()
            connection.close()
