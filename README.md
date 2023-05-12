# testes_django
fazendo testes com assuntos referentes a django

# adicionando imagens e usando essas imagens

- 1: use um tipo de campo no seu model que use o ImageField();

**obs**: existe um atributo no ImageField chamado `upload_to` que será para onde a imagem irá após o salvamento. você precisará criar uma pasta `midia` no diretorio raiz do seu projeto. no **upload_to** você irá colocar a pasta que estará na media ao qual a imagem irá. **ex: upload_to="imagens/"**, neste exemplo, a imagem carregada será enviada para a pasta: `media/imagens`

- 2: ajuste suas urls de media no arquivo `settings.py` do seu projeto:

```python
# configuração dos diretorios de midia:
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
```

no arquivo `urls.py` do seu projeto adicione:

```python 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
``` 

- 3: crie uma classe na sua aplicação para trabalhar com forms:

arquivo `forms.py`:

```python
from django import forms

class MyForms(forms.Form):
    imagem = forms.ImageField()
```

- 4: no template onde estiver o form você precisará usar as seguintes atributos:

- coloque isto na tag form: enctype="multipart/form-data"
- dentro da tag form use: {{ form.as_p }}

- 5: na view conrespondente ao salvamento da imagem faça:

```python
from . import forms

def create(request):
    form = forms.MyForms(request.POST, request.FILES)
    user = User(nome=request.POST["nome"], foto=request.FILES['foto'])
    user.save()
    return HttpResponseRedirect(reverse('user:home'))
```

com isso você poderá adicionar imagens a qualquer tipo de models, claro isso é só feito para a fase de desenvolvimento. na parte de produção você terá que usar outras ferramentas e meios.


