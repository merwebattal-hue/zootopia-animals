import json


def load_data(file_path):
    """Loads a JSON file and returns parsed data."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """Converts a single animal object into HTML."""
    output = '<li class="cards__item">\n'

    # Name
    if "name" in animal:
        output += f'  <div class="card__title">{animal["name"]}</div>\n'

    output += '  <p class="card__text">\n'

    # Diet
    characteristics = animal.get("characteristics", {})
    if "diet" in characteristics:
        output += f'    <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'

    # Location (first item)
    if "locations" in animal and animal["locations"]:
        output += f'    <strong>Location:</strong> {animal["locations"][0]}<br/>\n'

    # Type
    if "type" in characteristics:
        output += f'    <strong>Type:</strong> {characteristics["type"]}<br/>\n'

    output += "  </p>\n"
    output += "</li>\n"

    return output


def main():
    animals = load_data("animals_data.json")

    # Read HTML template
    with open("animals_template.html", "r", encoding="utf-8") as file:
        template_html = file.read()

    # Generate animal cards
    animals_html = ""
    for animal in animals:
        animals_html += serialize_animal(animal)

    # Replace placeholder
    final_html = template_html.replace(
        "__REPLACE_ANIMALS_INFO__", animals_html
    )

    # Write output HTML
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(final_html)

    print("animals.html erfolgreich erstellt.")


if __name__ == "__main__":
    main()
