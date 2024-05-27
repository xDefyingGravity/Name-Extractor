import sys
sys.path.insert(0, './src')
from names import NameExtractor as n
import cProfile

# Example usage:
def main():
    extractor = n("John Robert Smith and Mary Anne Johnson went to the park.")
    extractor.install()
    extracted_names = extractor.extract_names()
    names_with_genders = extractor.determine_genders(extracted_names)
    for name in names_with_genders:
        middlenames_str = ', '.join(name.middlenames) + ', ' if name.middlenames else ''
        print(f"Name: {name.text}, Gender: {name.gender}, Last Name: {name.surname}, Middle Names: {middlenames_str}")


mode = "test"
if __name__ == "__main__":
    if mode == "test":
        main()
    elif mode == "profile":
        cProfile.run("main()", sort='tottime')
    else:
        raise Exception("Invalid mode")