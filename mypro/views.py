from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'myfile.html')
def count(request):
    #return render(request,'count.html')
    fulltext = request.GET['filltext']
    wordlist=fulltext.split()
    return render(request,'count.html',{"fulltext":fulltext,"count":len(wordlist)})
