# Projeto Chave Triangulo

Esse foi um projeto pessoal 100% pensando e desenvolvido por mim. Este é um aplicativo que combina lógica matemática, geração de chaves únicas, armazenamento no mysql e uma interface gráfica intuitiva, criado como um exercício de programação criativa e funcional.

## Sobre o Projeto
O **Projeto Chave Triangulo** é uma aplicação desktop que permite aos usuários gerar chaves únicas baseadas em lados de um triângulo fornecidos como entrada. O projeto foi pensado do zero por mim, desde a ideia inicial até a implementação, com foco em modularização, orientação a objetos e uma experiência de usuário simples.

### Funcionalidades
- **Entrada de Dados**: O usuário insere três lados de um triângulo (valores inteiros entre 1 e 59).
- **Validação**: Verifica se os lados estão no intervalo permitido e se são todos diferentes.
- **Cálculo**: Identifica o maior lado, calcula seu fatorial e eleva o resultado ao cubo.
- **Geração de Chave**: Combina o resultado matemático com um timestamp (formato DDMMYYHHMMSS) e um número aleatório de 7 dígitos, ao gerar essa primeira chave, é calculado a diferença entre a quantidades de caracteres e o valor 255(a chave precisa ter 255 digitos), com o valor da diferença é gerado uma segunda chave aleatorio para complementar a primeira chave e o valor chegar a 255 caracteres, criando uma chave única.
- **Autenticação**: Inclui sistema de login e registro de usuários.
- **Persistência**: Armazena as chaves geradas em um banco de dados MySQL, vinculadas ao usuário autenticado.
- **Visualização**: Exibe as chaves geradas

## Estrutura do Projeto
O projeto segue uma arquitetura modular e orientada a objetos, organizada da seguinte forma:

```
triangle_key_generator/
├── main.py               # Ponto de entrada da aplicação
├── config.py             # Configurações do banco de dados
├── requirements.txt      # Dependências do projeto
├── app/                  # Módulo principal
│   ├── __init__.py
│   ├── gui.py            # Interface gráfica com Tkinter
│   ├── key_generator.py  # Lógica de geração de chaves
│   ├── auth/             # Autenticação de usuários
│   │   ├── __init__.py
│   │   ├── auth.py
│   ├── database/         # Gerenciamento do banco de dados
│   │   ├── __init__.py
│   │   ├── database.py
│   ├── core/             # Lógica central
│   │   ├── __init__.py
│   │   ├── validation.py # Validação dos lados
│   │   ├── calculations.py # Cálculos matemáticos
│   │   ├── utils.py      # Funções auxiliares
└── tests/                # Testes unitários (em desenvolvimento)
    ├── __init__.py
    ├── test_auth.py
    ├── test_calculations.py
    ├── test_database.py
```

## Tecnologias Utilizadas
- **Python 3.x**: Linguagem principal.
- **Tkinter**: Biblioteca para a interface gráfica.
- **MySQL Connector**: Integração com banco de dados MySQL.
- **Hashlib**: Para criptografia de senhas (SHA-256).
- **Bibliotecas Nativas**: `random`, `datetime`, `math`, `string`.



## Notas Técnicas
- O projeto é um trabalho em progresso, com planos para adicionar testes unitários e melhorias na interface.

## Autor
Este projeto foi 100% idealizado e desenvolvido por **[Weslley Santos]**, como um desafio pessoal para explorar conceitos de programação, matemática e design de software. Sinta-se à vontade para entrar em contato comigo para sugestões ou colaborações!

## Licença
Este é um projeto pessoal e não possui licença formal no momento. Todos os direitos são reservados ao autor.

