from pathlib import Path

# Escrevendo e lendo de um arquivo texto.
diretorio = Path('meu_arquivo_texto')
diretorio.write_text('Conteúdo do arquivo texto')
texto = diretorio.read_text()
print(texto)
print('---------------\n')

# Escrevendo e lendo de um arquivo em bytes.
diretorio = Path('meu_arquivo_binario')
diretorio.write_bytes(b'Conteudo do arquivo binario')
texto = diretorio.read_bytes()
print(texto)
