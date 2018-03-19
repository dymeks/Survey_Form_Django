# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	return render(request,'survey_form_app/index.html')

def	result(request):
	if 'number_submitted' in request.session:
		request.session['number_submitted'] = request.session['number_submitted'] + 1
	else:
		request.session['number_submitted'] = 1	
	
	context = {
		'name':request.POST['name'],
		'dojo_location':request.POST['location'],
		'favorite_language':request.POST['favorite_language'],
		'comment':request.POST['comment']
	}

	return render(request,'survey_form_app/result.html',context)