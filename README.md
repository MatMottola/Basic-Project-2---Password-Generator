# Password Generator 🔐

Gerador de senhas seguras via linha de comando, desenvolvido em Python.
Permite configurar comprimento mínimo, inclusão de números e caracteres
especiais, com validação de entrada e exclusão automática de caracteres
ambíguos.

## Funcionalidades

- Comprimento mínimo configurável pelo usuário
- Inclusão opcional de números e caracteres especiais
- Exclusão automática de caracteres ambíguos (O, 0, I, l, 1)
  para evitar confusão visual — critério comum em políticas de senha corporativas
- Exclusão de caracteres problemáticos em formulários web ( : , . + > < etc)
- Garantia de critérios: a senha só é retornada quando atende
  todos os requisitos definidos
- Validação de input com tratamento de erros

## Como usar

```bash
python password_generator.py
```

Siga as instruções no terminal:
