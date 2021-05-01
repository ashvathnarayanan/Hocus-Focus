import nltk
from nltk.tokenize import RegexpTokenizer
import speech_recognition as SpeechRecog
import pyaudio
from random_word import RandomWords
import random
import time
import threading

def word_filter(string):
    tokenizer = RegexpTokenizer(r'\w+')
    string_list_with_char = tokenizer.tokenize(string)
    string_list = [w for w in string_list_with_char if len(w) > 1]
    def is_noun(pos): return pos[:2] == 'NN'
    nouns = [word for (word, pos) in nltk.pos_tag(string_list) if is_noun(pos)]
    string_filtered = []
    for i in nouns:
        if (nouns.count(i) > 1 and (i not in string_filtered) or nouns.count(i) == 1):
            string_filtered.append(i)
    return string_filtered

def quiz(string):
    options = RandomWords().get_random_words()[:3]
    minimize = [words for words in string if len(words) > 5]
    options.append(random.choice(minimize))
    random.shuffle(options)
    return options

def main():
    init_rec = SpeechRecog.Recognizer()
    words = []
    print("start")
    for i in range(1):
        with SpeechRecog.Microphone() as source:
            audio_data = init_rec.record(source, duration=10)
            try:text = init_rec.recognize_google(audio_data)
            except:text = ''
            text_filtered = word_filter(text)
        for j in text_filtered:
            words.append(j)
    return quiz(words)
