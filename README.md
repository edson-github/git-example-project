# Projeto teste Git

## Introdução

Este projeto é um exemplo para treinamento no uso do Git. Ele foi criado para ajudar desenvolvedores a entenderem os conceitos básicos e avançados do controle de versão utilizando Git. Aqui você encontrará exemplos de como criar repositórios, fazer commits, trabalhar com branches, resolver conflitos e muito mais.

Sinta-se à vontade para clonar este repositório e experimentar os comandos e fluxos de trabalho descritos na documentação. Boa sorte e bons commits!


# Principais comandos e exemplos de uso

## Comandos Básicos do Git

### Inicializar um repositório
```sh
git init
```
Inicializa um novo repositório Git.

### Clonar um repositório
```sh
git clone <url-do-repositorio>
```
Clona um repositório existente.

### Verificar o status do repositório
```sh
git status
```
Mostra o estado das alterações no repositório.

### Adicionar arquivos ao staging
```sh
git add <arquivo>
```
Adiciona um arquivo específico ao staging.

### Fazer commit das alterações
```sh
git commit -m "mensagem do commit"
```
Faz commit das alterações no staging com uma mensagem descritiva.

### Ver o histórico de commits
```sh
git log
```
Exibe o histórico de commits.

## Trabalhando com Branches

### Criar uma nova branch
```sh
git branch <nome-da-branch>
```
Cria uma nova branch.

### Trocar para uma branch existente
```sh
git checkout <nome-da-branch>
```
Muda para a branch especificada.

### Mesclar uma branch
```sh
git merge <nome-da-branch>
```
Mescla a branch especificada na branch atual.

### Deletar uma branch
```sh
git branch -d <nome-da-branch>
```
Deleta a branch especificada.

## Resolvendo Conflitos

### Listar branches com conflitos
```sh
git branch --merge
```
Lista branches que têm conflitos de merge.

### Resolver conflitos manualmente
Edite os arquivos com conflitos e remova as marcações de conflito (`<<<<<<<`, `=======`, `>>>>>>>`). Depois, adicione os arquivos resolvidos ao staging e faça commit.

## Comandos do GitHub

### Fazer fork de um repositório
Clique no botão "Fork" na página do repositório no GitHub.

### Criar um pull request
1. Faça commit e push das suas alterações para uma branch no seu fork.
2. Vá até a página do repositório original no GitHub.
3. Clique em "New pull request" e selecione a branch do seu fork.

### Sincronizar seu fork com o repositório original
```sh
git remote add upstream <url-do-repositorio-original>
git fetch upstream
git merge upstream/main
```
Adiciona o repositório original como remoto e mescla as alterações na sua branch principal.