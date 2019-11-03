#!/usr/bin/env python
# coding: utf-8

from bokeh.models import Button
from bokeh.plotting import figure, curdoc
from bokeh.layouts import gridplot
import numpy as np
from bokeh.layouts import widgetbox
from bokeh.models import CustomJS, TextInput, Paragraph

#plots = [figure(title = 'Styles Demo {i}'.format(i = i + 1), plot_width = 200, plot_height = 200, tools = '') for i in range(9)]
#[plot.line(np.arange(10), np.random.random(10)) for plot in plots]

# CALLBACKS
def callback_print(text_banner=text_banner):
    user_input = str(cb_obj.value)
    welcome_message = 'You have selected: ' + user_input
    text_banner.text = welcome_message

# USER INTERACTIONS
text_input = TextInput(value="", title="Enter row number:",             
callback=CustomJS.from_py_func(callback_print))

button_bokeh = Button(label = "Submit your complain", css_classes = ['custom_button_bokeh'])
curdoc().add_root(text_input)
curdoc().add_root(button_bokeh)