from getFeatures import getFeatures
from getFeatures import getPCA
from getData import GetDirs
from getFeatures import plotDiag
import numpy as np

np.set_printoptions(suppress=True)


def main():
    # --------------------------------------Get Preprocessed Data------------------------------------------------------
    a = GetDirs()
    f1 = a.getDirs('DataFolder/CGMSeriesLunch')
    f2 = a.getDirs('DataFolder/CGMTimeSeries')
    zippedTups = a.zipFiles(f1, f2)
    allArraysLunch = np.array([])
    allArraysdateNum = np.array([])
    allArraysLunch = np.concatenate([a.returnArrays(i[0], i[1], 'Lunch') for i in zippedTups])
    allArraysdateNum = np.concatenate([a.returnArrays(i[0], i[1]) for i in zippedTups])

    # ------------------------------------------Get Features-----------------------------------------------------------

    getF = getFeatures(allArraysLunch)
    F1 = getF.fft()
    F2 = getF.entropy()
    F3 = getF.skewness()
    F4 = getF.movingStd()

    # ----------------------------------------------Get PCA------------------------------------------------------------

    PCs = getPCA(np.concatenate((F1, F2[:, None], F3[:, None], F4), axis=1)).pca()

    # -----------------------------Get PCA Results in decreasing order of accuracy--------------------------------------
    # print(getPCA(np.concatenate((F1, F2[:, None], F3[:, None], F4), axis=1)).results())

    # --------------------------------------------Plot PCA--------------------------------------------------------------
    plotDiag("Principal Conponent Analysis", 'Red', PCs['PC1'], 'CGM Data', 'PCA Values', 'PC1').plot()
    # plotDiag("Principal Conponent Analysis",'Red',PCs['PC2'],'CGM Data','PCA Values','PC2').plot()
    # plotDiag("Principal Conponent Analysis",'Red',PCs['PC3'],'CGM Data','PCA Values','PC3').plot()
    # plotDiag("Principal Conponent Analysis",'Red',PCs['PC4'],'CGM Data','PCA Values','PC4').plot()
    # plotDiag("Principal Conponent Analysis",'Red',PCs['PC5'],'CGM Data','PCA Values','PC5').plot()

    # ---------------------------------------------PlotEntropy----------------------------------------------------------
    # plotDiag("Feature: Entropy",'Red',F2,'CGM Data','Entropy','Entropy').plot()

    # --------------------------------------------Plot Skewness--------------------------------------------------------
    # plotDiag("Feature: Skewness",'Red',F3,'CGM Data','Skewness','Skewness').plot()

    # ----------------------------------------------Plot FFT-----------------------------------------------------------

    # plotDiag("Feature: FFT", 'Red', F1[:, 0], 'CGM Data', 'FFT-Coefficients', 'FFT').plot()
    # plotDiag("Feature: FFT", 'Red', F1[:, 1], 'CGM Data', 'FFT-Coefficients', 'FFT').plot()
    # plotDiag("Feature: FFT", 'Red', F1[:, 2], 'CGM Data', 'FFT-Coefficients', 'FFT').plot()
    # plotDiag("Feature: FFT", 'Red', F1[:, 3], 'CGM Data', 'FFT-Coefficients', 'FFT').plot()
    # plotDiag("Feature: FFT", 'Red', F1[:, 4], 'CGM Data', 'FFT-Coefficients', 'FFT').plot()

    # -------------------------------------------Plot Moving Std-------------------------------------------------------
    #
    # plotDiag("Feature: Standard Deviation", 'Red', F4[31], 'CGM Data', 'STD Values', 'STD').plot()
    # plotDiag("Feature: Standard Deviation", 'Red', F4[32], 'CGM Data', 'STD Values', 'STD').plot()
    # plotDiag("Feature: Standard Deviation", 'Red', F4[33], 'CGM Data', 'STD Values', 'STD').plot()
    # plotDiag("Feature: Standard Deviation", 'Red', F4[34], 'CGM Data', 'STD Values', 'STD').plot()
    # plotDiag("Feature: Standard Deviation", 'Red', F4[35], 'CGM Data', 'STD Values', 'STD').plot()
    # plotDiag("Feature: Standard Deviation", 'Red', F4[36], 'CGM Data', 'STD Values', 'STD').plot()
    # plotDiag("Feature: Standard Deviation", 'Red', F4[37], 'CGM Data', 'STD Values', 'STD').plot()
    # plotDiag("Feature: Standard Deviation", 'Red', F4[38], 'CGM Data', 'STD Values', 'STD').plot()
    # plotDiag("Feature: Standard Deviation", 'Red', F4[39], 'CGM Data', 'STD Values', 'STD').plot()
    # plotDiag("Feature: Standard Deviation", 'Red', F4[40], 'CGM Data', 'STD Values', 'STD').plot()
    # plotDiag("Feature: Standard Deviation", 'Red', F4[41], 'CGM Data', 'STD Values', 'STD').plot()


main()
