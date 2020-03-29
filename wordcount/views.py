from django.http import HttpResponse
from django.shortcuts import render
import operator

def hello(request):
    return  HttpResponse('hello')

def eggs(request):
    return  HttpResponse('I am from eggs function')

def test(request):
    return render(request, 'home.html', {'name':'vivek'})

def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split(' ')
    word_count = len(word_list)
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    ordered_words = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': word_count, 'ordered_words':ordered_words})

def about(request):
    return HttpResponse('Vivek have created this page for counting words')