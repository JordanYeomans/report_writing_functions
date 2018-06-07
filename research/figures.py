import numpy as np
import matplotlib.pyplot as plt
import string

class SubPlot():

    def __init__(self, height, width, fig_size=(5.9,3.32), dpi = 72, font_fam = 'sans-serif', font_label_size = 9,
                 font_title_size = 9, tick_size = 8, figure_num = 1):

        self.height = height
        self.width = width
        self.figure_num = figure_num
        self.figsize = fig_size
        self.dpi = dpi

        self.label_font = {'family': font_fam,
                           'size': font_label_size}

        self.title_font = {'family': font_fam,
                           'size': font_title_size}

        self.tick_size = tick_size

        # Current State
        self.current_plot = 0
        self.current_letter = 0

        self.fig = plt.figure(self.figure_num, figsize=self.figsize, dpi=self.dpi)

        self.adjust_plot()


    def add_subplot_data(self,
                         x_data,
                         y_data = None,
                         type= 'plot',
                         xlim = None,
                         ylim = None,
                         xlabel = None,
                         ylabel = None,
                         title = None,
                         add_data_to = None,
                         data_size = 1,
                         color = None,
                         linestyle = None,
                         legend_label = None
                         ):

        # Create New Subplot
        if add_data_to is None:

            # Update Plot State
            self.current_plot += 1
            self.current_letter = string.ascii_lowercase[self.current_plot-1]
            try:
                self.fig = plt.subplot(self.height, self.width, self.current_plot)
            except ValueError:
                print('Too many plots for Subplot')
                raise

        elif add_data_to is not None:

            # Add to existing subplot or creating new subplot
            assert add_data_to <= self.current_plot + 1, 'Adding Data to a plot that does not exist'

            try:
                self.fig = plt.subplot(self.height, self.width, add_data_to)

            except ValueError:
                print('Problem with add_data_to - Plot out of range')
                raise

        # Define Type Of Plot And Add Data To Plot
        if type == 'scatter':
            self.fig = plt.scatter(x_data,y_data, s=data_size, color=color, label = legend_label)
        elif type == 'plot':
            if y_data is None:
                self.fig = plt.plot(x_data, color=color, linestyle=linestyle, linewidth=data_size, label = legend_label)
            if y_data is not None:
                self.fig = plt.plot(x_data, y_data, color=color, linestyle=linestyle, linewidth=data_size, label = legend_label)
        else:
            raise Exception

        self.fig = plt.xticks(fontsize=self.tick_size)
        self.fig = plt.yticks(fontsize=self.tick_size)

        # Add Axis Limits
        if xlim is not None:
            self.axes = plt.xlim(xlim)

        if ylim is not None:
            self.axes = plt.ylim(ylim)

        # Add Axis Labels
        if xlabel is not None:
            self.axes = plt.xlabel(xlabel,fontdict=self.label_font)
        if ylabel is not None:
            self.axes = plt.ylabel(ylabel,fontdict=self.label_font)


        # Add Subplot title
        if title is not None:
            self.add_subplot_title(title)

    def adjust_plot(self,left=0.1,bottom=0.13,right=0.99,top=0.92,wspace=0.32,hspace=0.2):
        self.fig = plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)

    def show_plow(self):
        plt.show()

    def save_figure(self, save_name):
        self.fig = plt.savefig(save_name, pad_inches = 0)

    def add_subplot_title(self, title, plot_num = None, letter = None):

        if plot_num is not None:
            self.current_plot = plot_num

        if letter is not None:
            self.current_letter = letter

        if self.current_plot == 0:
            self.current_plot = 1

        self.fig = plt.subplot(self.height, self.width, self.current_plot)
        self.current_letter = string.ascii_lowercase[self.current_plot - 1]
        title = '(' + self.current_letter + ') ' + title
        self.fig = plt.title(title, fontdict=self.title_font)
        self.current_plot += 1

    def add_legend(self, bbox = [0.0, 1.02, 1.0, 0.102], loc = 3, ncol = 5, mode = 'expand'):
        self.fig = plt.legend(bbox_to_anchor=bbox, loc=loc,
           ncol=ncol, mode=mode, borderaxespad=0, frameon=False)