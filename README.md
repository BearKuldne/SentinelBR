# SentinelBR 🔐

Sistema de monitoramento de arquivos desenvolvido em Python utilizando a biblioteca Watchdog.

## Funcionalidades

* Monitoramento em tempo real;
* Detecção de criação de arquivos;
* Detecção de modificação de arquivos;
* Detecção de exclusão de arquivos;
* Autenticação por senha para autorizar alterações;
* Criação automática da pasta monitorada.

## Tecnologias utilizadas

* Python 3.14
* Watchdog
* Tkinter
* Git
* GitHub

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/BearKuldne/SentinelBR.git
```

### 2. Entre na pasta do projeto

```bash
cd SentinelBR
```

### 3. Instale a dependência

```bash
pip install watchdog
```

### 4. Configure a pasta monitorada

Abra o arquivo `Main.py` e altere o caminho da pasta que será monitorada para o diretório desejado.

### 5. Configure a senha

Abra o arquivo `senha.py` e altere o valor da variável:

```python
senha_correta = "123456"
```

para a senha de sua preferência.

### 6. Execute o programa

```bash
python Main.py
```

## Versão atual

**v2.0**

### Novidades da versão 2.0

* Sistema de autenticação por senha utilizando Tkinter;
* Janela gráfica para solicitação da senha;
* Mensagens de confirmação para autenticação;
* Código reorganizado em módulos.

## Objetivo

Projeto desenvolvido com o objetivo de estudar conceitos de monitoramento de arquivos, controle de acesso e eventos relacionados à segurança da informação.

## Próximas funcionalidades (v3.0)

* Proteção contra exclusão não autorizada de arquivos;
* Restauração automática de arquivos apagados;
* Bloqueio (por reversão) de modificações sem autorização;
* Sistema de backup automático.
