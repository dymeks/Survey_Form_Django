# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from time import gmtime, strftime,localtime
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	return render(request,'session_words_app/index.html')

def result(request):
	date = strftime("%Y-%m-%d %H:%M %p", localtime())
	css_class = ''
	word = {}
	if 'large_font' in request.POST:
		css_class = css_class + 'big '
	if request.POST['color'] == 'red':
		css_class = css_class + 'red'
	elif request.POST['color'] == 'blue':	
		css_class = css_class + 'blue'
	else:
		css_class = css_class + 'green'

	
	word['class'] = css_class
	word['word'] = request.POST['word']
	word['date'] = date
	print str('words' in request.session)
	if 'words' not in request.session:
		request.session['words'] = []
		print "SESSION is: " + str('words' in request.session)
	
	request.session['words'].append(word)
	request.session.modified = True
	
	return render(request,'session_words_app/index.html')

def clear_session(request):
	# request.session.flush()
	request.session.clear()
	return render(request,'session_words_app/index.html')