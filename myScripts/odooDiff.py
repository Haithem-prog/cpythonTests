import sys

def compare_files(file1_path = r"C:\Users\haith\Desktop\cpython\cpythonTests\myScripts\importMechansims\addonsFolders.txt", file2_path = r"C:\Users\haith\Desktop\cpython\cpythonTests\myScripts\importMechansims\entrpriseFolders.txt", output_path=r"C:\Users\haith\Desktop\cpython\cpythonTests\myScripts\importMechansims\dosesnt exists in entrprise.txt"):#
    # Read all lines from file2 into a set for fast lookup.
    # We remove only the line-ending characters, not spaces/tabs.
    with open(file2_path, "r", encoding="utf-8", errors="replace") as f2:
        file2_lines = {line.rstrip("\n\r") for line in f2}

    # Compare each line from file1 against file2
    with open(file1_path, "r", encoding="utf-8", errors="replace") as f1, \
         open(output_path, "w", encoding="utf-8") as out:

        for line in f1:
            clean_line = line.rstrip("\n\r")

            if clean_line not in file2_lines:
                out.write(clean_line + "\n")

    print(f"Done. Missing lines written to: {output_path}")


if __name__ == "__main__":
    compare_files()

A = set(open(r"C:\Users\haith\Desktop\cpython\cpythonTests\myScripts\importMechansims\addonsFolders.txt",
             encoding="utf-8", errors="replace").read().splitlines())

E = set(open(r"C:\Users\haith\Desktop\cpython\cpythonTests\myScripts\importMechansims\entrpriseFolders.txt",
             encoding="utf-8", errors="replace").read().splitlines())

missing_in_addons = E - A

print("Count:", len(missing_in_addons))

with open(r"C:\Users\haith\Desktop\cpython\cpythonTests\myScripts\importMechansims\exists in enterprise not in addons.txt",
          "w", encoding="utf-8") as f:
    for item in sorted(missing_in_addons):
        f.write(item + "\n")

        # if len(sys.argv) < 3:
    #     print("Usage: python compare_files.py file1.txt file2.txt [output.txt]")
    #     sys.exit(1)

    # file1 = sys.argv[1]
    # file2 = sys.argv[2]
    # output = sys.argv[3] if len(sys.argv) > 3 else "doesntExists.txt"