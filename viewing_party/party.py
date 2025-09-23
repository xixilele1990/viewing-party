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
def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0.0
    
    total_score = 0
    movie_num = 0
    for movie in user_data["watched"]:
        total_score += movie["rating"]
        movie_num += 1
    return total_score / movie_num

def get_most_watched_genre(user_data):
    watched = user_data["watched"]

    if not watched:
        return None
    
    genre_counts = {}
    for movie in watched:
        genre = movie.get("genre")
        if genre not in genre_counts:
            genre_counts[genre] = 1
        else:
            genre_counts[genre] += 1

    # most_watched_genre = max(genre_counts, key=genre_counts.get)

    max_count = 0
    
    for genre, count in  genre_counts.items():

        if count > max_count:

            max_count = count
            max_watched_genre = genre


    return max_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    
    user_watched = user_data["watched"]
    subscriptions = user_data["subscriptions"]
    
    friend_watched =[]
    
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friend_watched:
                friend_watched.append(movie)
                
    recs = []
    for movie in friend_watched:
       
        if movie in user_watched:
            continue

       
        if movie["host"] not in subscriptions:
            continue

       
        recs.append(movie)
    return recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)

    if most_watched_genre is None:
        return []
    
    friends_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_watched:
                friends_watched.append(movie)

    
    recs = []
    for movie in friends_watched:
        if movie in user_data["watched"]:
            continue 
        if movie["genre"] != most_watched_genre:
            continue  
        recs.append(movie)

    return recs


def get_rec_from_favorites(user_data):

    favorites = user_data.get("favorites", [])

 
    friends_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_watched:
                friends_watched.append(movie)

  
    recs = []
    for movie in favorites:
        if movie not in friends_watched:
            recs.append(movie)

    return recs

