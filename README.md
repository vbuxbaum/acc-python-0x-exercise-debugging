> <!-- # **Diretrizes de como usar o template para lição de Exercício como projeto ** -->

> <!-- O template contém um direcional de como deve ser a estrutura padrão dessa lição. -->

<!--⚠️ **_Ao produzir uma nova lição de exercício como projeto, copie esse template para o dia de conteúdo que está produzindo._**-->

<!-- - Edite os pontos necessários de acordo com a legenda abaixo:-->

<!-- > `[atualizar]`: Itens de preenchimento obrigatórios pelo time de Currículo (HS,SK e BT). As orientações de como preencher esse template estão em formato de comentários.Utilize-as para garantir que o uso do template está de acordo com as premissas da nossa Metodologia Trybe. -->

<!-- >`[HS]`: Orientações destinadas ao time de Hard Skills -->

<!-- >`[SK]`: Orientações destinadas ao time de Soft Skills -->

<!-- >`[BT]`: Orientações destinadas ao time de Busca por Trabalho -->

<!-- Os exercícios como projeto ajudam previamente as pessoas estudantes a realizar os projetos, pois possuem um repositório no Github com avaliadores automatizados. Esses exercícios possuem um nível de dificuldade menor, se comparados aos projetos, e não valem nota. Nesse sentido, são um instrumento de avaliação formativa durante o processo de aprendizagem. -->

<!-- Uma premissas da criação de novos exercícios como projetos é que eles devem caber no tempo disponível no dia para sua realização. Mais especificamente, todos os exercícios como projeto devem ocupar no máximo 75% do tempo disponível no dia. Este tempo é a soma do tempo para exercícios com o tempo de mentoria técnica.
Para estimarmos o tempo que uma pessoa estudante leva para fazer um exercício, seguimos a seguinte regra: 2,5x o tempo que uma pessoa com domínio do conteúdo leva para realizá-lo. -->

# Boas-vindas ao repositório do exercício `[atualizar]`

Para realizar o exercício, atente-se a cada passo descrito a seguir e se tiver **qualquer dúvida**, nos envie no _Slack_ da turma! #vqv 🚀

Aqui, você vai encontrar os detalhes de como estruturar o desenvolvimento do seu exercício a partir desse repositório, utilizando uma branch específica e um _Pull Request_ para colocar seus códigos.

<br />

# Termos e acordos

