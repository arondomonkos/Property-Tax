# Property Tax

This program processes and analyzes plot data for a fictional lakeside municipality's property tax system. Based on the distance of each plot from the lake and its associated zone (A, B, or C), the program determines various statistics, identifies multi-zone streets, and calculates individual and total taxes.

## Functionality

### Function 1
- Reads the contents of the `street.txt` file.
- Stores each line's plot information for further processing.

### Function 2
- Counts how many plot entries are present in the file.

### Function 3
- Prompts for an owner ID and displays which plots (with street and house number) are owned by that person.
- If the ID does not exist, displays: `Not found in the dataset.`

### Function 4
- Defines a function `tax(zone, area)` that computes the payable property tax:
  - A-zone: 800 Ft/m²
  - B-zone: 600 Ft/m²
  - C-zone: 100 Ft/m²
  - Tax is waived if the amount is less than 10,000 Ft.

### Function 5
- Calculates how many plots fall into each zone (A, B, C) and sums their respective tax totals.

### Function 6
- Lists street names that contain plots from more than one zone.

### Function 7
- Computes total tax per owner.
- Writes the results into `tax.txt`, with each line containing the owner ID and their total tax amount.

## Input

- `street.txt`: 
  - The first line contains three space-separated tax rates (A B C).
  - Each subsequent line contains five fields: owner ID, street name, house number, zone, and area (m²).

## Output

- Console messages for:
  - Plot count
  - Plot ownership by ID
  - Tax totals per zone
  - Multi-zone streets
- Output file: `tax.txt` containing one line per owner with their total tax liability.

## Output files

After running the program, it generates one output file: `tax.txt`.
This file is not included in the repository. It is automatically created during execution.

---
Developed by Áron Domonkos, 2024.