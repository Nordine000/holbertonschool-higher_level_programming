import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print ("Le template doit être une chaîne de caractères.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendees, dict) for attendee in attendees):
        print("Erreur : La liste des invités doit être une liste de dictionnaires.")
        return
    
    if not template.strip():
        print("Template est vide")
        return
    if not attendees:
        print("Aucune donnée, fichier vide")
        return
    
    for index, attendee in enumerate(attendees, start=1):
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")
        event_location = attendee.get("event_location", "N/A")

        personalized_invitation = template.format(
            name=name,
            event_title=event_title,
            event_date=event_date,
            event_location=event_location
        )

        output_filename = f"output_{index}.txt"
    
        if os.path.exists(output_filename):
            print.error(f"File {output_filename} already exists. Skipping file creation.")
            continue

        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(personalized_invitation)
            print(f"Generated invitation: {output_filename}")
        except Exception as e:
            print.error(f"Error writing file {output_filename}: {e}")