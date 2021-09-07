<p align="center">
  <img src="https://blog.aevo.com.br/wp-content/uploads/2018/08/Blog-1024x684.png">
</p>

# Dasafio

## Desenvolvedor :🤓

| [<img src="https://avatars.githubusercontent.com/u/7117011?s=96&v=4" width=115><br><sub>Emmanuel Cordeiro</sub>](https://github.com/ecordeiro) 

> Status do Projeto: Concluido :heavy_check_mark:

### Tópicos 

:small_blue_diamond: [Descrição dos Desafios](#descrição-do-projeto-star)

:small_blue_diamond: [Pré-requesitos](#pré-requesitos)

:small_blue_diamond: [Arquivo](#Arquivo)

:small_blue_diamond: [Execução](#Execução)

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

## Arquivo

Visualize [aqui](https://github.com/ecordeiro/Localiza/blob/master/base_dados/base_teste.csv) o **arquivo** com os dados utilizados no desafio 1.  

## Execução

Clique <a href="https://colab.research.google.com/drive/1oXKMrNhxt8D1dM_TkUT42S4kbzzYqyv7" target="_blank">aqui</a> para executar o Desafio 1, disponibilizei o mesmo notebook no google colab.



<p align="justify">
O Desafio 2, precisa ser execuado através de prompt de comando. Para a construção do algorítimo inicialmente eu criei quatro casos de teste e os parametros foram inseridos diretamente no *main*. Utilizei o desenvolviemento dirigido a teste para garantir um bom resultado e uma refatoração adequada.
  
**OBS:** Importante instalar a biblioteca pendulum antes da execução do algorítimo.
</p>
  
![image](https://user-images.githubusercontent.com/7117011/132363679-7c6ac3eb-4b1e-412e-ac40-8739655f2d55.png)
