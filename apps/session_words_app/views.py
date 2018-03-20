# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	return render(request,'session_words_app/index.html')

def result(request):
	print "INITIAL WORDS in session: " +  str(request.session['words'])
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

	print "SESSION is: " + str('words' in request.session)
	word['class'] = css_class
	word['word'] = request.POST['word']		
	if 'words' not in request.session:
		request.session['words'] = []
	
	request.session['words'].append(word)
	request.session.modified = True
	print "First time in session."
	# 	print css_class
	
	return render(request,'session_words_app/index.html')

def clear_session(request):
	request.session['words'] = []
	return render(request,'session_words_app/index.html')

# print "WORDS IS: " + str(request.session['words'])
# request.session['words'] = request.session['words'].append(word)
# print str(request.session['words'])