Ao iniciar este exercício, você concorda com as diretrizes do [Código de Conduta e do Manual da Pessoa Estudante da Trybe](https://app.betrybe.com/learn/student-manual/codigo-de-conduta-da-pessoa-estudante).

<br />

# Entregáveis

<details>
<summary><strong>🤷🏽‍♀️ Como entregar</strong></summary><br />

Para entregar o seu exercício, você deverá criar um _Pull Request_ neste repositório.

Lembre-se que você pode consultar nosso conteúdo sobre [Git & GitHub](https://app.betrybe.com/learn/course/5e938f69-6e32-43b3-9685-c936530fd326/module/fc998c60-386e-46bc-83ca-4269beb17e17/section/fe827a71-3222-4b4d-a66f-ed98e09961af/day/1a530297-e176-4c79-8ed9-291ae2950540/lesson/2b2edce7-9c49-4907-92a2-aa571f823b79) e nosso [Blog - Git & GitHub](https://blog.betrybe.com/tecnologia/git-e-github/) sempre que precisar!

</details>
  
<details>
<summary><strong>🧑‍💻 O que deverá ser desenvolvido</strong></summary><br />

<!-- Explicar brevemente o que será realizado ao longo do exercício. Aqui, é a porta de entrada para o exercício como projeto. 
Exemplo: Vamos fazer um exercício que vai deixar nítido como funções,com responsabilidades bem definidas,deixam o código mais bem escrito. Para isso, vamos criar uma série de funções com respostas já definidas e exercitar nossa lógica de programação.
-->

`[atualizar]`
<br />

</details>
  
<details>
  <summary><strong>:memo: Habilidades a serem trabalhadas</strong></summary><br />

Neste exercício, verificamos se você é capaz de:

`[atualizar]`
<!-- habilidade -->
`[atualizar]`
<!-- habilidade -->
`[atualizar]`
<!-- habilidade -->

<!-- [HS] Escrevam as habilidade utilizando a Taxonomia de Bloom. -->

</details>

<br/>

# Orientações
  
<details>

   <summary><strong>‼ Antes de começar a desenvolver </strong></summary><br />

<!-- [HS] Aqui, deve-se adicionar os comandos mais utilizados e orientações de como preparar o repositório. Atualize o nome do repositório do exercício nas instruções a seguir -->

1. Clone o repositório

- Use o comando: `[atualizar]`
- Entre na pasta do repositório que você acabou de clonar:
  - `[atualizar]`

2. Instale as dependências

- npm install

3. Crie uma branch a partir da branch `main`

- Verifique que você está na branch `main`
  - Exemplo: `git branch`
- Se você não estiver, mude para a branch `main`
  - Exemplo: `git checkout main`
- Agora, crie uma branch à qual você vai submeter os `commits` do seu exercício:
  - Você deve criar uma branch no seguinte formato: `nome-sobrenome-nome-do-exercício`;
  - Exemplo: `git checkout -b maria-soares-lessons-learned`

4. Crie na raiz do exercício os arquivos que você precisará desenvolver:

- Verifique que você está na raiz do exercício:
  - Exemplo: `pwd` -> o retorno vai ser algo tipo _/Users/maria/code/**sd-0x-project-lessons-learned**_
- Crie os arquivos index.html e style.css:
  - Exemplo: `touch index.html style.css`

5. Adicione as mudanças ao _stage_ do Git e faça um `commit`

- Verifique que as mudanças ainda não estão no _stage_:
  - Exemplo: `git status` (devem aparecer listados os novos arquivos em vermelho)
- Adicione o novo arquivo ao _stage_ do Git:
  - Exemplo:
    - `git add .` (adicionando todas as mudanças - _que estavam em vermelho_ - ao stage do Git)
    - `git status` (devem aparecer listados os arquivos em verde)
- Faça o `commit` inicial:
  - Exemplo:
    - `git commit -m 'iniciando o exercício. VAMOS COM TUDO :rocket:'` (fazendo o primeiro commit)
    - `git status` (deve aparecer uma mensagem tipo _nothing to commit_ )

6. Adicione a sua branch com o novo `commit` ao repositório remoto

- Usando o exemplo anterior: `git push -u origin maria-soares-lessons-learned`

7. Crie um novo `Pull Request` _(PR)_

- Vá até a página de _Pull Requests_ do [repositório no GitHub](https://github.com/tryber/sd-0x-project-lessons-learned/pulls)
  - Clique no botão verde _"New pull request"_
  - Clique na caixa de seleção _"Compare"_ e escolha a sua branch **com atenção**
- Coloque um título para o seu _Pull Request_
  - Exemplo: _"Cria tela de busca"_
- Clique no botão verde _"Create pull request"_

- Adicione uma descrição para o _Pull Request_, um título nítido que o identifique, e clique no botão verde _"Create pull request"_

 <img width="1335" alt="Exemplo de pull request" src="https://user-images.githubusercontent.com/42356399/166255109-b95e6eb4-2503-45e5-8fb3-cf7caa0436e5.png">

- Volte até a [página de _Pull Requests_ do repositório](https://github.com/tryber/sd-0x-project-lessons-learned/pulls) e confira que o seu _Pull Request_ está criado

</details>

<details>

<summary><strong>⌨️ Durante o desenvolvimento</strong></summary><br />

Faça `commits` das alterações que você fizer no código regularmente, pois assim você garante visibilidade para o time da Trybe e treina essa prática para o mercado de trabalho :) ;

- Lembre-se de sempre após um (ou alguns) `commits` atualizar o repositório remoto;
- Os comandos que você utilizará com mais frequência são:

  - `git status` _(para verificar o que está em vermelho - fora do stage - e o que está em verde - no stage)_;
  - `git add` _(para adicionar arquivos ao stage do Git)_;
  - `git commit` _(para criar um commit com os arquivos que estão no stage do Git)_;
  - `git push -u origin nome-da-branch` _(para enviar o commit para o repositório remoto na primeira vez que fizer o `push` de uma nova branch)_;
  - `git push` _(para enviar o commit para o repositório remoto após o passo anterior)_.

</details>

<details>
<summary><strong>🎛 Linter</strong></summary><br />

Para garantir a qualidade do código, vamos utilizar neste exercício o `ESLint`. Assim o código estará alinhado com as boas práticas de desenvolvimento, sendo mais legível e de fácil manutenção! Para poder rodar o `ESLint` certifique-se de ter executado o comando `npm install` dentro do repositório.

Para rodá-los localmente no repositório, execute os comandos abaixo:

```bash
npm run lint
```

Se a análise do `ESLint` encontrar problemas no seu código, tais problemas serão mostrados no seu terminal. Se não houver problema no seu código, nada será impresso no seu terminal.

Você pode também instalar o plugin do `ESLint` no `VSCode`. Para isso, basta fazer o download do [plugin `ESLint`](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) e instalá-lo.

Em caso de dúvidas, confira o material na plataforma sobre [ESLint e Stylelint](https://app.betrybe.com/course/real-life-engineer/eslint).

⚠️ **PULL REQUESTS COM ISSUES NO LINTER NÃO SERÃO AVALIADAS. ATENTE-SE PARA RESOLVÊ-LAS ANTES DE FINALIZAR O DESENVOLVIMENTO!** ⚠️

</details>
  
<details>
<summary><strong>🛠 Testes</strong></summary><br />

<!-- Escrever as intruções sobre os testes.-->

`[atualizar]`

</details>

# Requisitos

## 1. Identifique e corrija os erros no arquivo `src/word_finder.py`

No arquivo `src/word_finder.py` há um código que deveria retornar uma lista de linhas de um arquivo que contém uma determinada palavra. Porém, há alguns erros no código que impedem que ele funcione corretamente. Identifique e corrija os erros no código.

<details>

<summary> [atualizar] </code>
</summary><br/>

<!-- Explicação do requisito, regras de negócio esperadas. -->

**O que será testado:**

<!-- Descritivo do que será testado nesse requisito. -->

 `[atualizar]`

</details>

## 2.`[atualizar]`

<!-- Descrição do requisito, iniciado com verbo no imperativo (crie, filtre, faça, encontre) -->

<details>

<summary> [atualizar] </code>
</summary><br/>

<!-- Explicação do requisito, regras de negócio esperadas. -->

**O que será testado:**

<!-- Descritivo do que será testado nesse requisito. -->

 `[atualizar]`

</details>

<details>
<summary><strong> 🗣 Nos dê feedbacks sobre o exercício!</strong></summary><br />

Ao finalizar e submeter o exercício, não se esqueça de avaliar sua experiência preenchendo o [formulário](https://be-trybe.typeform.com/to/ZTeR4IbH).
**Leva menos de 3 minutos!**

</details>

---
