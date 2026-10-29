# Backend

API REST em Flask com PostgreSQL. O serviço expõe uma verificação de conexão
com o banco e uma rota para consultar usuários.

## Formas de executar

Há duas formas de rodar o projeto. **Escolha uma delas:**

1. **Via Docker Compose**: inicia a API e o PostgreSQL em contêineres. É a opção
   mais simples para executar o projeto completo.
2. **Localmente**: inicia a API diretamente na sua máquina. Nesse caso, você
   precisa ter um PostgreSQL em execução e configurado separadamente.

As instruções de cada opção estão nas seções abaixo. Em ambas, a API oferece os
mesmos endpoints; muda apenas o endereço: `http://localhost:8080` via Docker
Compose ou `http://localhost:5000` localmente.

## Requisitos

- Docker com Docker Compose; ou Python 3.10+ e PostgreSQL para executar sem Docker.

## Configuração das variáveis

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_HOST=database
DATABASE_NAME=backend
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
```

As variáveis são usadas pela aplicação para conectar ao banco. No Docker Compose,
`DATABASE_HOST` deve ser `database`, o nome do serviço PostgreSQL. Para execução
local da API, configure `DATABASE_HOST` com o endereço do PostgreSQL acessível
pela sua máquina (por exemplo, `localhost`).

| Variável            | Descrição                   |
| ------------------- | --------------------------- |
| `DATABASE_HOST`     | Host do servidor PostgreSQL |
| `DATABASE_NAME`     | Nome do banco de dados      |
| `DATABASE_USER`     | Usuário do banco            |
| `DATABASE_PASSWORD` | Senha do usuário do banco   |

O arquivo `.env` contém credenciais e não deve ser compartilhado ou enviado ao
controle de versão.

## Executar com Docker Compose

Na raiz do projeto, com o `.env` configurado, execute:

```bash
docker compose up --build
```

A API ficará disponível em `http://localhost:8080`. O PostgreSQL é iniciado
junto com a API, e o arquivo `init.sql` cria a tabela `users` e insere alguns
registros de exemplo na primeira inicialização do volume do banco.

Para encerrar os serviços, pressione `Ctrl+C` e execute:

```bash
docker compose down
```

## Executar localmente

Com um PostgreSQL em execução e as variáveis de ambiente configuradas para esse
banco:

Crie e ative o ambiente virtual Python:

```bash
python -m venv .venv       # Cria um ambiente virtual no diretório .venv
source .venv/bin/activate  # Ativa o ambiente virtual (Linux/macOS)
```

No Windows PowerShell, use este comando para ativar o ambiente virtual:

```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências e inicie a API:

```bash
pip install -r requirements.txt
python app.py
```

Ao executar localmente, a API escuta na porta `5000`. Configure o banco com a
mesma estrutura definida em `init.sql` antes de consultar `/users`.

## Endpoints

### `GET /health`

Verifica a conexão com o PostgreSQL.

```bash
curl -i http://localhost:8080/health
```

Quando a conexão funciona, a resposta é `200 OK`:

```json
{ "message": "Database connection is working!" }
```

Se a conexão falhar, a rota retorna `400 Bad Request`.

### `GET /users`

Retorna os usuários cadastrados na tabela `users`.

```bash
curl -i http://localhost:8080/users
```

Com registros disponíveis, a resposta é `200 OK`, por exemplo:

```json
{
	"message": "Users retrieved successfully!",
	"users": [{ "id": 1, "name": "JOSÉ", "email": "jose@gmail.com" }]
}
```

Se a tabela não tiver usuários, a resposta é `404 Not Found`:

```json
{ "message": "No users found!" }
```

Se estiver executando a API localmente, substitua `8080` por `5000` nos
comandos `curl`.
