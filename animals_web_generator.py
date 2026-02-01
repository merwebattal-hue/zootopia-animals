import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def main():
    data = load_data("animals_data.json")


    with open("animals_template.html", "r", encoding="utf-8") as f:
        template_html = f.read()


    output = ""
    for animal in data:
        name = animal.get("name")

        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet")
        animal_type = characteristics.get("type")

        locations = animal.get("locations", [])
        location_first = locations[0] if locations else None

        output += '<li class="cards__item">\n'

        # Title
        if name:
            output += f'  <div class="card__title">{name}</div>\n'

        # Text block
        output += '  <p class="card__text">\n'
        if diet:
            output += f'      <strong>Diet:</strong> {diet}<br/>\n'
        if location_first:
            output += f'      <strong>Location:</strong> {location_first}<br/>\n'
        if animal_type:
            output += f'      <strong>Type:</strong> {animal_type}<br/>\n'
        output += "  </p>\n"

        output += "</li>\n"


    final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", output)


    with open("animals.html", "w", encoding="utf-8") as f:
        f.write(final_html)

    print("animals.html oluşturuldu")


if __name__ == "__main__":
    main()
