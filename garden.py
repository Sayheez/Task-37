import spacy
nlp = spacy.load('en_core_web_sm')


sentence1 = u'After Bill drank the water proved to be poisoned.'
sentence2 = u'The girl told the story cried.'
sentence3 = u'The complex houses married and single soldiers and their families.' 
sentence4 = u'While the man hunted the deer ran into the woods.'
sentence5 = u'When John called his old mother was happy.'

gardenpathSentences = [sentence1, sentence2, sentence3, sentence4, sentence5]

#We tokenise our sentences, removing any whitespace or commas///
#methods with an underscore as a suffix return strings, to make them readable for human

nlp_sentence1 = nlp(sentence1)
nlp_sentence2 = nlp(sentence2)
nlp_sentence3 = nlp(sentence3)
nlp_sentence4 = nlp(sentence4)
nlp_sentence5 = nlp(sentence5)
sentences = [nlp_sentence1, nlp_sentence2, nlp_sentence3, nlp_sentence4, nlp_sentence5]

#A function to categorize each entity:
def show_ents(doc):
    if doc.ents:    #if it can find any suitable elements in the string to categorise
        for ent in doc.ents :
            print(ent.text+' - ' +str(ent.start_char) +' - '+ str(ent.end_char) +' - '+ent.label_+ ' - '+str(spacy.explain(ent.label_)))  #returns various pieces of info, formatted, about each one
    else:
        print("No named entities found.")


show_ents(nlp_sentence2)

for i in range(0, len(sentences)) :
    print(f'''
    for sentence {i+1} :''')
    show_ents(sentences[i])


### Commenting on the outputs:

# Spacy can only pick up proper nouns like person, placeincluding fictional.
# therefore it's not actually returning anything for sentences two, three, and four. But in sentences one and five, it picked the noun in the sentence.
# The Spacy literature defines an entity as a real world object with a name: mostly proper nouns.

# because of this, the fact that these are garden-path sentences is not actually relevant, as these focus on mistaking nouns for verbs,
# but we cannot distinguish between nouns/verbs with this

