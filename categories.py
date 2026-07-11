from config import CATEGORIES



def get_category(movie):


    genres = movie.get(
        "genre_ids",
        []
    )


    for genre in genres:


        if genre in CATEGORIES:

            return CATEGORIES[genre]



    return "films"
