import csv

def generate_html():
    # Define the colors and output file name
    item_color = "blue"          # Text color for list items
    background_color = "#f0f8ff" # Background color for the entire page (light blue)

    # Read data from Lab7.csv
    with open("Lab7.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        emails = []
        names = []
        
        # Collect emails and names
        for row in reader:
            emails.append(row['Email'])
            names.append(row['FirstName'])
    
    # Generate HTML content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ordered and Unordered Lists</title>
    <style>
        body {{
            background-color: {background_color};
            font-family: Arial, sans-serif;
            color: {item_color};
        }}
        .list-item {{
            color: {item_color};
        }}
    </style>
</head>
<body>
    <h1>Email and First Name Lists</h1>
    
    <!-- Ordered List for Emails -->
    <h2>Ordered List of Emails</h2>
    <ol>
"""
    
    # Add each email as an ordered list item
    for email in emails:
        html_content += f"        <li class='list-item'>{email}</li>\n"
    
    html_content += """    </ol>
    
    <!-- Unordered List for Names -->
    <h2>Unordered List of First Names</h2>
    <ul>
"""
    
    # Add each name as an unordered list item
    for name in names:
        html_content += f"        <li class='list-item'>{name}</li>\n"
    
    # Close the HTML tags
    html_content += """    </ul>
</body>
</html>
"""
    
    # Write the content to an HTML file
    with open("output.html", "w") as file:
        file.write(html_content)

    print("HTML file 'output.html' has been generated successfully.")

# Run the function
generate_html()
