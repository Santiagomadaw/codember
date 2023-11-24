colors ={
    'black':'30',
    'red':'31',
    'green':'32',
    'yellow':'33',
    'blue':'34',
    'magenta':'35',
    'cyan':'36',
    'white':'37',
    'reset':'39'
    }
colorsbg ={
    'black':'40',
    'red':'41',
    'green':'42',
    'yellow':'43',
    'blue':'44',
    'magenta':'45',
    'cyan':'46',
    'white':'47',
    'reset':'49'
    }
style ={
    'bold':'1',
    'underline':'4',
    'blink':'5',
    'reverse':'7',
    'reset':'0'
    }
import string
import unicodedata
def rem_punt(frase):
    return filter(lambda x: x not in string.punctuation)
def remove_puntuacion(frase):
    caracteres=string.punctuation
    frase_despuntuada = ""
    i =0
    while i < len(frase):
        if frase[i] not in caracteres:
            frase_despuntuada = frase_despuntuada + frase[i]
        i += 1
    return frase_despuntuada

def eliminar_acentos(cadena):
    forma_nfkd = unicodedata.normalize('NFKD', cadena)
    solo_ascii = forma_nfkd.encode('ASCII', 'ignore')
    return solo_ascii.decode()

def normalize_text(text):
    text = text.lower()  # convertir a minúsculas
    text = text.strip()  # eliminar espacios en blanco al inicio y al final
    return text

def normalizacion(frase):
    normalizada = ""
    normalizada = normalize_text(eliminar_acentos(remove_puntuacion(frase)))
    return normalizada
def clear():
    '''limpia la pantalla'''
    print("\033[2J")
    
def locate(line:int, column:int):
    '''locate(line, column) Coloca el cursor en la posicion deseada'''
    print("\033[{};{}H".format(line, column), end="")
    
def reset():
    '''resetea los estilos'''
    print("\33[{}m".format(colors['reset']), end="")
    print("\33[{}m".format(colorsbg['reset']), end="")
    print("\33[{}m".format(style['reset']), end="")
    
def procesarparametros(params):
    '''funcion auxiliar que procesa los parametros de Printext y Inputtext'''
    if 'linea' in params:
        linea = params ['linea']
        columna = 1
        if 'columna' in params:
            columna = params ['columna']
    locate(linea, columna)
    if 'color' in params and params['color'] in colors:
        print("\33[{}m".format(colors[params['color']]), end="")
    if 'bg' in params and params['bg'] in colorsbg:
        print("\33[{}m".format(colorsbg[params['bg']]), end="")
    if 'style' in params and params['style'] in style:
        print("\33[{}m".format(style[params['style']]), end="")    

def Input(texto, **parametros):
    procesarparametros(parametros)
    return input(texto) 

def Print(texto, **parametros):
    '''parametros: linea, columna, estilo, colortx, color bg, tend'''
    def procesarparametros(params):
        if 'linea' in params:
            linea = params ['linea']
            columna = 1
            if 'columna' in params:
                columna = params ['columna']
        locate(linea, columna)
        if 'color' in params and params['color'] in colors:
            print("\33[{}m".format(colors[params['color']]), end="")
        if 'bg' in params and params['bg'] in colorsbg:
            print("\33[{}m".format(colorsbg[params['bg']]), end="")
        if 'style' in params and params['style'] in style:
            print("\33[{}m".format(style[params['style']]), end="")
        
    procesarparametros(parametros)
    print(texto)
    reset()
    
def transform(elements:list, change_element) ->list :
    '''transform(a:list, b:fuction_aplicada)'''

    new_list = []
    for element in elements:
        new_list.append(change_element(element))
    return new_list

def select(elements: list, predicate)-> list:
    """select(list, funcion_predicado)
    Recibe una lista y un predicado. Devuelve una nueva lista con aquellos elementos
    que superan el test del predicado.
    """
    selected = []
    for element in elements:
        if predicate(element):
            selected.append(element)
    return selected

def compress(elements, initial_value, operation):
    """compress(secuencia, valor inicial, funcion_operacion)
    Recibe una secuencia de elementos, un valor inicial y 
    una función que representa una operación de combinación
    de dos elementos.
    Devuelve un solo valor comprimido
    """
    accum = initial_value
    for element in elements:
        accum = operation(accum, element)
    return accum 