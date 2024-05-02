import json


def load_data(file_path):
    ''' Function to load data'''
    with open(file_path, "r") as handle:
        return json.load(handle)

def print_animals_data(animals_data):
    content = ''
    for animal in animals_data:
        if 'locations' in animal:
            location = animal['locations'][0]
        else:
            location = "undefined"
        content += "<li class=\"cards__item\">"
        content += "<div class=\"card__title\">"
        content += "<p class=\"card__text\">"
        content += f"Name: {animal['name']}<br/>"
        content += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>"
        content += f"<strong>Location:</strong> {location}<br/>"

        if 'type' in animal['characteristics']:
            type = animal['characteristics']['type']
        else:
            type = "undefined"
        content += "<strong>Type:</strong> " + type + "<br/>"
        content += "</p>"
        content += "</li>"
    return content



def read_html(read_file):
    with open (read_file, "r") as handle:
        return handle.read()


def replace_animals_info(output, html_temp):
    new_string = html_temp.replace("__REPLACE_ANIMALS_INFO__", output)
    return new_string

def write_html(new_string, new_file):
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



