import json


def load_data(file_path):
    ''' Function to load data'''
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """
        Serialize an animal object into HTML format for a card. """

    content = ''
    if 'locations' in animal_obj:
        location = animal_obj['locations'][0]
    else:
        location = "undefined"
    content += "<li class=\"cards__item\">"
    content += "<div class=\"card__title\">"
    content += "<p class=\"card__text\">"
    content += f"{animal_obj['name']}</div>"
    content += f"<strong>Diet:</strong> {animal_obj['characteristics']['diet']}<br/>"
    content += f"<strong>Location:</strong> {location}<br/>"

    if 'type' in animal_obj['characteristics']:
        type = animal_obj['characteristics']['type']
    else:
        type = "undefined"
    content += "<strong>Type:</strong> " + type + "<br/>"
    content += "</p>"
    content += "</li>"
    return content

def print_animals_data(data):
    """
       Serialize a list of animal objects into HTML content for printing.
       """
    output = ''
    for animal_obj in data:
        output += serialize_animal(animal_obj)
    return output


def read_html(read_file):
    """
       Read content to the file. """
    with open (read_file, "r") as handle:
        return handle.read()


def replace_animals_info(output, html_temp):
    new_string = html_temp.replace("__REPLACE_ANIMALS_INFO__", output)
    return new_string

def write_html(new_string, new_file):
    """
           Write content to an HTML file. """
    with open (new_file, "w") as handle:
        handle.write(new_string)

def main():
    animals_data = load_data('animals_data.json')
    output = print_animals_data(animals_data)
    html_temp = read_html("animals_template.html")
    new_string = replace_animals_info(output, html_temp)
    write_html(new_string, 'animals.html')



if __name__=="__main__":
    main()



