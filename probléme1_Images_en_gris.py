import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import PIL.ImageOps


class image: #crée une class image
    def __init__(self,P,M):
        self.H=M.shape[0] #H le nombre des plans existe dans M
        self.L=M.shape[1] #L le nombre des lignes
        self.P=P #profondeur
        self.M=M #la matrice
#------------------------------------------- Partie I -------------------------------------------#
def Allouer(H,L,P):
    M=np.int32(np.zeros((H,L))) # Crée un matrice rempli par des zero
    return image(P,M)

def Inverser(I):
    I2=Allouer(I.H,I.L,I.P) #crée une image vide
    I2.M=(I.P-1)-I.M #remplace I2 par l'invers de l'image I
    return I2

def flipH(I):
    I2=Allouer(I.H,I.L,I.P) #crée une image vide de méme large et hauteur de I
    I2.M = np.fliplr(I.M)
    # for c in range(I.L):
    #     I2.M[:,c]=I.M[:,(I.L-1-c)] #iverse les colonnes de la matrices de l'image I
    return I2

def poserV(I1,I2):
    I3=Allouer(I2.H+I1.H, I1.L, I1.P) #image vide 
    if (I1.L != I2.L or I1.P != I2.P): return I3 #en cas d'erreur la faction sera retourné I3 vide
    I3.M = np.append(I1.M,I2.M, axis=0)
    return I3

def poserH(I1,I2):
    I3=Allouer(I1.H, I1.L+I2.L, I1.P) #image vide 
    if (I1.H != I2.H or I1.P != I2.P): return I3 #en cas d'erreur la faction sera retourné I3 vide
    I3.M = np.append(I1.M,I2.M, axis=1) 
    return I3

#------------------------------------------- Partie II -------------------------------------------#
def transferer(I,P2,T):
    I2=Allouer(I.H,I.L,P2) #crée une nouvel image de même hauteur et largeur de I et de profondeur P2
    for l in range(I.H):
        for c in range(I.L):
            m=I.M[l,c]
            m[3]=243 # j'ai changer chaque m[3]==255 cas par 243 car il m'adonnée cet erreur
            #           <IndexError: index 255 is out of bounds for axis 0 with size 244>
            I2.M[l,c]=T[m]
    return I2

def inverse2(I):
    P=I.P
    T = [0]*P+1
    for i in range(len(T)):
        T[i] = len(T) - i # remplir le tableau par des valeur de 0 jusqu à len(T) décroissante
    return transferer(I,P,T)



#**************************************T E S T *******************************************#

IMAGE=Image.open("D:\master\S1 génie logiciel pour cloud\Python\Les TPs\TP5\image.png")
tab=np.array(IMAGE)
I = image(255,tab)

# img = Inverser(I)
# img = flipH(I)
# img2 = poserH(I,img)
# img2 = poserV(I,img)
# img2 = poserH(I,img)
t = np.random.randint(255, size=(I.H, I.L))
# img = transferer(I,255,t)

plt.imshow(I.M)
# plt.imshow(img.M)
plt.show()
