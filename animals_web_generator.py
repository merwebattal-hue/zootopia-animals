import json


def load_data(file_path):
    """Loads a JSON file and returns parsed data."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """Converts a single animal object into semantic HTML."""
    name = animal.get("name")
    taxonomy = animal.get("taxonomy", {})
    characteristics = animal.get("characteristics", {})
    locations = animal.get("locations", [])

    output = '<li class="cards__item">\n'

    if name:
        output += f'  <div class="card__title">{name}</div>\n'

    output += '  <div class="card__text">\n'
    output += '    <ul class="animal__details">\n'

    scientific = taxonomy.get("scientific_name")
    if scientific:
        output += (
            f'      <li><strong>Scientific:</strong> {scientific}</li>\n'
        )

    diet = characteristics.get("diet")
    if diet:
        output += f'      <li><strong>Diet:</strong> {diet}</li>\n'

    if locations:
        output += (
            f'      <li><strong>Location:</strong> '
            f'{", ".join(locations)}</li>\n'
        )

    animal_type = characteristics.get("type")
    if animal_type:
        output += f'      <li><strong>Type:</strong> {animal_type}</li>\n'

    color = characteristics.get("color")
    if color:
        output += f'      <li><strong>Color:</strong> {color}</li>\n'

    output += '    </ul>\n'
    output += '  </div>\n'
    output += '</li>\n'

    return output


def main():
    animals = load_data("animals_data.json")

    with open("animals_template.html", "r", encoding="utf-8") as file:
        template_html = file.read()

    animals_html = ""
    for animal in animals:
        animals_html += serialize_animal(animal)

    final_html = template_html.replace(
        "__REPLACE_ANIMALS_INFO__", animals_html
    )

    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(final_html)

    print("animals.html erfolgreich erstellt.")


if __name__ == "__main__":
    main()
