# 📝 TodoList API - FastAPI

Este é o primeiro projeto prático do módulo de **APIs com FastAPI** do curso.  
O objetivo é criar uma **API simples para gerenciamento de tarefas (ToDo List)**, com rotas para inserir, listar, alterar status e excluir tarefas.

---

## 🚀 Como executar

1. **Clone o repositório** e navegue até a pasta do projeto.
2. **Crie um ambiente virtual** e ative-o:

   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # macOS/Linux
   ```

3. **Instale as dependências**:

   ```bash
   pip install fastapi uvicorn
   ```

4. **Execute o servidor**:

   ```bash
   uvicorn nome_do_arquivo:app --reload
   ```

   > Substitua `nome_do_arquivo` pelo nome do seu script, por exemplo `main` ou `app`.

5. **Acesse a documentação interativa**:

   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - OpenAPI JSON: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

---

## ✅ Funcionalidades disponíveis

| Método | Rota                | Descrição                                 |
|--------|---------------------|-------------------------------------------|
| POST   | `/inserir`          | Adiciona uma nova tarefa                  |
| POST   | `/lista?opcao=0`    | Lista todas as tarefas                    |
| POST   | `/lista?opcao=1`    | Lista apenas tarefas **não realizadas**  |
| POST   | `/lista?opcao=2`    | Lista apenas tarefas **realizadas**      |
| GET    | `/listaUnica/{id}`  | Retorna uma tarefa específica por índice |
| POST   | `/alteraStatus?id=` | Inverte o status de conclusão da tarefa   |
| POST   | `/excluirTarefa?id=`| Remove a tarefa com base no índice        |

---

## 📦 Modelo de dados (Todo)

```json
{
  "tarefa": "Estudar FastAPI",
  "realizada": false,
  "prazo": "2025-07-31"
}
```

- `tarefa` → descrição da atividade (texto)
- `realizada` → se a tarefa já foi concluída (`true` ou `false`)
- `prazo` → data limite da tarefa (opcional)

---

## 🧠 Observações

- Os dados são armazenados **em memória**, ou seja, são perdidos ao reiniciar o servidor.
- Este projeto é apenas didático e serve como base para projetos mais robustos.
- Em versões futuras, o sistema poderá evoluir com banco de dados, autenticação, organização por módulos, etc.

---

### 👨‍💻 Desenvolvido durante os estudos de FastAPI.