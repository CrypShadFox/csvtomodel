# Blender RenderDoc CSV Import Script

## Description

This Blender Python script imports vertex data from a CSV file exported by RenderDoc and creates a merged mesh in Blender.

## Requirements

- Blender 2.8 or later
- latest version of Renderdoc
- No additional Python modules (uses built-in `csv` and `math` modules)

---
 Ensure you have a CSV file containing vertex data (e.g., exported from RenderDoc).
---

## Usage

1. Open Blender.
2. Switch to the **Scripting** workspace.
3. Click **New** to create a new script, then copy and paste the contents of the `import_renderdoc_csv.py` script below.
4. Modify the `filepath` variable at the top of the script to point to your CSV file:

    ```python
    filepath = "C:/Path/to/YourFile.csv"
    ```

5. (Optional) Adjust `merge_threshold` to control vertex merging sensitivity.
6. Click **Run Script**. The imported mesh will appear in the current scene.
7. You may need to adjust the column names in the csv to make them readable.

## Configuration

- `merge_threshold`: Minimum distance between vertices to consider them the same point (default: `0.01`).

---
