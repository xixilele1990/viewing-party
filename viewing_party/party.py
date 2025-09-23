# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:   
        return {
            "title": title,
            "genre": genre,
            "rating": rating
        }
    return None


def add_to_watched(user_data, movie):  #{watched : []}
    
    if "watched" not in user_data:
        user_data["watched"] = []
 
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie): #{watchlist : [{},{},{}]}

    user_data["watchlist"].append(movie)
    return user_data

# {"watchlist": [watched movies]}
def watch_movie(user_data, title):
    
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie) # remove is ok for list since movie existed 
            user_data["watched"].append(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

