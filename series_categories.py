from config import SERIES_CATEGORIES



def get_series_category(series):


    genres = series.get(
        "genre_ids",
        []
    )


    for genre in genres:


        if genre in SERIES_CATEGORIES:

            return SERIES_CATEGORIES[genre]



    return "serialy"
