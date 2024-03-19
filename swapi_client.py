import swapi_client
from formatter import format_characters, format_vehicles, format_starships, format_species


def get_film_info(film_id):
    film = swapi_client.get_film(film_id)
    print(f"Фільм: {film.title}")

    characters = [character for character in film.get_characters().iter()]
    vehicles = [vehicle for vehicle in film.get_vehicles().iter()]
    starships = [starship for starship in film.get_starships().iter()]
    species = [specie for specie in film.get_species().iter()]

    print("Персонажі:")
    print(format_characters(characters))

    print("Транспортні засоби:")
    print(format_vehicles(vehicles))

    print("Космічні кораблі:")
    print(format_starships(starships))

    print("Види істот:")
    print(format_species(species))
