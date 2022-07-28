# связующее звено между двумя модулями model и view

import model_kalk as model
import view
import menu as m

def button_click():
    # m.calkylator()
    а = view.get_value()
    result = model.my_eval(а)


  
