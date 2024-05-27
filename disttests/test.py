#tests

def test1():
    import NameExtractor
    extractor = NameExtractor.NameExtractor("John Robert Smith and Mary Anne Johnson went to the park.")
    extractor.install()
    extracted_names = extractor.extract_names()
    names_with_genders = extractor.determine_genders(extracted_names)
    for name in names_with_genders:
        middlenames_str = ', '.join(name.middlenames) + ', ' if name.middlenames else ''
        print(f"Name: {name.text}, Gender: {name.gender}, Last Name: {name.surname}, Middle Names: {middlenames_str}")

test1()