from bs4 import BeautifulSoup
import json

# Read the HTML content from the local file
with open("dst_commands.html", "r", encoding="utf-8") as html_file:
    html_content = html_file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

commands_data = []

li_elements = soup.find_all("li")

for li in li_elements:
    b_tag = li.find("b")
    pre_tag = li.find_next("pre")
    i_tag = li.find_next("i")

    if b_tag and pre_tag and i_tag:
        command_name = b_tag.text.strip()
        command = pre_tag.text.strip()
        command_description = i_tag.text.strip()

        commands_data.append(
            {
                "CommandName": command_name,
                "Command": command,
                "CommandDescription": command_description,
            }
        )
        print(f"Added command: {command_name}")

# Save the data to a JSON file
with open("dst_commands.json", "w") as json_file:
    json.dump(commands_data, json_file, indent=4)

print("Data has been scraped and saved to 'dst_commands.json'")
