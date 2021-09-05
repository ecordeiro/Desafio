"""
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
Exemplo: Considere o seguinte cenário:
1. Agenda da pessoa A: [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
2. Horário de Trabalho da pessoa A: ['9:00', '20:00']
3. Agenda da pessoa B: [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', 
'17:00']]
4. Horário de Trabalho da pessoa B: ['10:00', '18:30']
Os horários que possibilitam uma reunião de 30 minutos entre a pessoa A e pessoa B são:
[['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']
"""

import pendulum

def free_time(fulltime, lista_ocupada):
    """
    Retorna todos os horários livres de um trabalhador.

    Args:
        fulltime (list): Lista com com os valores de hora de início e fim do trabalho
        lista_ocupada (list): Lista com os horários indisponíveis do trabalhador

    Returns:
        list: Lista com sub-listas com a agenda livre do trabalhador
    """
    lista_free = []
    hora_ini = fulltime[0]
    hora_fim = fulltime[1]

    len_list = len(lista_ocupada)
    j = 0

    for i in lista_ocupada:

        diff = date_dif(hora_ini,i[0])

        if diff > 0: lista_free.append([hora_ini, i[0]])

        # Guarda a hora final na hora incial da próxima lista de horas
        hora_ini = i[1]

        j += 1
        if j==len_list: lista_free.append([hora_ini,hora_fim])
    
    return lista_free        
        

def nucleo_time(work_A,work_B):
    """
    Retorna o horário comum entre duas agendas.

    Args:
        work_A(list): Lista com as agendas do trabalhador A
        work_B(list): Lista com as agendas do trabalhador B
    Returns: 
        list: lista com os valores do horário Núcleo entre os dois trabalhadores
    """
    nucleo_work = []

    # Analisa se os períodos são totalmente incompatíveis. Ex: Um inicia depois que outro ja acabou.
    # Para a data inicial de B e a data final de A. Se B ocorrede depois de A, não existe nucleo.
    compat = date_dif(work_B[0],work_A[1])
    if compat <= 0: nucleo_work = [0]

    # Para a data Final de B e a data inicial de A. Se A ocorrede depois de B, não existe nucleo.    
    compat = date_dif(work_A[0],work_B[1])
    if compat < 0: nucleo_work = [0]

    if 0 not in nucleo_work:

        diff_start = date_dif(work_A[0],work_B[0])
        diff_end = date_dif(work_A[1],work_B[1])

        # Se diff_start > 0 então o trabalhador A, inicia primeiro, guardar o horário do B
        # Se diff_start = 0 eles iniciam juntos
        # Se diff_start < 0 então o trabalhador B, inicia primeiro, guardar o horário do A
        nucleo_work.append(work_B[0]) if diff_start > 0 else nucleo_work.append(work_A[0])  
            
        # Se diff_end > 0 então o trabalhador A, Termina primeiro, guardar o horário do A
        # Se diff_end = 0 eles terminam juntos
        # Se diff_end < 0 então o trabalhador B, Termina primeiro, guardar o horário do B
        nucleo_work.append(work_A[1]) if diff_end > 0 else nucleo_work.append(work_B[1])
    
    return nucleo_work

def date_dif(start,end):

    """
    Calcula a diferença entre duas horas.
    Args:
        start(string): Valor string que representa uma determinada hora de início no formato(HH:MM)
        end(string): Valor string que representa uma determinada hora de Fim no formato(HH:MM)
    Returns: 
        (int) Retorna um valor (int) em minutos
    """    
    t1 = pendulum.parse(start)
    t2 = pendulum.parse(end)
    period = t2 - t1

    return period.in_minutes()


def schedule(minutos, schedule_A, schedule_B, work_A, work_B):
    """
    Identifica os horários disponíveis entre duas pessoas considerando a agenda de cada um e
    seus horários de trabalhado. Também leva em consideração o tempo demandado de reunião.

    Args:
        minutos (int): Minutos de duração da reunião
        schedule_A (list): Lista com os horários indisponíveis do trabalhador A
        schedule_B (list): Lista com os horários indisponíveis do trabalhador B
        work_A (list): Horário de trabalho do Trabalhador A
        work_B (list): Horário de trabalho do Trabalhador B

    Returns:
        [list]: Lista com os horários disponíveis entre os dois trabalhadores e de acordo com o tempo
        da reunião
    """

    free_schedule = []

    nucleo_work = nucleo_time(work_A,work_B)

    free_A = free_time(work_A, schedule_A)
    free_B = free_time(work_B, schedule_B)

    free_nucleo_work = [nucleo_time(a,b) for a in free_A for b in free_B if nucleo_time(a,b) != [0]]

    free_schedule = [i for i in free_nucleo_work if date_dif(i[0],i[1])>=minutos]
           
    return free_schedule


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---
def test(f, expected,**kwargs):
    """
    Executa a função f com os parâmetros em **kwargs e compara o resultado com expected.

    Args:
        f(funcao): Função a ser utilizada para testes
        expected: valor esperado para validar o caso de teste

    kwargs:
        minutos (int): Minutos de duração da reunião
        schedule_A (list): Lista com os horários indisponíveis do trabalhador A
        schedule_B (list): Lista com os horários indisponíveis do trabalhador B
        work_A (list): Horário de trabalho do Trabalhador A
        work_B (list): Horário de trabalho do Trabalhador B     

    returns 
        (str):Exibe uma mensagem indicando se a função f está correta ou não.
    """
    minute = kwargs.get('minute')
    sch_a = kwargs.get('schedule_A')
    sch_b = kwargs.get('schedule_B')
    w_a = kwargs.get('work_A')
    w_b = kwargs.get('work_B')    

    out = f(minute,sch_a, sch_b, w_a, w_b)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({minute!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    
    schedule_A = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
    schedule_B = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]

    work_A = ['9:00', '20:00']
    work_B = ['10:00', '18:30']

    # Testes que verificam o resultado do código em alguns cenários.
    test(schedule, minute=30,
            schedule_A=schedule_A, 
            schedule_B=schedule_B, 
            work_A=work_A, 
            work_B=work_B, expected=[['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']])

    test(schedule, minute=25,
            schedule_A=schedule_A, 
            schedule_B=schedule_B, 
            work_A=work_A, 
            work_B=work_B, expected=[['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']])

    test(schedule, minute=60,
            schedule_A=schedule_A, 
            schedule_B=schedule_B, 
            work_A=work_A, 
            work_B=work_B, expected=[['15:00', '16:00']])

    test(schedule, minute=70,
            schedule_A=schedule_A, 
            schedule_B=schedule_B, 
            work_A=work_A, 
            work_B=work_B, expected=[])
    
    
