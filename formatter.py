def format_characters(characters):
    return "\n".join([f"  {i + 1}. {character.name} з планети {character.homeworld.name}" for i, character in enumerate(characters)])

def format_vehicles(vehicles):
    return "\n".join([f"  {i + 1}. {vehicle.name}" for i, vehicle in enumerate(vehicles)])

def format_starships(starships):
    return "\n".join([f"  {i + 1}. {starship.name}" for i, starship in enumerate(starships)])

def format_species(species):
    return "\n".join([f"  {i + 1}. {specie.name}" for i, specie in enumerate(species)])
