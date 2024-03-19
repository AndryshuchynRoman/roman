from swapi_client import get_film_info

def main():
    film_id = input("Введіть ідентифікатор фільму: ")
    get_film_info(film_id)

if __name__ == "__main__":
    main()
