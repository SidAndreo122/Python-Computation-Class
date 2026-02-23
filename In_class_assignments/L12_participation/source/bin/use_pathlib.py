from pathlib import Path
data_folder = Path("../data/text.d/")
file_to_open = data_folder / "some_text.txt"
print(file_to_open.read_text())
