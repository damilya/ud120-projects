{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "9f51b316",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib\n",
    "import sys\n",
    "import re\n",
    "sys.path.append( \"../tools/\" )\n",
    "from parse_out_email_text import parseOutText"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "48050811",
   "metadata": {},
   "outputs": [],
   "source": [
    "from_sara  = open(\"from_sara.txt\", \"r\")\n",
    "from_chris = open(\"from_chris.txt\", \"r\")\n",
    "\n",
    "from_data = []\n",
    "word_data = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "a90659a0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "emails processed\n",
      "tjonesnsf stephani and sam need nymex calendar\n"
     ]
    }
   ],
   "source": [
    "for name, from_person in [(\"sara\", from_sara), (\"chris\", from_chris)]:\n",
    "    for path in from_person:\n",
    "        path = \"../tools/\" + path[:-1]\n",
    "        email = open(path, \"r\")\n",
    "\n",
    "        ### use parseOutText to extract the text from the opened email\n",
    "        words = parseOutText(email)\n",
    "\n",
    "        list_rep  = [\"sara\", \"shackleton\", \"chris\", \"germani\"]\n",
    "        for e in list_rep:\n",
    "            words = words.replace(e,\"\")\n",
    "            \n",
    "        ### append the text to word_data\n",
    "        word_data.append(words.replace('\\n', ' ').strip())\n",
    "        \n",
    "        ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris\n",
    "        from_data.append(0 if name == \"sara\" else 1)\n",
    "\n",
    "        email.close()\n",
    "\n",
    "print(\"emails processed\")\n",
    "from_sara.close()\n",
    "from_chris.close()\n",
    "\n",
    "joblib.dump( word_data, open(\"your_word_data.pkl\", \"wb\") )\n",
    "joblib.dump( from_data, open(\"your_email_authors.pkl\", \"wb\") )\n",
    "\n",
    "print(word_data[152])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "40d6bfc2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "17578\n"
     ]
    }
   ],
   "source": [
    "print(len(word_data))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "64d9cd51",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "38757\n"
     ]
    }
   ],
   "source": [
    "from nltk.corpus import stopwords\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "\n",
    "sw = stopwords.words(\"english\")\n",
    "vectorizer = TfidfVectorizer(stop_words=\"english\",lowercase=True)\n",
    "vectorizer.fit_transform(word_data)\n",
    "\n",
    "print(len(vectorizer.get_feature_names()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "3d3aee0b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'stephaniethank'"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vectorizer.get_feature_names()[34597]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4558434e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
