# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 22:46:17 2018

@author: Siva

Input Array: [10 20 30 40 50 60 70 80 90 100] -> N Elements
K=4
Output Array: [25 35 45 55 65 75 85] -> (N-K+1) Elements

Strategy: 10+20+30+40/4, 20+30+40+50/4......(N-K+1) times
"""
import numpy as np

def GetMovingAverageArray(inputVector,K):
    if(K>len(inputVector)): #Dont proceed if K is greater than the length of the array
        print("Please input k to be less than the length of the input vector")
    else:
        resultArray=np.ones(len(inputVector)-K+1) #Initialize to an arrray of ones with length = (N-K+1)
        currentIndex=0
        for i in inputVector:
            s=i
            for j in inputVector[currentIndex+1:currentIndex+K]:
                s+=j
            resultArray[currentIndex]=s/K
            currentIndex+=1
            if currentIndex==len(resultArray): #if the current index equals the length of the resultArray then break
                break
        return resultArray
    
inputArray=np.array([10,20,30,40,50,60,70,80,90,100])
outputArray=GetMovingAverageArray(inputArray,4)#window is 4
print(outputArray)
print('----------')
inputArray=np.array([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150])
outputArray=GetMovingAverageArray(inputArray,3)#window is 3
print(outputArray)
print('----------')
inputArray=np.array([10, 12, 14, 16])
outputArray=GetMovingAverageArray(inputArray,4)#window is 4
print(outputArray)
print('----------')
inputArray=np.array([10, 12, 14, 16])
outputArray=GetMovingAverageArray(inputArray,5)#window is 4
print(outputArray)
print('----------') 

