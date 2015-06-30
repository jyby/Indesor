# -*- coding: utf-8 -*-
#!/usr/bin/python
from __future__ import division 
import ast
import requests
import json,sys
from random import randint
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


# Create your views here.
def error(request):
	return render_to_response('error.html', locals(), context_instance=RequestContext(request))


def about(request):
	return render_to_response('acerca_del_proyecto.html', locals(), context_instance=RequestContext(request))


def how_it_works(request):
	return render_to_response('como_funciona.html', locals(), context_instance=RequestContext(request))


def create_user(request):
	params = {
		'first_name': request.POST['first_name'],
		'username': request.POST['username'],
		'email' : request.POST['email'],
		'password' : request.POST['password'],
		'user_type' : request.POST['user_type']}

	r = requests.post('http://localhost:8000/api/v1.0/users/', data = params)
	
	if r.json()['status'] == 'ok':
		request.session['username'] = request.POST['username']
		request.session['password'] = request.POST['password']
		request.session['credit'] = r.json()['credit']		
		request.session['user_type'] = request.POST['user_type']

		if request.session['user_type'] == '01':
			return HttpResponseRedirect('/configuracion_manual/01')
		else:
			return HttpResponseRedirect('/orden_alfabetico/A')

	else:
		if r.json()['error'] == "Username already exists":
			error = "El nombre de usuario que escogió ya existe. Por favor ingrese otro nombre de usuario."

		return render_to_response('registrar_usuario.html', locals(), context_instance=RequestContext(request),)



def login(request):
	params = {
		'username': request.POST['username'],
		'password' : request.POST['password']}

	r = requests.post('http://localhost:8000/api/v1.0/users/login/', data = params)

	print(r.__dict__)

	if r.json()['status'] == 'ok':
		request.session['username'] = request.POST['username']
		request.session['password'] = request.POST['password']
		request.session['credit'] = r.json()['credit']
		request.session['user_type'] = r.json()['user_type']

		if request.session['user_type'] == '01':
			return HttpResponseRedirect('/configuracion_manual/01')
		else:
			return HttpResponseRedirect('/orden_alfabetico/A')

	else:
		if r.json()['error'] == "Username or password incorrect":
			error = "Nombre de usuario o contraseña incorrecta."

		return render_to_response('iniciar_sesion.html', locals(), context_instance=RequestContext(request),)


def logout(request):
	request.session.flush()
	return HttpResponseRedirect('/acerca_del_proyecto')


def change_password(request):
	return render_to_response('modificar_contraseña.html', locals(), context_instance=RequestContext(request))


def get_words(request, letra):
	if 'username' not in request.session:
		return HttpResponseRedirect('/error/')

	if letra=='0':
		letra='Ñ'
	letra = letra.upper()

	r = requests.get('http://localhost:8000/api/v1.0/get_words/?character=' + letra)

	if r.json()['status'] == 'error':
		list_of_words = []

	else:
		list_of_words = r.json()['data']

	letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','0','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	
	#Search code
	try:
		query = request.GET['buscar']
		r_search = requests.get('http://localhost:8000/api/v1.0/word_search/?buscar=' + query + '&letra=' + letra)
		list_of_words = r_search.json()['data']
	except:
		pass

	#Pagination Code
	paginator = Paginator(list_of_words, 10)

	page = request.GET.get('pagina')
    
	try:
		words = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		words = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		words = paginator.page(paginator.num_pages)

	return render_to_response('diccionario_multimedia.html', locals(), context_instance=RequestContext(request),)


def get_words_manual_config(request, manual_configuration):
	if 'username' not in request.session:
		return HttpResponseRedirect('/error/')
			
	r = requests.get('http://localhost:8000/api/v1.0/get_manual_config/?manual_configuration=' + manual_configuration)

	if r.json()['status'] == 'error':
		list_of_words = []

	else:
		list_of_words = r.json()['data']

	manual_config = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49']
	manual_config_icon = ['b1', 'b2', 'b3', 'b4', 'b5', 'a1', 'a2', 'a3', 'a4', 'a5', 'g1', 'g2', 'g3', 'g4', 'g5', 'c1', 'c2', '51', '52', '53', '54', 'v1', 'v2', 'o1', 'o2', 'o3', 'o4', 'o5', 'f1', 'f2', 'x1', 'h1', 'h2', 'l1', 'y1', 'y2', 'y3', 'y4', 'y5', 'aa1', 'aa2', 'k1', 'i1', 'r1', 'r2', 'w1', '31', '32', 'e1' ]
	manual_config_pair_array = zip(manual_config, manual_config_icon)
	manual_config_pair_dict = dict(manual_config_pair_array)
	icon_code = manual_config_pair_dict[manual_configuration]

	#Search code
	try:
		query = request.GET['buscar']
		r_search = requests.get('http://localhost:8000/api/v1.0/word_search_mc/?buscar=' + query + '&configuracion_manual=' + manual_configuration)
		list_of_words = r_search.json()['data']
	except:
		pass

	#Pagination Code
	paginator = Paginator(list_of_words, 10)

	page = request.GET.get('pagina')
    
	try:
		words = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		words = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		words = paginator.page(paginator.num_pages)

	return render_to_response('diccionario_multimedia_configuracion_manual.html', locals(), context_instance=RequestContext(request),)


