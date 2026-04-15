## Guia inicial | Como começar?

Este documento é um manual inicial para ajudar futuros ingressantes a prepararem seus ambientes de estudos do Code Club. 

> Objetivos desse guia:

- Criar e usar uma conta no **GitHub**; 
- Instalar e usar o **Visual Studio Code**; 
- Preparar arquivos em **Jupyter Notebooks**, utilizando ambiente **Python**;
- Encontrar os desafios no **Rosalind**; 
- Baixar e utilizar o **Discord**. 

----

### 1) Git e GitHub

> O que é Git e GitHub?

O Git é um **sistema de controle de versão** (versionamento). Ele é utilizado para salvar o histórico de códigos de algum projeto, verificar versões antigas de maneira **local**. Já o GitHub é um site que **hospeda em nuvem** projetos que usam Git. Com ele, você pode guardar seus códigos, compartilhar projetos e colaborar com outras pessoas, além de participar de projetos abertos como é o caso do nosso. Site: [https://github.com](https://github.com)

Como criar uma conta no GitHub: entre em [https://github.com](https://github.com), clique em Sign up, crie sua conta e confirme seu e-mail.

> Como instalar o Git:

- Windows: [https://git-scm.com/download/win](https://git-scm.com/download/win)
- Linux: sudo apt install git
- Mac: [https://git-scm.com/download/mac](https://git-scm.com/download/mac)

> Conceitos básicos:

- **Repositório**: pasta do projeto.
- **Branch**: linha paralela de desenvolvimento. 
- **Pull Request**: pedido para juntar sua branch ao projeto principal.

Para aprender mais: [Curso de Git e GitHub | Curso em Vídeo](https://www.youtube.com/watch?v=xEKo29OWILE&list=PLHz_AreHm4dm7ZULPAmadvNhH6vk9oNZA)

----

### 2) Visual Studio Code (VSCode)

O VSCode é um **editor de código** gratuito que nós escolhemos padronizar para programar. É considerado relativamente fácil de integrar com o GitHub, para organizar e contribuir com os projetos.

- Baixe [aqui](https://code.visualstudio.com).
- Extensões importantes: Python, Jupyter, GitHub Pull Requests.
- Como abrir um Jupyter Notebook (.ipynb): criar (Ctrl+Shift+P) > Create New Jupyter Notebook > Ambiente Python.
- Como conectar ao GitHub: clique no ícone do Git na barra à esquerda, faça login e autorize no navegador.

----

### 3) Rosalind

O Rosalind é uma **plataforma de desafios de bioinformática** (DNA, RNA, proteínas, algoritmos).

- Acesse [aqui](https://rosalind.info).
- Usaremos para **escolher** alguns desafios simples e **discutir** as soluções em nossos encontros.

----

### 4) Discord

O Discord é a nossa ferramenta principal de comunicação.

- Faça o download [aqui](https://discord.com/download).
- Você será convidado para acessar a nossa comunidade/canal. Nós centralizamos nossa comunicação por lá.

----

### 5) Estrutura do nosso repositório

```
unesp-code-clubs/
├── README.md (apresentação do projeto, objetivos, como participar)
├── LICENSE
├── desafios_anteriores.md/ 
├── encontros/
│ ├── encontro_DD_MM_AA/
│ │ ├── desafio.md (enunciado)
│ │ ├── solucao_nome1.ipynb
│ │ └── solucao_nome2.ipynb (opcional)
│ ├── encontro_DD_MM_AA/
│ └── [....]
├── tutoriais/
│ ├── guia_inicial.md 
│ └── guia_PR.md

```

> Fluxo: criar branch > adicionar arquivos > commit > push > pull request (PR).

Para compreender melhor esses passos, criamos um [guia](/tutoriais/guia_PR.md) para **facilitar a criação de um Pull Request (PR)**.

- A cada quinzena teremos 1 desafio. Um propõe, todos resolvem, um apresenta e o grupo discute. Após a reunião, o responsável irá adicionar uma nova pasta no repositório, seguindo os templates e mantendo a padronização, mas também aprendendo um pouco de GitHub 

Bem-vindos ao Code Club! Se precisar de ajuda em **qualquer etapa**, sinta-se à vontade para chamar um de nós para te ajudar.
