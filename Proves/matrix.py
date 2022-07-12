m = {(0, 0): 1,
     (0, 1): 2,
     (0, 2): 3,
     (1, 0): 4,
     (1, 1): 5,
     (1, 2): 6,
     (2, 0): 7,
     (2, 1): 8,
     (2, 2): 9,
     (0, 3): 1000,
     (1, 3): 500,
     (2, 3): 500,
     }    

def zero_if_negative(myValue):
    if myValue<1:
        return 0
    return myValue

def matrix_bombing_plan(myValue):    
    lResult = dict(myValue)
    
    #define greatest k[0] iGreatest0
    #define greatest k[1] iGreatest1
    iGreatestRow = 0
    iGreatestCol = 0
    
    for k in iter(myValue.keys()):
        if iGreatestRow < k[0]:
            iGreatestRow = k[0]
        if iGreatestCol < k[1]:
            iGreatestCol = k[1]
    
    for k in iter(myValue.keys()):
        iRow = k[0]
        iCol = k[1]      
                
        #Rebuilding the dictionary here:
        lTempResult = dict(myValue)
        
        #Left, Right, Up and Down:
        if iRow+1<=iGreatestRow:
            lTempResult[iRow+1,iCol]-=lTempResult[iRow,iCol]
            lTempResult[iRow+1,iCol] = zero_if_negative(lTempResult[iRow+1,iCol])
            
        if iRow-1>=0:
            lTempResult[iRow-1,iCol]-=lTempResult[iRow,iCol]
            lTempResult[iRow-1,iCol] = zero_if_negative(lTempResult[iRow-1,iCol])  
            
        if iCol+1<=iGreatestCol:
            lTempResult[iRow,iCol+1]-=lTempResult[iRow,iCol]
            lTempResult[iRow,iCol+1] = zero_if_negative(lTempResult[iRow,iCol+1])
            
        if iCol-1>=0:
            lTempResult[iRow,iCol-1]-=lTempResult[iRow,iCol]
            lTempResult[iRow,iCol-1] = zero_if_negative(lTempResult[iRow,iCol-1])
        
        #Diagonals:
        if iCol-1>=0 and iRow-1>=0:
            lTempResult[iRow-1,iCol-1]-=lTempResult[iRow,iCol]
            lTempResult[iRow-1,iCol-1] = zero_if_negative(lTempResult[iRow-1,iCol-1])
            
        if iCol+1<=iGreatestCol and iRow-1>=0:
            lTempResult[iRow-1,iCol+1]-=lTempResult[iRow,iCol]
            lTempResult[iRow-1,iCol+1]= zero_if_negative(lTempResult[iRow-1,iCol+1])
                        
        if iCol-1>=0 and iRow+1<=iGreatestRow:
            lTempResult[iRow+1,iCol-1]-=lTempResult[iRow,iCol]
            lTempResult[iRow+1,iCol-1] = zero_if_negative(lTempResult[iRow+1,iCol-1])
            
        if iCol+1<=iGreatestCol and iRow+1<=iGreatestRow:
            lTempResult[iRow+1,iCol+1]-=lTempResult[iRow,iCol]
            lTempResult[iRow+1,iCol+1] = zero_if_negative(lTempResult[iRow+1,iCol+1])
        
        
        lResult[iRow,iCol]=sum(lTempResult.values())
        
    return lResult


print(matrix_bombing_plan(m))