def upload_video(request):
	try:
		if request.session['user_type'] == '02':
			return HttpResponseRedirect('/error/')
	except:
		return HttpResponseRedirect('/error/')

	return render_to_response('subir_video.html', locals(), context_instance=RequestContext(request),)


def upload_video_new_word(request):
	try:
		if request.session['user_type'] == '02':
			return HttpResponseRedirect('/error/')
	except:
		return HttpResponseRedirect('/error/')

	if request.method == 'GET':
		return render_to_response('palabra_nueva.html', locals(), context_instance=RequestContext(request),)

	elif request.method == 'POST':

		try:
			word_name = request.POST['word']
			manual_configuration = request.POST['mc_radio']

			for filename, file in request.FILES.iteritems():
				#file es el archivo a enviar
				files = {'file': file}

			params = {
				'word_name': word_name,
				'manual_configuration': manual_configuration,
				'username' : request.session["username"],
				'password' : request.session["password"]
			}

			r = requests.post('http://localhost:8000/api/v1.0/word/upload_file_new_word/', data=params, files=files)
			request.session["credit"] = r.json()['credit']

			status = r.json()['status']

			if status == 'ok':
				result = "El archivo se ha subido correctamente."
			else:
				result = "Usted no tiene suficiente crédito para realizar esta acción."

			return render_to_response('palabra_nueva.html', locals(), context_instance=RequestContext(request),)
		
		except:
			status = "error"
			result = "Complete el formulario para subir un archivo."
			return render_to_response('palabra_nueva.html', locals(), context_instance=RequestContext(request),)


def upload_video_existing_word(request):
	try:
		if request.session['user_type'] == '02':
			return HttpResponseRedirect('/error/')
	except:
		return HttpResponseRedirect('/error/')

	words = requests.get('http://localhost:8000/api/v1.0/get_words_by_status/?status=VA')
	if words.json()['status'] == 'ok':
		list_of_words = words.json()['data']

	if request.method == 'GET':		
		return render_to_response('palabra_existente.html', locals(), context_instance=RequestContext(request),)

	elif request.method == 'POST':
		try:
			word_name = request.POST['word']

			for filename, file in request.FILES.iteritems():
				#file es el archivo a enviar
				files = {'file': file}

			params = {
				'word_name': word_name,
				'username' : request.session["username"],
				'password' : request.session["password"]				
			}

			r = requests.post('http://localhost:8000/api/v1.0/word/upload_file_existing_word/', data=params, files=files)
			request.session["credit"] = r.json()['credit']

			status = r.json()['status']

			if status == 'ok':
				result = "El archivo se ha subido correctamente."
			else:
				result = "Usted no tiene suficiente crédito para realizar esta acción."

			return render_to_response('palabra_existente.html', locals(), context_instance=RequestContext(request),)

		except:
			status = "error"
			result = "Complete el formulario para subir un archivo."
			return render_to_response('palabra_existente.html', locals(), context_instance=RequestContext(request),)


def upload_definition(request):
	try:
		if request.session['user_type'] == '01':
			return HttpResponseRedirect('/error/')
	except:
		return HttpResponseRedirect('/error/')

	words = requests.get('http://localhost:8000/api/v1.0/get_words_by_status/?status=IN')
	if words.json()['status'] == 'ok':
		list_of_words = words.json()['data']

	if request.method == 'GET':
		return render_to_response('subir_definicion.html', locals(), context_instance=RequestContext(request),)

	elif request.method == 'POST':

		try:		
			word_name = request.POST['word']
			word_definition = request.POST['definition']

			params = {
				'word_name': word_name,
				'word_definition': word_definition,
				'username' : request.session["username"],
				'password' : request.session["password"]				
			}

			r = requests.post('http://localhost:8000/api/v1.0/word/upload_definition/', data=params)
			request.session["credit"] = r.json()['credit']

			status = r.json()['status']

			if status == 'ok':
				result = "La definición se ha subido correctamente."

			else:
				result = "Usted no tiene suficiente crédito para realizar esta acción."
			list_of_words =[]
			words = requests.get('http://localhost:8000/api/v1.0/get_words_by_status/?status=IN')
			if words.json()['status'] == 'ok':
				list_of_words = words.json()['data']
			return render_to_response('subir_definicion.html', locals(), context_instance=RequestContext(request),)

		except:
			status = "error"
			result = "Complete el formulario para subir una definición."
			return render_to_response('subir_definicion.html', locals(), context_instance=RequestContext(request),)



