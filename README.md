# Ethereum File Signing and Verification
Este projeto demonstra como usar a biblioteca `web3.py` para assinar e verificar arquivos usando a blockchain Ethereum. O código realiza o seguinte:

1. Conecta-se a um nó Ethereum local.
2. Converte UUIDs para endereços e chaves privadas no formato hexadecimal necessário para Ethereum.
3. Calcula o hash SHA-256 de um arquivo.
4. Assina o hash do arquivo usando a chave privada.
5. Verifica a assinatura do arquivo.

## Requisitos

- Python 3.x
- `web3.py` library
- `hashlib` library

## Instalação

1. Instale as dependências do projeto:

    ```bash
    pip install web3
    ```

2. Certifique-se de que o `geth` (Go Ethereum) está instalado e executando um nó Ethereum local. Para instalar o `geth`, siga as instruções abaixo.

## Executando o Geth

Para instalar e executar o `geth`, siga estas etapas:

1. **Instalação do Geth:**

    - **Para Linux:**

      ```bash
      sudo apt-get update
      sudo apt-get install software-properties-common
      sudo add-apt-repository -y ppa:ethereum/ethereum
      sudo apt-get update
      sudo apt-get install geth
      ```

    - **Para macOS:**

      ```bash
      brew tap ethereum/ethereum
      brew install ethereum
      ```

    - **Para Windows:**

      Baixe o instalador do Geth [aqui](https://geth.ethereum.org/downloads/) e siga as instruções de instalação.

2. **Executando o Geth:**

    Para iniciar um nó Ethereum local, execute o seguinte comando:

    ```bash
    geth --dev --http --http.api personal,db,eth,net,web3,miner
    ```

    Este comando inicializa o nó no modo de desenvolvimento e habilita a API HTTP necessária para se conectar ao nó.

## Executando o Projeto

1. Clone o repositório e acesse o diretório do projeto:

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Execute o script:

    ```bash
    python3 test.py
    ```

O script calculará o hash de um arquivo, assinará o hash usando uma chave privada e verificará a validade da assinatura.

## Estrutura do Código

- `uuidToHex(uuidStr)`: Converte uma string UUID para hexadecimal.
- `formatForEthereum(hexValue, length)`: Ajusta uma string hexadecimal para o comprimento necessário.
- `calculateFileHash(filePath)`: Calcula o hash SHA-256 de um arquivo.
- `signMessage(messageBytes, privateKey)`: Assina uma mensagem usando a chave privada.
- `verifySignature(messageBytes, signature, accountAddress)`: Verifica a validade de uma assinatura.

## Licença
Este projeto está licenciado sob a open source

