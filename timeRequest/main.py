import funcoes
from prompt_toolkit import prompt
from prompt_toolkit.completion import word_completer

lst = funcoes.timezone_lst()
timezone_options = word_completer.WordCompleter(lst, ignore_case=True, match_middle=True)

funcoes.limpa_tela()


timezone = prompt('Insira o Timezone: ', completer=timezone_options, validator=funcoes.TimezoneValidator(),
                  validate_while_typing=False)

print("="*30)
print(timezone)

print('Data => '+funcoes.hora(timezone).strftime('%d/%m/%Y'))
print('Hora => '+funcoes.hora(timezone).strftime('%H:%M'))

print("="*30)

