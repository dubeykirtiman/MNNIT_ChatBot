import spacy

english_nlp = spacy.load('en_core_web_sm')

text = '''
My name is sarthak kumar
'''

spacy_parser = english_nlp(text)

print(spacy_parser)

for entity in spacy_parser.ents:
    print(f'Found: {entity.text} of type: {entity.label_}')