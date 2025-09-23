# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    return {
        "title":title,
        "genre":genre,
        "rating":rating
    }
    

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return  user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            break
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

    most_watched_genre = max(genre_counts, key=genre_counts.get)
    return most_watched_genre
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

