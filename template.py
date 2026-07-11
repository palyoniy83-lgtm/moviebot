id="template_code"
def movie_template(movie):


    title = movie.get(
        "title",
        "Без назви"
    )


    year = movie.get(
        "release_date",
        ""
    )[:4]


    rating = movie.get(
        "vote_average",
        0
    )


    poster_path = movie.get(
        "poster_path"
    )


    if poster_path:

        poster = (
            "https://image.tmdb.org/t/p/w500"
            +
            poster_path
        )

    else:

        poster = ""



    description = movie.get(
        "overview",
        "Опис відсутній"
    )



    html = f"""

<div class="movie-card">


<center>

<img src="{poster}" 
style="width:300px;border-radius:10px;">

</center>



<h1>

{title} ({year})

</h1>



<hr>



<p>

<b>⭐ Рейтинг:</b>

{rating}/10

</p>



<h2>
Опис фільму
</h2>


<p>

{description}

</p>



<h2>
Дивитися онлайн
</h2>


<div style="
background:#111;
padding:20px;
text-align:center;
color:white;
">


ТУТ БУДЕ ПЛЕЄР


</div>



<h2>
Трейлер
</h2>


<div>


ТУТ БУДЕ YOUTUBE


</div>



</div>

"""


    return html
