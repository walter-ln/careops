
## Passo a Passo do Lab 

### Passo 1 – Subir o OWASP Juice Shop no Codespaces

1. Abra seu repositório `careops` no Codespaces.  
2. No terminal, execute:

```bash
docker run --rm -p 3000:3000 bkimminich/juice-shop
````

3. O Codespaces vai detectar a porta 3000 e mostrar um pop-up **“Open in Browser”**.

   * Clique nele **ou** vá em **Ports → 3000 → Open Browser**.
4. Você será redirecionado para uma URL do tipo:

```
https://<seu-codespace>-3000.app.github.dev
```

> Dica: abra essa URL em aba anônima para evitar cookies/estado anterior.

**Checklist rápido:**

* [ ] Container do Juice Shop está rodando no terminal
* [ ] Porta 3000 está aberta no painel “Ports”
* [ ] A tela inicial do Juice Shop apareceu no navegador
