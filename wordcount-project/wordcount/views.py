# from django.http import HttpResponse
import operator

from django.shortcuts import render


def home(request):
    return render(request, "home.html", {"title": "Home"})


def about(request):
    return render(request, 'about.html', {"title": "About"})


def count(request):
    paragraph = request.GET["paragraph"]
    words = paragraph.split()
    word_freq = get_frequency(words)
    wordcount = len(words)
    print(word_freq)
    return render(request, "count.html", {"title": "Count",
                                          "paragraph": paragraph,
                                          "wordcount": wordcount,
                                          "word_freq": word_freq})


def get_frequency(words):
    word_freq = dict()
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    sorted_dict = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_dict
