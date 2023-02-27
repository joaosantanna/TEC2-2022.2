import PySimpleGUI as sg
from L2Q1 import simular


desenho =[
    [sg.Text('Simulador de lancamento de dados')],
    [sg.Multiline(size=(15,10), key='saida')],
    [sg.Button('Simular'), sg.Button('sair')]
]

janela = sg.Window('Lancamento de dados APP',
                   font='Arial 12',
                   layout= desenho)
while True:
    eventos, valores = janela.read()

    if eventos =='sair'or eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Simular':
        resultado = simular()
        texto =''
        for c, v in resultado.items():
            texto = texto + str(c) +' - ' + str(v/10) + '%' +'\n'

        janela['saida'].update(texto)







