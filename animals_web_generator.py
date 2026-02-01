import json


def load_data(file_path):
    """Loads a JSON file and returns parsed data."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """
    Converts a single animal object into an HTML card.
    Bonus fields included: Scientific name, Color, all Locations.
    """
    name = animal.get("name")
    taxonomy = animal.get("taxonomy", {})
    characteristics = animal.get("characteristics", {})
    locations = animal.get("locations", [])

    output = '<li class="cards__item">\n'

    # Title
    if name:
        output += f'  <div class="card__title">{name}</div>\n'

    output += '  <p class="card__text">\n'

    # Scientific name (BONUS)
    scientific = taxonomy.get("scientific_name")
    if scientific:
        output += f'    <strong>Scientific:</strong> {scientific}<br/>\n'

    # Diet
    diet = characteristics.get("diet")
    if diet:
        output += f'    <strong>Diet:</strong> {diet}<br/>\n'

    # All locations (BONUS)
    if locations:
        output += (
            f'    <strong>Location:</strong> '
            f'{", ".join(locations)}<br/>\n'
        )

    # Type
    animal_type = characteristics.get("type")
    if animal_type:
        output += f'    <strong>Type:</strong> {animal_type}<br/>\n'

    # Color (BONUS)
    color = characteristics.get("color")
    if color:
        output += f'    <strong>Color:</strong> {color}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'

    return output


def main():
    animals = load_data("animals_data.json")

    # Read HTML template
    with open("animals_template.html", "r", encoding="utf-8") as file:
        template_html = file.read()

    # Generate HTML for all animals
    animals_html = ""
    for animal in animals:
        animals_html += serialize_animal(animal)

    # Replace placeholder in template
    final_html = template_html.replace(
        "__REPLACE_ANIMALS_INFO__", animals_html
    )

    # Write final HTML file
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(final_html)

    print("animals.html erfolgreich erstellt.")


if __name__ == "__main__":
    main()
