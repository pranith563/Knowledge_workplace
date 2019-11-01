import requests, base64
from requests.auth import HTTPBasicAuth
import json

# data_string = "neo4j:password"
# data_bytes = data_string.encode("utf-8")
# b64_val = base64.b64encode(data_bytes)
# auth = requests.get,headers={"Authorization": "Basic %s" % b64_val})

# print(auth.json())

prefix = ''
length_prefix = len(prefix)
url = "http://localhost:7474/db/data/"
def getLabels(prefix):
	r = requests.get(url+"labels",auth=HTTPBasicAuth('neo4j', 'password'))
	labels = []
	for i in r.json():
		p = i[:length_prefix]
		if(p==prefix):
			label = i[length_prefix+1:]
			labels.append(label)
	return labels

def getProperties(prefix):
	r = requests.get(url+"propertykeys",auth=HTTPBasicAuth('neo4j', 'password'))
	properties = []
	for i in r.json():
		p = i[:length_prefix]
		if(p==prefix):
			property = i[length_prefix+1:].lower()
			properties.append(property)
	return properties

def getUri(r):
	return r.json()['data']['uri'][length_prefix+1:]

def getNode(id):
	r = requests.get(url+"node/"+str(id),auth=HTTPBasicAuth('neo4j', 'password'))
	metadata  = r.json()['metadata']
	data = r.json()['data']
	data['id'] = metadata['id']
	return data

def getId(entity, value):
	data = {
			"query" : "MATCH (n:`http://www.iiitb.com/ontologies/iiitb.owl#"+entity+
			"`{uri:'http://www.iiitb.com/ontologies/iiitb.owl#"+value+"'}) RETURN n" ,
   			"params" : { }
	}
	r = requests.post(url+"cypher",auth=HTTPBasicAuth('neo4j', 'password'),json=data)
	return r.json()['data'][0][0]['metadata']['id']


def getId_new(entity, value):
	data = {
			"query" : "MATCH (n:`"+prefix+"#"+entity+
			"`{uri:'"+prefix+"#"+value+"'}) RETURN n" ,
   			"params" : { }
	}
	r = requests.post(url+"cypher",auth=HTTPBasicAuth('neo4j', 'password'),json=data)
	return r.json()['data'][0][0]['metadata']['id']


def findPath_v1(e1,e2):
	url="http://localhost:7474/db/data/cypher"
	data = {"query" : "MATCH (from:`http://www.iiitb.com/ontologies/iiitb.owl#Institute`{uri:'http://www.iiitb.com/ontologies/iiitb.owl#"+e1+"'}) ,(to:`http://www.iiitb.com/ontologies/iiitb.owl#Branch`{uri:'http://www.iiitb.com/ontologies/iiitb.owl#"+e2+"'}) call apoc.algo.allSimplePaths(from,to,'',5) yield path as path return path",
   	"params" : { }
	}
	r = requests.post(url,auth=HTTPBasicAuth('neo4j', 'password'),json=data)
	for i in r.json()['data']:
		print("path",i[0]['nodes'])
		for j in i[0]['nodes']:
			print(getUri(getNode(j[35:])))

def findPath_v2(e1,e2):
	url="http://localhost:7474/db/data/cypher"
	data = {
	"query" : "MATCH (from:`http://www.iiitb.com/ontologies/iiitb.owl#Institute`"+
			"{uri:'http://www.iiitb.com/ontologies/iiitb.owl#"+e1+"'}) ,"+
			"(to:`http://www.iiitb.com/ontologies/iiitb.owl#Branch`"+
			"{uri:'http://www.iiitb.com/ontologies/iiitb.owl#"+e2+"'})"+
			" call apoc.algo.allSimplePaths(from,to,'',5) yield path as path return path",
   	"params" : { }
	}
	r = requests.post(url,auth=HTTPBasicAuth('neo4j', 'password'),json=data)
	for i in r.json()['data']:
		print('path ', i[0])
		print('')

def getPaths(source,dest):
	path_url= url + "node/"+str(source)+"/paths"
	data = {
		"to" : url+"node/"+str(dest),
  		"max_depth" : 2,
  		"algorithm" : "allPaths"
	}
	r = requests.post(path_url,auth=HTTPBasicAuth('neo4j', 'password'),json=data)
	paths = []
	for i in r.json():
		paths.append(i['nodes'])
	return paths


#findPath_v1('IIITB','CSE')
#findPath_v2('IIITB','ECE')
#print(getLabels('iiitb'))
#getId('Institute','IIITB')
#print(getProperties(prefix))
#getPaths('34','16')