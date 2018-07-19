import numpy as np
import matplotlib.pyplot as plt


class PhDPlot():
    ''' The purpose of this object is easily build figures suitable for publications.

    Steps:
    1. Create PhD Object: {var} = PhDPlot()
    2. Load new default styles: {var}.update_default_style(Dictionary)
    3. Create Figure: {var}.new_figure(...)
    4. Target desired plot: {var}.target_subplot(...)
    5. Plot data with various functions
    6. Repeat as needed
    7. Show/save plot

    Note:
    - Internal variables and functions are denoted with _ prior to the name/function.
    - It is highly recommended to leave these alone unless you know what you are doing.
    - Variables/Functions without a leading _ are for user use and interaction

    '''

    def __init__(self):
        ''' Initialisation creates object variables to store default styles.
        In all instances, the first step is to create a PhDPlot object with {var} = PhDPlot()

        Once created, default styles can be modified in the following ways:

        1. Direct Modification: {var}.dpi = 500
        2. Update with dictionary: {var}.update_default_style(Dictionary) - See below

        Important Note:
        1. Updates to figure styles must be completed before calling new_figure()
        2. Temporary style changes can be sent during plotting functions without affecting the default values

        '''

        ## Set Default Styles
        # Figure Styles
        self.fig_size = None
        self.dpi = None
        self.label_font = {'family': 'sans-serif',
                           'size': 9}

        self.title_font = {'family': 'sans-serif',
                           'size': 10}

        # Plot Styles
        self.color = None
        self.data_size = None
        self.linestyle = None
        self.tick_length = None

        ''' If adding new default styles the style needs to be added to the following functions:
        1. update_default_style() - Essential
        2. _update_temp_style() - Essential
        3. _reset_temp_style - Essential
        4. Plotting functions - As required.
            i - In function call if user might need to change for 1 off plots
            ii - In _update_temp_style() function which will be at the start of the plotting function
            
        5. new_figure() - As required.
        
        '''
    def update_default_style(self, style_dict):
        # Figure Styles
        fig_width = style_dict.get("fig_width") if style_dict.get("fig_width") is not None else None
        fig_height = style_dict.get("fig_height") if style_dict.get("fig_height") is not None else None
        self.dpi = style_dict.get("dpi") if style_dict.get("dpi") is not None else self.dpi

        self.fig_size = (fig_width, fig_height) if fig_height and fig_width is not None else self.fig_size
        label_font = style_dict.get("label_font") if style_dict.get("label_font") is not None else 'sans-serif'
        label_size = style_dict.get("label_size") if style_dict.get("label_size") is not None else 9
        title_font = style_dict.get("title_font") if style_dict.get("title_font") is not None else 'sans-serif'
        title_size = style_dict.get("title_size") if style_dict.get("title_size") is not None else 10

        self.label_font = {'family': label_font,
                           'size': label_size}

        self.title_font = {'family': title_font,
                           'size': title_size}

        # Plot Styles
        self.color = style_dict.get("color") if style_dict.get("color") is not None else self.color
        self.data_size = style_dict.get("data_size") if style_dict.get("data_size") is not None else self.data_size
        self.linestyle = style_dict.get("linestyle") if style_dict.get("linestyle") is not None else self.linestyle
        self.tick_length = style_dict.get("tick_length") if style_dict.get("tick_length") is not None else self.tick_length

    def new_figure(self, height, width):
        # Create Figure
        self._height = height
        self._width = width

        self.fig, self.axes = plt.subplots(height,
                                           width,
                                           figsize=self.fig_size,
                                           dpi=self.dpi)
        self._set_current_axes([0, 0])

    ## Functions for User:
    def target_subplot(self, co_ords):
        self._set_current_axes(co_ords)

    def plot_data_line(self,
                       y_data,
                       x_data=None,
                       colour=None,
                       linewidth=None,
                       linestyle=None):  # Make sure to add any new styles to both functions
        ''' Typical line plot'''
        self._update_temp_style(colour=colour, data_size=linewidth, linestyle=linestyle)
        self._set_tick()
        # x-data & y-data
        if x_data is not None:
            self._current_axes.plot(x_data, y_data, color=self._colour_temp,
                                    linewidth=self._data_size_temp, linestyle=self._linestyle_temp)
        # Only y-data
        else:
            self._current_axes.plot(y_data, color=self._colour_temp,
                                    linewidth=self._data_size_temp,linestyle=self._linestyle_temp)


    def plot_data_scatter(self,
                          x_data,
                          y_data,
                          size = None,
                          colour = None):
        ''' Typical x-y scatter plot'''
        self._update_temp_style(colour=colour, data_size=size)
        self._set_tick()
        self._current_axes.scatter(x_data, y_data, s=self.data_size, c=self.color)

    def set_x_label(self, xlabel):
        self._current_axes.set_xlabel(xlabel, fontdict=self.label_font)

    def hide_x_labels(self):
        self._current_axes.set_xticklabels([])

    def hide_y_labels(self):
        self._current_axes.set_yticklabels([])

    ## Internal Functions:
    def _set_tick(self):
        self._current_axes.tick_params(length=self.tick_length)

    def _set_current_axes(self, co_ords):
        if co_ords is not None:
            self._current_co_ords = co_ords

        if self._height == 1 and self._width == 1:
            self._current_axes = self.axes
        elif self._height == 1 or self._width == 1:
            self._current_axes = self.axes[self._current_co_ords]
        else:
            self._current_axes = self.axes[self._current_co_ords[0], self._current_co_ords[1]]

    def _update_temp_style(self, colour=None, data_size=None, linestyle=None):
        self._reset_temp_style() # Reset all styles to default

        self._colour_temp = colour if colour is not None else self.color
        self._data_size_temp = data_size if data_size is not None else self.data_size
        self._linestyle_temp = linestyle if linestyle is not None else self.linestyle

    def _reset_temp_style(self):
        self._colour_temp = self.color
        self._data_size_temp = self.data_size
        self._linestyle_temp = self.linestyle

    def show_plot(self):
        plt.show()



def main():
    pass

if __name__ == '__main__':
    main()
