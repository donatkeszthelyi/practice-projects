import numpy as np

def calculate(list0):
    if len(list0) != 9:
        raise ValueError("List must contain nine numbers.")

    try:    
        ar = np.array(list0).reshape((3, 3))
        
        dic = {'mean':[],
               'variance':[],
               'standard deviation':[],
               'max':[],
               'min':[],
               'sum':[]}
        
        mean1ar = np.mean(ar, axis=0)
        mean1 = mean1ar.tolist()
        mean2ar = np.mean(ar, axis=1)
        mean2 = mean2ar.tolist()
        meanF = np.mean(list0)
        dic['mean'] = [mean1, mean2, meanF]
        
        var1ar = np.var(ar, axis=0)
        var1 = var1ar.tolist()
        var2ar = np.var(ar, axis=1)
        var2 = var2ar.tolist()
        varF = np.var(list0)
        dic['variance'] = [var1, var2, varF]
        
        std1ar = np.std(ar, axis=0)
        std1 = std1ar.tolist()
        std2ar = np.std(ar, axis=1)
        std2 = std2ar.tolist()
        stdF = np.std(list0)
        dic['standard deviation'] = [std1, std2, stdF]
        
        max1ar = np.max(ar, axis=0)
        max1 = max1ar.tolist()
        max2ar = np.max(ar, axis=1)
        max2 = max2ar.tolist()
        maxF = np.max(list0)
        dic['max'] = [max1, max2, maxF]
        
        min1ar = np.min(ar, axis=0)
        min1 = min1ar.tolist()
        min2ar = np.min(ar, axis=1)
        min2 = min2ar.tolist()
        minF = np.min(list0)
        dic['min'] = [min1, min2, minF]
        
        sum1ar = np.sum(ar, axis=0)
        sum1 = sum1ar.tolist()
        sum2ar = np.sum(ar, axis=1)
        sum2 = sum2ar.tolist()
        sumF = np.sum(list0)
        dic['sum'] = [sum1, sum2, sumF]
        
        return dic
    
    except ValueError:
        raise ValueError("List must contain nine numbers.")