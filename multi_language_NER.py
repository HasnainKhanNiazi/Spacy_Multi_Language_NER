import spacy

class NER_Extraction:
    def extract_NER(self, text, language):
        print(f"Text is: {text}")
        dict = {}
        
        if language == "en":
            nlp = spacy.load(language + '_core_web_sm')
        else: 
            nlp = spacy.load(language + '_core_web_sm')
            
        doc = nlp(text)
        for entity in doc.ents:
            dict[entity.text] = {entity.start_char, entity.end_char, entity.label_}

        return dict
if __name__=="__main__":
    NER = NER_Extraction()
    print(NER.extract_NER("I am Hasnain", "en"))