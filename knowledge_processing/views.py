from django.shortcuts import render
from django.http import HttpResponse
from . import extractor 
import os
def index(request):
    return HttpResponse("Welcome to Knowledge_processing unit")

# API To process the docs
def process_text(request,repo_name,docs):
	for doc_name in docs:
		path = repo_name+"/docs/"+doc_name
		fd = os.open(path,'r')
		doc = fd.read()
		doc = extractor.co_reference(doc)
	return HttpResponse("Extracted relations successfully")

# API to extract entities from unstructured text
def extract_entites(request,repo_name,docs):
	for doc_name in docs:
		path = repo_name + "/docs" + doc_name
		fd = os.open(path,'r')
		text = fd.read()
		entites = extractor.entites(text)
	return HttpResponse("Extracted entites successfully")