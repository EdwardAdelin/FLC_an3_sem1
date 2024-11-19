# Lists with data
name = ["Alex", "Emma", "Kate", "Ryan", "Lily"]
age = [21, 25, 36, 31, 27]

# Open a new HTML file in write mode
with open("table.html", "w") as file:
    # Write the basic HTML structure
    file.write("<html>\n")
    file.write("<head><title>Names and Ages</title></head>\n")
    file.write("<body>\n")
    
    # Start the table
    file.write("<table border='1'>\n")
    file.write("  <tr><th>Name</th><th>Age</th></tr>\n")  # Table headers
    
    # Populate the table with data from the lists
    for n, a in zip(name, age):
        file.write(f"  <tr><td>{n}</td><td>{a}</td></tr>\n")
    
    # End the table and HTML
    file.write("</table>\n")
    file.write("</body>\n")
    file.write("</html>\n")

print("HTML file 'table.html' created successfully.")
