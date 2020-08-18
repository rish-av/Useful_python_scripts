import matplotlib.pyplot as plt
import numpy as np

#for LaTex font
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.sans-serif": ["Helvetica"]})



def _plot_data(data_listx,data_listy,styles,labels,xlabel,ylabel):
    #define figure size here
    f = plt.figure()
    ax = plt.subplot(111)

    # Hide the right and top spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')

     #you can define the x separation here, here it is 1.0 & set limits
    plt.xticks(np.arange(np.min(data_listx), np.max(data_listx)+1, 1.0))

    for datax,datay,style,label in zip(data_listx,data_listy,styles,labels):
        ax.plot(datax,datay,style,label=label)

    # plt.xlim(0,6)
    # plt.ylim(0,10)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    return f




#for number of rows/columns greater than 1,
#example terminology: matrix[0][0] corresponds to left top image
#all figs are of same size

def _plot_matrix(matrix,title_matrix,figsize=5,big_title="Images"):
    shape = matrix.shape
    h,w = shape[0],shape[1]
    fig,ax = plt.subplots(h,w,figsize=(figsize*h,figsize*w))
    fig.suptitle(big_title)

    for i in range(h):
        for j in range(w):
            # if you want a math operation on matrix[i][j], that can be done here
            ax[i,j].plot(matrix[i][j])
            ax[i,j].title.set_text(title_matrix[i][j])
    return ax

#plots images in a single row or a single column based upon argument plot_align
def _plot_subplots_single_image(images,plot_align='horizontal',title="Images",figsize = None):
    num_images = len(images)
    hori_align = False

    #assuming one image size is 5x5, if something else, change it!
    if plot_align.lower() == 'horizontal':
        fig,ax = plt.subplots(1,num_images)
        if figsize == None:
            fig.set_figheight(5)
            fig.set_figwidth(num_images*5)
        else:
            fig.set_figheight(figsize[0])
            fig.set_figwidth(num_images*figsize[1])
    else:
        fig,ax = plt.subplots(num_images,1)
        if figsize == None:
            fig.set_figheight(num_images*5)
            fig.set_figwidth(5)
        else:
            fig.set_figheight(num_images*figsize[0])
            fig.set_figwidth(figsize[1])

    fig.suptitle(title)
    
    for i in range(num_images):
        ax[i].plot(images[i])
    return ax,fig

def _save_fig(figure):
    plt.savefig(figure)


x = np.random.randn(10)
y = np.array([i for i in range(10)])
data_y = [np.cos(x),np.sin(x),np.tan(x)]
data_x = [y,y,y]
styles = ['g--','r--','b--']
label = ['cos','sin','tan']

f = _plot_data(data_x,data_y,styles,label,"Input","Trigonometric Value")

f.savefig('check.pdf')