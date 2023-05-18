from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas
import random

events = [
    # Add events here that will appear in each square
    "UNITED KINGDOM",
    "UKRAINE",
]


def draw_grid(canvas, used_events):
    canvas.setStrokeColorRGB(0, 0, 0)  # Set grid color to black
    canvas.setLineWidth(0.5)  # Set grid line width
    width, height = landscape(A4)  # Get landscape page size

    # Calculate cell size
    cell_width = width / 5
    cell_height = height / 5

    # Iterate over each cell
    for i in range(5):
        for j in range(5):
            x = i * cell_width
            y = j * cell_height

            # Check if all events have been used
            if not events:
                # Reset the events list
                events.extend(used_events)
                used_events = []

            # Get a random event that hasn't been used on this page
            event = random.choice(events)

            # Remove the event from the list
            events.remove(event)

            # Add the event to the used_events list
            used_events.append(event)

            # Set font properties
            canvas.setFont("Helvetica-Bold", 8)
            canvas.setFillColorRGB(0, 0, 0)

            # Draw the event in the middle of the cell
            canvas.drawCentredString(
                x + cell_width / 2, y + cell_height / 2, event)

            # Draw horizontal line
            canvas.line(x, y, x + cell_width, y)

            # Draw vertical line
            canvas.line(x, y, x, y + cell_height)

    # Draw the remaining lines
    for i in range(6):
        y = i * cell_height
        canvas.line(0, y, width, y)

    for i in range(6):
        x = i * cell_width
        canvas.line(x, 0, x, height)

    return used_events


# Create a new PDF document
pdf_file = "eurovision.pdf"
canvas = canvas.Canvas(pdf_file, pagesize=landscape(A4))

# List to keep track of used events
used_events = []

# Draw grids
for _ in range(200):
    # Draw the grid and update the used_events list
    used_events = draw_grid(canvas, used_events)

    # Save the page
    canvas.showPage()

# Save and close the document
canvas.save()
