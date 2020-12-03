#DJango REST Framework

Link udemy: https://www.udemy.com/course/apis-restful-com-django-rest-framework/
Link repositório git: https://github.com/gustavolio/DjangoREST-APIPontosTuristicos
Link API heroku (Consumir via postman): https://touristic-points-api.herokuapp.com/ 

***
###1.Conceitos Fundamentais
***

* RestFul API: Interface de comunicação entre aplicações e usuários, implementada sobre uma arquitetura HTTP de forma padronizada assim como representação dos seus dados;

* API: Application Programming Interface, conjunto de rotinas e padrões que permitem outras aplicações usarem seus recursos sem a necessidade do conhecimento de detalhes sobre sua implementação;

* REST: Representational State Transfer, estilo arquitetural (principios e regras) p/ a comunicação entre aplicações;

* Verbos HTTP:
	- GET recuperar um recurso;
	- POST criar um novo recurso;
	- PUT atualizar o estado de um recurso;
	- PATCH atualizar parte de um recurso;
	- DELETE remover um recurso existente;

* JSON: Javascript Object Notation;

* DJango REST: Baseado no DJango para construção rápida sobre API Restful API's.

***
###2.Configuração do Ambiente
***

* Windows:
	- Instalar o python;
	- Instalar o pycharm(opcional);
	- Criar uma pasta para o projeto;
	- Dentro dessa pasta inicializar uma venv: python -m venv venv;
	- Ativar venv no terminal na pasta do projeto: venv\Scripts\activate
	- Instalar o django na venv: pip install django 

* Criando projeto (DJango):
	- Com a venv ativada...
	- Criar o projeto django: django-admin start-project <nome_do_projeto> .
	- Criar migrations: py manage.py makemigrations
	- Popular o banco: py manage.py migrate
	- Criar super usuário: py manage.py createsuperuser
	- Rodar o servidor: py manage.py runserver

* Criando projeto (Django REST Framework):
	- install djangoREST: pip install djangorestframework
	- put 'rest_framework' in INSTALLED_APP on settings.py file

* Run clone project from git:
	- Clone application;
	- Install venv: `python -m venv venv`;
	- Activate venv: `venv\Scripts\activate`;
	- Install django and djangoREST: `pip install django & pip install djangorestframework & pip install django-filter`
	- Install requirements.txt: `pip install -r requirements.txt`;

***
###3.Desenvolvendo uma API de pontos turísticos
***
* Criando uma/um APP
	- Use command py manage.py startapp <name>
	- put <name> app in INSTALED_APP on settings.py file
	- create model and regiter model in admin.py:
		- from .models import <model name>
		-
		- admin.site.register(<model name>)
	- execute 'makemigrations' and 'migrate';
	- create folder 'api' inside app and create three files:
		- __init__.py
		- viewsets.py
		- serializers.py




* API first steps:
	- URL + num = URI. Ex.: \pontos-turisticos/1 (resource identify)

	1) Create Serializers: (https://www.django-rest-framework.org/tutorial/quickstart/)
		- Serializers defined data representarion format;

	2) Create Viewsets: (https://www.django-rest-framework.org/tutorial/quickstart/)
		- Viewsets are use for querys

	3) Create Route:
		- register route:
			router = routers.DefaultRouter()
			router.register(r'route alias', <viewset name>)

		- include route object on url's:
			path('', include(router.urls)),

***
###4.Desenvolvendo Recursos Avançados na API
***
* Overwrite queryset (Section ModelViewSet in: https://www.django-rest-framework.org/api-guide/viewsets/#viewset-actions):
	- define function <get_queryset(self) in viewset>;
	- define <basename> parameter on url of modificated viewset.

* Overwrite default actions of django:
	- list() and create() functions not dependi of key;
	- destroy(), retrieve(), update() and partial_update() functions depend of key;

***
###5.Utilizando na API
***
* Create field on model with image;
* Define MEDIA_ROOT and MEDIA_URL on setting.py;
* Install Pillow with pip install;
* Add field on var field_sets on serializer.py.
* Using (https://docs.djangoproject.com/en/3.0/topics/files/) for development

***
###6.Filtros de querysets
***
* On viewset, take query parameters from self argument;
* Take all model atributes;
* Create filters using if's for False arguments and inside of 'ifs' use Model.filter(<logic expression>)


***
###7.Habilitando buscas na API
***
link: https://www.django-rest-framework.org/api-guide/filtering/
- install django-filter, for this use pip;

* DJangoFilter Backend:
	- add REST_FRAMEWORK variable on settings.py if you implements filtering on all viewsets
			or
	  add import DjangoFilterBackend in viewset and inside class use 'filter_backends' variable;
	- define 'filter_fields' variable with a iterable content desired filters.

* Search Filter:
	- add 'from rest_framework import filters' on viewset
	- add 'filter_backends = [filters.SearchFilter]' inside class viewset
	- define 'search_fields' variable with a iterable content desired filters.
		- use ^, =, @, $ for change type of search

* Lookup field:
	- The default django search field is id, but it's possible change using 'lookup_field' variable;
	- lookup_field = '<field name>'

***
###8.Autenticação e autorização
***
link: https://www.django-rest-framework.org/api-guide/authentication/
* Using token for create autorization in your API;
* Search for Token Authorization in API guide;

***
###9.Aprofundando Conhecimento em Serializers
***
...

***
###10.Colocando API no ar com heroku
***
 * Consultar arquivo com CookBook para deploy no heroku .md;


***
###11.Trabalhando com Nested Relationships
***
(Parei aqui)



