#Server

Geral
O servidor recebe como parametros um endereço IP, uma porta e um diretório onde ele irá buscar os arquivos.
Com isso o servidor cria um socket de rede e fica escutando a espera de uma conexão.
Ao receber uma nova conexão, o servidor aguarda o recebimento de pacotes, ao receber ele analisa o tipo de informação que o cliente deseja.
O cliente pode solicitar um arquivo ou solicitar o nome dos arquivos armazenados na cache.
Caso solicite um arquivo, o servidor busca no diretorio passado como parâmetro o arquivo soliciado, caso exista, o arquivo é carregado logo em seguida é enviado para o cliente por meio da conexão estabelecida. Ao enviar o arquivo, o servidor salva o mesmo numa cache de dados para melhorar o desempenho em possíveis requisições futuras.
Caso o cliente solicite a lista dos arquivos em cache, o servidor envia o nome dos arquivos armazenados.

Multi Threading
Toda vez que um cliente solicita uma conexão com o servidor, é criado uma nova thread para atender as requisições deste cliente, isso permite que o servidor consiga atenter mais clientes de forma simultânea.

Cache
O servidor implementa uma cache de 64MB utilizada para armazenar arquivos solicitados pelos clientes para melhorar o desempenho.
Toda vez que um arquivo é solicitado o servidor verifica se o mesmo já existe na cache, caso não exista busca o arquivo no HD, envia e salva o mesmo na cache caso haja espaço disponível.
Caso não haja espaço disponível na cache, o servidor remove continuamente arquivos até que exista espaço para armazenar o arquivo atual. Para remover arquivos, o servidor utiliza o princípio da localidade temporal, removendo os arquivos menos recentemente acessados até que haja espaço disponível.


#Cliente

O cliente recebe as informações do servidor, IP e Porta, com isso consegue solicitar uma conexão.
Após aberta, cliente pode solicitar arquivos ou solicitar os arquivos armazenados na cache. Ao solicitar a lista de arquivos, ele fica aguardando a resposta do servidor com a lista dos arquivos, ao receber, imprime na tela. 
Ao solicitar um arquivo no terminal, o cliente fica aguardando do servidor uma resposta, caso o carquivo exista o cliente vai ler continuamente pacotes de 1024 bytes e salvar continuamente em um arquivo até que todo o arquivo enviado pelo servidor seja escrito no arquivo respectivo armazenado no diretorio especificado como parametro.
