# Bingo PDF Generator

This repository contains a Python script for generating a Bingo game card in PDF format. The Bingo card is populated with a list of events, and a grid is drawn to create a randomized Bingo game card. The events used in this example are related to countries.

## Prerequisites

Before you run the code, make sure you have the necessary dependencies installed. You can install them using `pip`:

```bash
pip install reportlab
```

## How to Use

Follow these steps to generate your Bingo PDF:

1. Clone this repository or download the script to your local machine.

```bash
git clone https://github.com/your-username/bingo.git
```

2. Open the terminal and navigate to the directory containing the script.

```bash
cd bingo
```

3. Run the script by executing the following command:

```bash
python bingo_generator.py
```

4. The script will generate a PDF file named "eurovision.pdf" in the same directory.

## Customizing Events

You can customize the list of events by modifying the `events` list in the `bingo_generator.py` script. Add or remove events as desired to create your own Bingo card.

```python
events = [
    "UNITED KINGDOM",
    "UKRAINE",
    # Add more events here
]
```

## Important Notes

- The script generates 200 Bingo game cards in a single PDF file. You can adjust the number of cards generated by changing the loop in the script.

- The events are randomly placed on the Bingo cards. If you have a specific set of events you want to use, you may need to modify the script accordingly.

- The PDF file is named "eurovision.pdf" by default. You can change the output filename by modifying the `pdf_file` variable in the script.

Enjoy playing Bingo with your customized cards!
