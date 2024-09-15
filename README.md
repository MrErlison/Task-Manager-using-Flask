# Hackers do Bem - Fase DevSecOps

## Estudo de Caso

### Etapa 2: Desenvolvimento do Sistema

- Task-Manager-using-Flask é uma simples aplicação web para armazenar tarefas todo. O projeto orifinal pode ser acessado clicando [aqui](https://github.com/AdityaBagad/Task-Manager-using-Flask)

- [x] Para executar a aplicação é necessário ter o Docker instalado, em seguida execute `docker compose up -d` na linha de comando.

### Etapa 3: Criação de um pipeline CI/CD

- [x] Compilação: O código deve ser automaticamente compilado a cada commit para assegurar a consistência do ambiente.
- [/] Testes Automatizados: Realizar os Testes unitários, de integração e funcionais são executados.

### Etapa 4: Análise Estática de Código

- [x] Análise Estática de Código: uso do Bandit para analisar o código em busca de vulnerabilidades.
- [x] Análise de Dependência: uso do Owasp Dependency-check

### Etapa 5: Análise Dinâmica de Segurança (DAST)

- [x] uso do OAWSP ZAP Proxy

### Etapa 6: Entrega Contínua (CD)

- [x] Deploy em staging para posterior aprovação, o código é implantado no ambiente de stage para simular a produção.

## Registration Page
Login or Register if you dont have an account

![Registration Page](output/register.jpg)

## Accessing URL's 
User cannot access any URL's if they are not logged in

![Invalid Access](output/invalid-access.jpg)

## After Successfull Login
See all your tasks after successfull login.

![After Login](output/after-login.jpg)

## Add Tasks
Click the **Add Task** link in the side-bar to add tasks

![Image of Yaktocat](output/add-task.jpg)

## View All Tasks
Click the **View All Task** link in the side-bar to see all tasks. You can **Update** and **Delete** Tasks from this page.

![Image of Yaktocat](output/all-tasks.jpg)

## Account Settings
Change your username and password. You can access this by clicking dropdown in the Navbar

![Image of Yaktocat](output/account-settings.jpg)

