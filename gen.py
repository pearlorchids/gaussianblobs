from sklearn.datasets import make_blobs
from matplotlib import pyplot
from pandas import DataFrame
from numpy import arange

# generate 2d classification dataset
X, y = make_blobs(n_samples=1000000, centers=1, n_features=2,center_box=(0,0.02),cluster_std=0.001)
# scatter plot, dots colored by class value
print(len(X))
print(len(y))
print(X)
fig, ax = pyplot.subplots()
#for key, group in grouped:
pyplot.scatter(X[:,0],X[:,1], color='white',s=0.2)
#pyplot.xlim(0,0.02)
#pyplot.ylim(0,0.02)
pyplot.xlim(0,0.02)
pyplot.ylim(0,0.02)
pyplot.autoscale(False)
#pyplot.axis('off')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.set_facecolor('black')
fig.add_axes(ax)
pyplot.show()

f = open("coords.txt", "a")

#f.write(str(n)+","+str((min(X[:,0])+max(X[:,0]))/2)+","+str((min(X[:,1])+max(X[:,1]))/2))
n=6085

        
for i in arange(0,0.015,0.00025):
    for j in arange(0,0.015, 0.00025):
        x_x = list(map(lambda x:x-i, X[:,0]))
        y_y = list(map(lambda x:x+j, X[:,1]))
        #X, y = make_blobs(n_samples=1000000, centers=1, n_features=2,center_box=(0,0.02),cluster_std=0.001)
        fig, ax = pyplot.subplots()
        pyplot.scatter(x_x,y_y, color='white',s=0.2)
        #ax.set_position([i,j,2,2], which='both')
        #print(len(x_x))
        #pyplot.axis('off')
        print(i,max(x_x))
        print(j,max(y_y))
        ax.set_facecolor('black')
        pyplot.xlim(0,0.02)
        pyplot.ylim(0,0.02)
        pyplot.autoscale(False)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        #pyplot.autoscale(enable=False, axis='both', tight=None)
        #ax.get_xaxis().set_ticks([])
        #ax.get_yaxis().set_ticks([])
        #print(i,min(x_x))
        #print(j,min(y_y))
        #fig.savefig('1.png',bbox_inches='tight', pad_inches = 0)
        if(((max(x_x)>0.0009))&((min(y_y)<0.019))):
            fig.savefig(str(n)+'.png',bbox_inches='tight', pad_inches = 0)           
            f.write(str(n)+","+str((min(x_x)+max(x_x))/2)+","+str((min(y_y)+max(y_y))/2)+"\n")
            n = n+1
        if((max(x_x)<0.0009)or(min(y_y)>0.019)):
            break
        pyplot.close(fig)
        pyplot.clf()
        pyplot.cla()
        

for i in arange(0,0.015, 0.00025):
    for j in arange(0,0.015, 0.00025):
        x_x = list(map(lambda x:x+i, X[:,0]))
        y_y = list(map(lambda x:x+j, X[:,1]))
        
        #X, y = make_blobs(n_samples=1000000, centers=1, n_features=2,center_box=(0,0.02),cluster_std=0.001)
        fig, ax = pyplot.subplots()
        pyplot.scatter(x_x,y_y, color='white',s=0.2)
        #ax.set_position([i,j,2,2], which='both')
        #print(len(x_x))
        #pyplot.axis('off')
        
        ax.set_facecolor('black')
        pyplot.xlim(0,0.02)
        pyplot.ylim(0,0.02)
        pyplot.autoscale(False)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        #pyplot.autoscale(enable=False, axis='both', tight=None)
        #ax.get_xaxis().set_ticks([])
        #ax.get_yaxis().set_ticks([])
        print(i,min(x_x))
        print(j,min(y_y))
        #fig.savefig('1.png',bbox_inches='tight', pad_inches = 0)
        if(((min(x_x)<0.019))&((min(y_y)<0.019))):
            fig.savefig(str(n)+'.png',bbox_inches='tight', pad_inches = 0)
            f.write(str(n)+","+str((min(x_x)+max(x_x))/2)+","+str((min(y_y)+max(y_y))/2)+"\n")
            n = n+1
        if(((min(x_x)>0.019))&((min(y_y)>0.019))):
            break
        pyplot.close(fig)
        pyplot.clf()
        pyplot.cla()


        
for i in arange(0,0.015, 0.00025):
    for j in arange(0,0.015, 0.00025):
        x_x = list(map(lambda x:x+i, X[:,0]))
        y_y = list(map(lambda x:x-j, X[:,1]))
        #X, y = make_blobs(n_samples=1000000, centers=1, n_features=2,center_box=(0,0.02),cluster_std=0.001)
        fig, ax = pyplot.subplots()
        pyplot.scatter(x_x,y_y, color='white',s=0.2)
        #ax.set_position([i,j,2,2], which='both')
        #print(len(x_x))
        #pyplot.axis('off')
        
        ax.set_facecolor('black')
        pyplot.xlim(0,0.02)
        pyplot.ylim(0,0.02)
        pyplot.autoscale(False)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        #pyplot.autoscale(enable=False, axis='both', tight=None)
        #ax.get_xaxis().set_ticks([])
        #ax.get_yaxis().set_ticks([])
        print(i,min(x_x))
        print(j,max(y_y))
        #fig.savefig('1.png',bbox_inches='tight', pad_inches = 0)
        if(((min(x_x)<0.019))&((max(y_y)>0.0009))):
            fig.savefig(str(n)+'.png',bbox_inches='tight', pad_inches = 0)
            f.write(str(n)+","+str((min(x_x)+max(x_x))/2)+","+str((min(y_y)+max(y_y))/2)+"\n")

            n = n+1
        if((min(x_x)>0.019)or(max(y_y)<0.0009)):
            break
        pyplot.close(fig)
        pyplot.clf()
        pyplot.cla()
for i in arange(0,0.015,0.00025):
    for j in arange(0,0.015,0.00025):
        x_x = list(map(lambda x:x-i, X[:,0]))
        y_y = list(map(lambda x:x-j, X[:,1]))
        #X, y = make_blobs(n_samples=1000000, centers=1, n_features=2,center_box=(0,0.02),cluster_std=0.001)
        fig, ax = pyplot.subplots()
        pyplot.scatter(x_x,y_y, color='white',s=0.2)
        #ax.set_position([i,j,2,2], which='both')
        #print(len(x_x))
        #pyplot.axis('off')
        
        ax.set_facecolor('black')
        pyplot.xlim(0,0.02)
        pyplot.ylim(0,0.02)
        pyplot.autoscale(False)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        #pyplot.autoscale(enable=False, axis='both', tight=None)
        #ax.get_xaxis().set_ticks([])
        #ax.get_yaxis().set_ticks([])
        print(i,max(x_x))
        print(j,min(y_y))
        #fig.savefig('1.png',bbox_inches='tight', pad_inches = 0)
        if(((max(x_x)>0.0009))&((max(y_y)>0.0009))):
            fig.savefig(str(n)+'.png',bbox_inches='tight', pad_inches = 0)
            f.write(str(n)+","+str((min(x_x)+max(x_x))/2)+","+str((min(y_y)+max(y_y))/2)+"\n")

            n = n+1
        if((max(x_x)<0.0009)or(max(y_y)<0.0009)):
            break
        pyplot.close(fig)
        pyplot.clf()
        pyplot.cla()
f.close()       