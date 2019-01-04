# Upload de Arquivos
  
O funcionamento do upload de um arquivo em Flask funciona da seguinte maneira:  

- Garantir que o atributo `enctype="multipart/form-data"` do formulário esteja definido para que o navegador transmita seus arquivos.  

- O formulário deverá conter um `<input type=file>` para pegar o arquivo no sistema de arquivos do cliente.  

- Esses arquivos podem ser acessados na aplicação por meio do dicionário `files` pertencente ao o objeto `request`.  

- O arquivo poderá ser salvo no sistema de arquivos através do método `save()`.  

## secure_filename()
  
A função `secure_filename()` do pacote `werkzeug.utils.secure_filename(filename)` é usada garantir que o nome do diretório é seguro. Algumas entradas feitas por usuários bem intencionados ou não, podem gerar problemas para o servidor.  

Hackers podem tentar modificar e executar arquivos dentro do servidor através da passagem de nome de arquivos. Sempre use essa função em nome de arquivos antes de armazenar algo diretamente no sistema de arquivos. Ela garantirá que os nomes de arquivos gerados são seguros.  

## Algumas funções
  
- `send_from_directory('diretorio', 'nome_arquivo')` - A partir do servidor, quando requisitado, ele envia um arquivo para o cliente.  

- `filename` - Atributo do objeto retornado pelo `files` que retorna o nome do arquivo que foi passado pelo cliente. Esse nome não é seguro, tem que ser tratado posteriormente pela função `secure_filename()`.  

## Limitando o tamanho do upload
  
Por padrão o Flask aceita uploads de tamanho ilimitado. Mas isso pode ser configurado através do `app.config['MAX_CONTENT_LENGTH']`. Caso exceda o limite definido será lançada a exceção `RequestEntityTooLarge`.  

> Em servidores de desenvolvimento talvez ocorra o erro `connection reset error` usando essa funcionalidade. O status correto será alcançado normalmente em um servidor WSGI de produção.  

```py
from flask import Flask, Request

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
```

## Exemplo da Documentação
  
```py
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
```  

```py
# Continuação.
from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
```
  
## Referências
  
[Docs Flask Quick Start](http://flask.pocoo.org/docs/1.0/quickstart/#file-uploads);  

[Docs Flask Patterns FileUploads](http://flask.pocoo.org/docs/1.0/patterns/fileuploads/#uploading-files);  
