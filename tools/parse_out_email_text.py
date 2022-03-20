from nltk.stem.snowball import SnowballStemmer
import string
# import re

def parseOutText(f):
    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
        ### remove punctuation
        text_string = content[1].translate(str.maketrans('', '', string.punctuation))

        # text_string = re.sub(r'[^\w\s]', '', content[1])

        ### project part 2: comment out the line below
        stemmer = SnowballStemmer("english")
        words = ' '.join([stemmer.stem(word) for word in text_string.split()])

    return words

# def main():
#     ff = open("../text_learning/test_email.txt", "r")
#     text = parseOutText(ff)
#     print(text)

# if __name__ == '__main__':
#     main()