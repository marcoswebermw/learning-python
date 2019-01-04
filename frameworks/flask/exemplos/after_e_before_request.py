from flask import Flask, request, after_this_request

app = Flask(__name__)

@app.route( "/" )
def index():
    return "<strong>Olá Mundo!</strong>"

@app.route( "/login" )
def login():
    return "<strong>É necessário logar!</strong>"

@app.before_request
def callback_antes_do_request():
    # Pegando o caminho e o método usados na requisição.
    print("Caminho: {} - Método: {}".format(request.path, request.method))
    print('Executado antes do request ser processado.')

@app.after_request
def callback_depois_do_request(response):
    # Valor da resposta.
    resp = response.get_data(as_text=True)
    print( "Resposta depois do request: {}".format(resp) )
    # Alterando a resposta.
    response.set_data( resp + " Alterado" )
    resp = response.get_data(as_text=True)
    print( "Resposta depois do request(ALTERADA): {}".format(resp) )

    print('Executado depois do request ser processado.')
    return response
    
@app.route('/listar')
def listar():
    print('Antes do callback')
    @after_this_request
    def imprimir_ok(response):
        response.headers['estado'] = 'OK'
        print('OK OK OK')
        return response
    return 'Listagem feita'

if __name__ == "__main__":
    app.run()