def files_to_validate(request):
	try:
		if request.session['user_type'] == '01' or request.session['user_type'] == '02':
			return HttpResponseRedirect('/error/')
	except:
		return HttpResponseRedirect('/error/')

	if request.method == 'GET':

		r = requests.get('http://localhost:8000/api/v1.0/get_words_to_validate/')

		if r.json()['status'] == 'error':
			list_of_words = []

		else:
			list_of_words = r.json()['data']

		return render_to_response('listado_archivos.html', locals(), context_instance=RequestContext(request))


def validate(request):
	try:
		if request.session['user_type'] == '01' or request.session['user_type'] == '02':
			return HttpResponseRedirect('/error/')
	except:
		return HttpResponseRedirect('/error/')

	if request.method == 'GET':

		word = request.GET['palabra']
		r = requests.get('http://localhost:8000/api/v1.0/get_word/?name=' + word)

		word_data = r.json()['data']

		manual_configuration = word_data['manual_configuration']
		manual_config = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49']
		manual_config_icon = ['b1', 'b2', 'b3', 'b4', 'b5', 'a1', 'a2', 'a3', 'a4', 'a5', 'g1', 'g2', 'g3', 'g4', 'g5', 'c1', 'c2', '51', '52', '53', '54', 'v1', 'v2', 'o1', 'o2', 'o3', 'o4', 'o5', 'f1', 'f2', 'x1', 'h1', 'h2', 'l1', 'y1', 'y2', 'y3', 'y4', 'y5', 'aa1', 'aa2', 'k1', 'i1', 'r1', 'r2', 'w1', '31', '32', 'e1' ]
		manual_config_pair_array = zip(manual_config, manual_config_icon)
		manual_config_pair_dict = dict(manual_config_pair_array)
		icon_code = manual_config_pair_dict[manual_configuration]				

		return render_to_response('validar_archivo.html', locals(), context_instance=RequestContext(request))


def validate_word(request):
	try:
		if request.session['user_type'] == '01' or request.session['user_type'] == '02':
			return HttpResponseRedirect('/error/')
	except:
		return HttpResponseRedirect('/error/')

	if request.method == 'GET':
		word = request.GET['palabra']
		answer = request.GET['respuesta']

		if answer == 'Aceptar':
			answer = 'Accept'

		else:
			answer = 'Reject'

		params = {
			'word': word,
			'answer': answer,
			'username' : request.session["username"],
			'password' : request.session["password"]				
		}

		r = requests.post('http://localhost:8000/api/v1.0/word/validate_word/', data=params)

		credit = r.json()['credit']
		request.session['credit'] = credit

		return HttpResponseRedirect('/listado_archivos/')


def challenge(request):
	try:
		if request.session['user_type'] == '01':
			url = '/desafio_video/'
		elif request.session['user_type'] == '02':
			url = '/desafio_definicion'
		else:
			url = '/error/'
	except:
		return HttpResponseRedirect('/error/')
	return render_to_response('desafio.html', locals(), context_instance=RequestContext(request))


def video_challenge(request):
	r = requests.get('http://localhost:8000/api/v1.0/word_challenge_video/')
	challenge = r.json()
	random_number = randint(0,1)
	number = random_number

	return render_to_response('desafio_video.html', locals(), context_instance=RequestContext(request))


def video_challenge_result(request):
	params = {
		'id_word_known': request.POST['id_known'],
		'id_word_unknown': request.POST['id_unknown'],
		'answered_word_known' : request.POST['option_known'],
		'answered_word_unknown' : request.POST['option_unknown'],
		'username' : request.session["username"],
		'password' : request.session["password"],
		}

	r = requests.post('http://localhost:8000/api/v1.0/check_challenge/', data=params)

	if r.json()['status'] == "ok":
		request.session['credit'] = r.json()["new_credit"]
		return render_to_response('ganaste.html', locals(), context_instance=RequestContext(request))
	else:
		return render_to_response('perdiste.html', locals(), context_instance=RequestContext(request))


def definition_challenge(request):
	r = requests.get('http://localhost:8000/api/v1.0/word_challenge_definition/')
	challenge = r.json()
	random_number = randint(0,1)
	number = random_number

	return render_to_response('desafio_definicion.html', locals(), context_instance=RequestContext(request))


def pay_per_word(request):
	params = {
		'word' : request.GET['word'],
		'username' : request.session["username"],
		'password' : request.session["password"],
		}	
	r = requests.post('http://localhost:8000/api/v1.0/pay_per_word/', data=params)
	request.session["credit"] = r.json()['credit']
	return HttpResponse(r, content_type='application/json')