from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	context={
		'name':'milan',
	}
	return render(request,'home.html', context)


def contact(request):
	return HttpResponse('<h1>This is contact page</h1>')

def count(request):
	data=request.GET.get('fulltext')
	word_list=data.split()
	list_length=len(word_list)

	worddictionary={}

	for word in word_list:
		if word in worddictionary:
			worddictionary[word]+=1
		else:
			worddictionary[word]=1
	word_dictionary=sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
	context={
		'data':data,
		'list_length':list_length,
		'word_dictionary':word_dictionary,
	}
	return render(request, 'count.html',context)