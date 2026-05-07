
# Guia de Pull Request no GitHub

## 1. Verificar se o repositório já foi clonado
- Confirme se você já tem o repositório no seu computador.
- Caso não, use:
  ```bash
  git clone <url_do_repositorio>
  ```

## 2. Configuração inicial do Git
- Configure seu nome e email (o **email deve ser o mesmo usado no GitHub**):
  ```bash
  git config --global user.name "Seu Nome"
  git config --global user.email "seu_email@github.com"
  ```

## 3. Atualizar a branch `main` (passo essencial!)
- Antes de criar qualquer branch, atualize a `main`:
  ```bash
  git fetch
  git pull origin main
  ```
- Isso garante que você está trabalhando com a versão mais recente.

## 4. Criar uma nova branch no VSCode
- No canto inferior esquerdo do VSCode, clique no **Nome da branch** (exemplo: Main) > **Create new branch**.
- Nomeie a branch com o título da atividade:
  ```
  nome_atividade
  ```

## 5. Fazer as alterações desejadas
- Vá até a aba nos ícones do lado esquerdo no **Explorer** e edite o que desejar:
  - Adicione código
  - Crie/mova/apague pastas e arquivos

## 6. Commit das alterações
- Vá até a aba nos ícones do lado esquerdo no **Source Control**:
  - Selecione as alterações que vão para o commit (+).
  - Escreva uma mensagem clara descrevendo a alteração.
  - Clique em **Commit**.

## 7. Publicar a branch
- Clique em **Publish Branch** para enviar sua branch ao GitHub.

## 8. Criar o Pull Request
- No GitHub, vá até a aba **Pull Requests**.
- Confira se o PR está indo **da branch correta para a branch correta**  
  (ex.: `nome_atividade` → `main`).

## 9. Revisão e exclusão da branch
- O responsável irá revisar e aprovar.
- Após o merge, a branch será apagada para manter o repositório organizado.

