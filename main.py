import numpy as np

np.set_printoptions(suppress=True)
from getFeatures import getFeatures
from getFeatures import getPCA
from getData import GetDirs
from getFeatures import plotDiag
import sys


def main():
    a = GetDirs()
    f1 = a.getDirs('DataFolder/CGMSeriesLunch')
    f2 = a.getDirs('DataFolder/CGMTimeSeries')
    zippedTups = a.zipFiles(f1, f2)
    allArraysLunch = np.array([])
    allArraysdateNum = np.array([])
    allArraysLunch = np.concatenate([a.returnArrays(i[0], i[1], 'Lunch') for i in zippedTups])
    allArraysdateNum = np.concatenate([a.returnArrays(i[0], i[1]) for i in zippedTups])
    # print(allArraysLunch.shape,allArraysdateNum.shape)
    getF = getFeatures(allArraysLunch)
    F1 = getF.fft()
    F2 = getF.entropy()
    F3 = getF.skewness()
    F4 = getF.movingStd()
    # print(F1.shape,F2.shape,F3.shape,F4.shape)
    print(getPCA(np.concatenate((F1, F2[:, None], F3[:, None], F4), axis=1)).results())
    sys.exit(1)
    # Plot PCA
    # plt=plotDiag("Principal Conponent Analysis",'Red',PCs['PC1'],'CGM Data','PCA Values','PC1').plot()
    # plt=plotDiag("Principal Conponent Analysis",'Red',PCs['PC2'],'CGM Data','PCA Values','PC2').plot()
    # plt=plotDiag("Principal Conponent Analysis",'Red',PCs['PC3'],'CGM Data','PCA Values','PC3').plot()
    # plt=plotDiag("Principal Conponent Analysis",'Red',PCs['PC4'],'CGM Data','PCA Values','PC4').plot()
    # plt=plotDiag("Principal Conponent Analysis",'Red',PCs['PC5'],'CGM Data','PCA Values','PC5').plot()

    # PlotEntropy
    # plt=plotDiag("Feature: Entropy",'Red',F2,'CGM Data','Entropy','Entropy').plot()

    # Plot Skewness
    # plt=plotDiag("Feature: Skewness",'Red',F3,'CGM Data','Skewness','Skewness').plot()

    # Plot FFT
    # plt=plotDiag("Feature: FFT",'Red',F1[:,2],'CGM Data','FFT-Coefficients','FFT').plot()

    # Plot Moving Std
    plt = plotDiag("Feature: Standard Deviation", 'Red', F4[40], 'CGM Data', 'STD Values', 'STD').plot()


main()

if __name__ == '__main__':
    main()
