<p align="center">
  <img src="https://blog.aevo.com.br/wp-content/uploads/2018/08/Blog-1024x684.png">
</p>

# Dasafio

## Desenvolvedor :octocat:

| [<img src="https://avatars.githubusercontent.com/u/7117011?s=96&v=4" width=115><br><sub>Emmanuel Cordeiro</sub>](https://github.com/ecordeiro) 



> Status do Projeto: Concluido :heavy_check_mark:

### Tópicos 

:small_blue_diamond: [Descrição dos Desafios](#descrição-do-projeto-star)

:small_blue_diamond: [Pré-requesitos](#pré-requesitos)

:small_blue_diamond: [Como rodar a aplicação](#como-rodar-a-aplicação-arrow_forward)

:small_blue_diamond: [Arquivos](#files)

## Descrição dos Desafios :star:

<p align="justify">
Desafio 1

O gerenciamento do relacionamento com os clientes tem como um dos seus objetivos
centrais aumentar o número de clientes ativos da empresa - e a retenção desses clientes é crítica
para seu sucesso. Sendo assim, um time foi mobilizado para garantir o desenvolvimento da
estratégia de retenção de clientes e, sabendo do seu potencial analítico, você foi convocado para
esse desafio.

Em busca de uma maior compreensão das particularidades do negócio e de melhor
entendimento do cenário do churn, vocês optaram por realizar uma análise exploratória dos
dados. Em um primeiro momento algumas hipóteses foram levantadas visando direcionar esse
desenvolvimento inicial e, considerando a base de dados disponibilizada e um período de churn
de 1 ano, foi requisitado a você a validação da seguinte hipótese:

“O churn de novos clientes é maior do que o churn de clientes ativos”

Desafio 2
Antes de apresentar as análises para a liderança, você decide se reunir com seu colega 
de trabalho para discutirem os resultados e se estruturarem para a apresentação. No entanto, 
para isso, é preciso identificar um horário na agenda que seja factível para ambos.
Dadas as agendas de duas pessoas e seus respectivos horários de trabalho, escreva 
um algoritmo que retorna todos os horários nos quais ambas as pessoas estariam disponíveis 
para uma reunião de t minutos. 

As agendas serão compostas por uma lista de n compromissos previamente marcados. 
Esses compromissos, por sua vez, serão representados por uma lista ou tuple de duas strings, 
no qual o primeiro elemento representa o horário de início do compromisso e o último elemento 
o horário de término. A jornada de trabalho terá o mesmo formato de um compromisso, no qual 
o primeiro elemento representa o horário de início do turno e o último elemento o horário final da 
jornada. O tempo da reunião, em minutos, será um inteiro. Por fim, espera-se que o resultado 
esteja no mesmo formato das agendas, nos quais os “compromissos”, nesse caso, 
correspondem aos horários disponíveis para a reunião.

</p>

## Pré-requesitos

:warning: [pendulum](https://pendulum.eustace.io/docs/#installation)

:warning: [Anaconda](https://repo.anaconda.com/archive/Anaconda3-2021.05-Windows-x86_64.exe) 

:warning: [pandas](https://pandas.pydata.org/docs/getting_started/install.html)

:warning: [numpy](https://numpy.org/install/)

:warning: [matplotlib](https://matplotlib.org/1.4.3/faq/installing_faq.html)

:warning: [seaborn](https://seaborn.pydata.org/installing.html)

## Files

[Aqui](https://github.com/React-Bootcamp-WoMarkersCode/certificate-generator/blob/DianaRegina/README_PAGES.md) é possível visualizar a **proposta** de layout do projeto.  

## CRUD

### Usuários

:heavy_check_mark: O usuário pode ser **criado** na pagina Sign-up a partir de um formulário ou com uma conta existente no Google.

:heavy_check_mark: Os dados do usuário podem ser **acessados** em Login e perfil. 

:heavy_check_mark: Os dados do usuário podem ser **atualizados** em seu perfil a partir de um formulário.

:heavy_check_mark: A conta do usuário pode ser **deletada** em seu perfil.

### Eventos

:heavy_check_mark: Podem ser **criados** a partir de um formulário na lista de eventos.

:heavy_check_mark: Podem ser **acessados** na lista de eventos 

:heavy_check_mark: Podem ser **atualizados**  na lista de eventos a partir de um formulário.

:heavy_check_mark: Podem ser **deletados** na lista de eventos

### Participantes

:heavy_check_mark: Podem ser **criados** a partir de um formulário na lista de participantes.

:heavy_check_mark: Podem ser **acessados** em uma lista na lista de participantes.

:heavy_check_mark: Podem ser **atualizados**, indicando se aquele participante poderá ou não receber um certificado na lista de participantes.

:heavy_check_mark: Podem ser **deletados** na lista de participantes.

## Linguagens, dependencias e libs utilizadas :books:

- [React](https://pt-br.reactjs.org/docs/create-a-new-react-app.html)
- [React PDF](https://react-pdf.org/)
- [React Router](https://reacttraining.com/react-router/web/guides/quick-start)

Framework para layouts prontos:
- [AntDesign](https://ant.design/docs/react/introduce) 

Autenticação com Google
- [Login com Google](https://www.npmjs.com/package/react-google-login)

Para mandar PDF por email
- [jspdf](https://www.npmjs.com/package/jspdf) 

Para inserir HTML no corpo do email
- [html2canvas](https://www.npmjs.com/package/html2canvas)

Para desenvolver a assinatura digital:

- [Reactjs-Popup](https://react-popup.elazizi.com/getting-started/)
- [react-signature-canvas](https://www.npmjs.com/package/react-signature-canvas)

Permite visualizar uma animação enquanto o usuário espera o e-mail ser enviado:
- [React-Spinkit](https://github.com/KyleAMathews/react-spinkit)

## Dependência externa :incoming_envelope:
[Server Mailjet](https://github.com/beebones/server-mailjet) - Back-end feito em **Golang** utiizado para consumir api **mailjet** e enviar os emails com o certificado.
<hr/>
