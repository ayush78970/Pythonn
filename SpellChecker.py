# import the SpellChecker library
from spellchecker import SpellChecker

# creating the app class
class SpellCheckerApp:
    def __init__(self):  # constructor function automatically executes when we create a class object
        self.spell = SpellChecker()  # create an object of SpellChecker to check each word

    def correct_text(self, text):  # check if words are correct or not
        words = text.split()  # break text into words
        corrected_words = []  # list to store corrected words

        for word in words:
            corrected_word = self.spell.correction(word)  # get corrected word using ->>correction func
            if corrected_word != word.lower():  # ->>lower func
                print(f'correcting "{word}" to "{corrected_word}"')
            corrected_words.append(corrected_word)  # append corrected word to the list

        # step 4: returning the corrected text
        return ' '.join(corrected_words)  # used join function (corrected indentation)

    # running app step 5
    def run(self):
        print("\n___Spell Checker____")
        while True:
            text = input('Enter text to check (or type "exit" to quit): ')  # Corrected "exist" to "exit"
            if text.lower() == 'exit':
                print('Closing the program....')
                break
            
            corrected_text = self.correct_text(text)
            print(f'Corrected Text: {corrected_text}')

# running the main program
if __name__ == "__main__":  # if file is directly run, the app runs
    app = SpellCheckerApp()  # Corrected: create SpellCheckerApp object
    app.run()  # run the app
