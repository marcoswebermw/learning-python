# Configurando testes
  
Algumas configurações podem ser feitas antes e depois dos testes com o `setUp()` e `tearDown()` respectivamente. Essas configurações podem ser a criação e destruição de objetos, conexões de rede e banco de dados, etc.  

## Suítes de testes
  
Vários testes podem ser adicionados a uma suíte de testes personalizada para serem executados conforme necessário. Isso pode ser feito através da instânciação da classe `unittest.TestSuite()`.  

Os testes podem ser adicionados na suíte pelo método `addTest(Classe('test_metodo'))`. Este método recebe como argumento a classe onde se encontra o método que queremos testar. A classe receberá como parâmetro o nome do método a ser testado dentro de aspas simples.  

