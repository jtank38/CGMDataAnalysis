import pandas as pd
import numpy as np
import os
import re



class GetDirs():


    def getDirs(self,root):
        fileList = []
        for subdir, dirs, files in os.walk(root):
            for file in files:
                filepath = subdir + os.sep + file
                if filepath.endswith(".csv"):
                    fileList.append(root + '/' + file)

        return fileList

    def zipFiles(self,L1,L2):

        L1.sort(key=lambda f: int(re.sub('\D', '', f)))
        L2.sort(key=lambda f: int(re.sub('\D', '', f)))
        return [i for i in zip(L1,L2)]

    def getPreprocessedFiles(self,LunchFilename, DateNumFilename):
        # fetch file and correct them, reverse the dataframe

        df = pd.read_csv(LunchFilename)
        df2 = pd.read_csv(DateNumFilename)

        dfvals, dfdatenums=self.missingValues(df, df2)  # [df.columns[::-1]]) to reverse columns
        if dfvals.shape[1]<42:
            z = np.zeros((dfvals.shape[0], 42 - dfvals.shape[1]))
            y = np.zeros((dfdatenums.shape[0], 42 - dfdatenums.shape[1]))
            return np.concatenate([np.append(dfvals, z, axis=1)]), np.concatenate([np.append(dfdatenums, y, axis=1)])

        return dfvals,dfdatenums

    def missingValues(self,dfL, dfN):
        # Interpolate to remove nan values

        df_series_list = dfL.values.tolist()
        correctedDF = self.missingValuesHelper(dfL, df_series_list)
        indexes = correctedDF[correctedDF[correctedDF.columns[0]].isnull()].index.tolist()
        if len(indexes) >= 1:  # remove nans from both series
            for i in indexes:
                correctedDF = correctedDF.drop(i)
                dfN = dfN.drop(i)

        dfN_series_list = dfN.values.tolist()
        dfDateNum = self.missingValuesHelper(dfN, dfN_series_list)

        return np.array(correctedDF), np.array(dfDateNum)

    def missingValuesHelper(self,df, dfSeries):
        interpolated_data = []
        for series in dfSeries:
            cleaned_data = pd.Series(series).interpolate(method='linear', limit_direction='forward').to_list()
            interpolated_data.append(cleaned_data)

        return pd.DataFrame(interpolated_data, columns=df.columns)

    def returnArrays(self,x,y,types=None):
        Lunchpat, TimeSeries = self.getPreprocessedFiles(x, y)
        if types=='Lunch':
            return Lunchpat
        else:
            return TimeSeries

if __name__=='__main__':
    a=GetDirs()
    f1 = a.getDirs('DataFolder/CGMSeriesLunch')
    f2 = a.getDirs('DataFolder/CGMTimeSeries')
    zippedTups=a.zipFiles(f1,f2)
    allArrays=np.array([])
    allArraysdateNum = np.array([])
    allArrays = np.concatenate([a.returnArrays(i[0],i[1],'Lunch') for i in zippedTups])
    allArraysdateNum= np.concatenate([a.returnArrays(i[0],i[1]) for i in zippedTups])

    print(allArraysdateNum.shape)