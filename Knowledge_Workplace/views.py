from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from pathlib import Path
import os
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt


def index(request):
	return HttpResponse("Welcome to Knowledge Workplace")

# To load the respective repository
def load_repo(request,repo_name):
	return HttpResponse("This is %s. " % repo_name)

#To get the documents form repo
def get_docs(request,repo_name):
	docs = []
	doc_path = "./repos/"+repo_name+"/docs"
	print(doc_path)
	if os.path.isdir(doc_path):
		for doc in os.listdir(doc_path):
			docs.append(doc)
		return HttpResponse(docs)
	else:
		return HttpResponse("No documents found")

#To get the entities form repo
def get_entities(request,repo_name):
	docs = []
	doc_path = repo_name+"/entities"
	if os.path.isdir(doc_path):
		for doc in os.listdir(doc_path):
			docs.append(doc)
		return HttpResponse(docs)
	else:
		return HttpResponse("No entities found")

#To get the dictionaries form repo
def get_dictionaries(request,repo_name):
	docs = []
	doc_path = repo_name+"/doc"
	if os.path.isdir(doc_path):
		for doc in os.listdir(doc_path):
			docs.append(doc)
		return HttpResponse(docs)
	else:
		return HttpResponse("No dictionaries found")

def get_relationTypes(request,repo_name):
	docs = []
	doc_path = repo_name+"/relation_types"
	if os.path.isdir(doc_path):
		for doc in os.listdir(doc_path):
			docs.append(doc)
		return HttpResponse(docs)
	else:
		return HttpResponse("No relation types found")

# To Upload Documents/Document Sets
@csrf_exempt
def upload_doc(request,repo_name):
	if request.method == 'POST':
		path = "./repos/"+repo_name+"/docs/"+request.FILES['file'].name
		upload_file(request.FILES['file'],path)
		return HttpResponse("Document has been uploaded successfully")
	else:
		return HttpResponse("Unable to upload Document")

# To Upload Entities
def upload_entities(request,repo_name):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			path = "./repos/"+repo_name+"/entities/"+request.FILES['file'].name
			upload_file(request.FILES['file'],path)
			return HttpResponse("Document has been uploaded successfully")
	else:
		form = UploadFileForm()
		return HttpResponse("Unable to upload Document")

# To Upload Relation_types
def upload_relationTypes(request,repo_name):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			path = "./repos/"+repo_name+"/relation_types/"+request.FILES['file'].name
			upload_file(request.FILES['file'],path)
			return HttpResponse("Document has been uploaded successfully")
	else:
		form = UploadFileForm()
		return HttpResponse("Unable to upload Document")

# To Upload Dictionaries
def upload_dictionaries(request,repo_name):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			path = "./repos/"+repo_name+"/dictionaries/"+request.FILES['file'].name
			upload_file(request.FILES['file'],path)
			return HttpResponse("Document has been uploaded successfully")
	else:
		form = UploadFileForm()
		return HttpResponse("Unable to upload Document")

# To Upload File 
def upload_file(file,path):
    with open(path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)