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
        
        mean1 = np.mean(ar, axis=0).tolist()
        mean2 = np.mean(ar, axis=1).tolist()
        meanF = np.mean(list0)
        dic['mean'] = [mean1, mean2, meanF]
        
        var1 = np.var(ar, axis=0).tolist()
        var2 = np.var(ar, axis=1).tolist()
        varF = np.var(list0)
        dic['variance'] = [var1, var2, varF]
        
        std1 = np.std(ar, axis=0).tolist()
        std2 = np.std(ar, axis=1).tolist()
        stdF = np.std(list0)
        dic['standard deviation'] = [std1, std2, stdF]
        
        max1 = np.max(ar, axis=0).tolist()
        max2 = np.max(ar, axis=1).tolist()
        maxF = np.max(list0)
        dic['max'] = [max1, max2, maxF]
        
        min1 = np.min(ar, axis=0).tolist()
        min2 = np.min(ar, axis=1).tolist()
        minF = np.min(list0)
        dic['min'] = [min1, min2, minF]
        
        sum1 = np.sum(ar, axis=0).tolist()
        sum2 = np.sum(ar, axis=1).tolist()
        sumF = np.sum(list0)
        dic['sum'] = [sum1, sum2, sumF]
        
        return dic
    
    except ValueError:
        raise ValueError("List must contain nine numbers.")
