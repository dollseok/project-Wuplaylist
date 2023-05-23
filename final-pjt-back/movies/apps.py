from django.apps import AppConfig

class MoviesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movies'
    
    # def ready(self):
    #     from .views import get_movie_datas, get_genres_data
    #     get_movie_datas()
    #     get_genres_data()