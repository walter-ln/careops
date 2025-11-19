# CareOps+ — Aplicação Base para Disciplina de DevSecOps  

API simples utilizada nas aulas práticas da disciplina **Segurança de Aplicações (DevSecOps)** – Dell Academy 2025 – IMD/UFRN.

A CareOps+ será evoluída **a cada aula**, integrando os temas:

- SDLC Seguro  
- OWASP Top 10  
- SAST, SCA, DAST  
- Segurança em pipelines  
- Segurança de containers  
- Supply Chain Security  
- SBOM, assinatura e verificação de imagens  
- Pipeline DevSecOps completo  

---

# 1. Estrutura do Projeto

careops/
│
├── init.py
├── database.py          # Simulação mínima (aula 2–3)
├── main.py              # API principal FastAPI
├── models.py            # Modelos da aplicação
├── templates/           # HTML (aplicação simples)
│   └── index.html
├── requirements.txt     # Dependências Python
└── README.md            # Este arquivo

---

# 2. Como rodar a aplicação

## **2.1 Instalar dependências**

No diretório raiz da aplicação:

```bash
pip install -r requirements.txt
````

No Codespaces isso geralmente não é automático.
Execute sempre o comando acima ao abrir o workspace.

⸻

2.2 Executar o servidor

No diretório careops/:

uvicorn main:app --host 0.0.0.0 --port 8000

Se você estiver usando o GitHub Codespaces, a porta será detectada e exposta automaticamente.

Você verá um link assim:

https://<seu-codespace>.app.github.dev


⸻

# 3. Acessar a aplicação (UI)

Abra o navegador e acesse:

https://<seu-codespace>.app.github.dev

Você verá a interface simples em HTML contendo:
	•	mensagem de boas-vindas
	•	mini “calculadora” (nas aulas seguintes)
	•	botão para testar API


4. Acessar a documentação automática (Swagger)

Acesse:
```
/docs
````

Exemplo:

https://<seu-codespace>.app.github.dev/docs

E também o Redoc:

/redoc

Essas interfaces permitem testar a API sem precisar de Postman.

⸻

5. Testar a API

5.1 Testar no navegador

Root:
```
GET /
```

Retorno esperado:

```
{
  "message": "CareOps+ API funcionando. Use /health para checar o status."
}
```
Healthcheck:

GET /health


Retorno:

```
{
  "status": "ok"
}
```


5.2 Testar com curl no Codespaces:

```
curl https://<seu-codespace>.app.github.dev/
curl https://<seu-codespace>.app.github.dev/health


6. Endpoints implementados nesta etapa

Método	Endpoint	Descrição
GET	/	Testa a aplicação e retorna mensagem inicial
GET	/health	Healthcheck usado em CI/CD e monitoramento

Outros endpoints serão adicionados aula a aula.

7. Segurança aplicada (a cada aula)

A CareOps+ evoluirá com:

Aula 1
	•	Conceito geral de SDLC Seguro
	•	Estrutura mínima da aplicação

Aula 2
	•	OWASP Top 10
	•	Primeiras vulnerabilidades intencionais

Aula 3
	•	Testes com pytest
	•	Simulação de erro lógico

Aula 4
	•	CodeQL (SAST)
	•	Correção de vulnerabilidades

Aula 5
	•	SCA com Dependabot e Trivy

Aula 6
	•	DAST com OWASP ZAP

Aula 7
	•	Segurança em containers
	•	Dockerfile seguro

Aula 8
	•	SBOM com Syft
	•	Scanner com Grype

Aula 9
	•	Pipeline DevSecOps completo

8. Problemas comuns (FAQ rápido)

Erro: "Could not import module careops"

Você executou o uvicorn no diretório errado.

Correto:

cd careops/
uvicorn main:app --host 0.0.0.0 --port 8000

Navegador mostra “Not Found”

Possíveis causas:
	•	Porta 8000 não exposta no Codespaces
	•	URL do Codespaces mudou
	•	Servidor não está rodando

Solução:
	•	Confira a aba PORTS
	•	Rode novamente o uvicorn

🧾 9. Licença

Conteúdo exclusivo para uso na disciplina Segurança de Aplicações (DevSecOps) – Dell Academy 2025.

