import csv
import unidecode

# Function to remove or replace unwanted characters
def clean_text(text):
    # Replace unwanted characters with spaces
    text = text.replace("<", " ").replace(">", " ").replace("!", " ").replace("?", " ").replace("-", " ").replace("$", " ").replace(";", " ").replace("Ãƒ", " ").replace("Â©", " ").replace("_", " ").replace("Â«", " ").replace("Â»", " ").replace("*", " ")
    # Use unidecode to handle special characters and accents
    text = unidecode.unidecode(text)
    return text

user_list = []
elon_list = []
current_speaker = None

# Open the input text file in UTF-8 encoding to handle special characters
with open('Elon_musk_data.txt', 'r', encoding='UTF-8', errors='ignore') as file:
    for line in file:
        line = line.strip()
        if line.startswith("User: "):
            current_speaker = "User"
            user_list.append(clean_text(line[len("User: "):]))
        elif line.startswith("Elon Musk: "):
            current_speaker = "Elon Musk"
            elon_list.append(clean_text(line[len("Elon Musk: "):]))
        elif current_speaker:
            # Append text to the appropriate list based on the current speaker
            if current_speaker == "User":
                user_list[-1] += " " + clean_text(line)
            elif current_speaker == "Elon Musk":
                elon_list[-1] += " " + clean_text(line)

# Create a CSV file and write the conversation data
with open('dataset.csv', 'w', newline='', encoding='UTF-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["User", "Elon Musk"])  # Write header row
    writer.writerows(zip(user_list, elon_list))