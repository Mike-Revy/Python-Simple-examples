CELLS = [ (0,0), (1,0), (2,0), (3,0), (4,0),
          (0,1), (1,1), (2,1), (3,1), (4,1),
          (0,2), (1,2), (2,2), (3,2), (4,2),
          (0,3), (1,3), (2,3), (3,3), (4,3),
          (0,4), (1,4), (2,4), (3,4), (4,4) ]
          
          

def matrix_build():          
    dimension = int(input("Give matrix dimension (start is at ZERO - so 1 dimension is 00,10,01,11)"))
    matrix = []
    if dimension > 0 :
        x=0
        while x <= dimension:
            y = 0
            while y <= dimension: 
                matrix.append((y,x))
                y +=1
            x +=1
    return matrix, dimension

matrix, dimension = matrix_build()
print(matrix)
input("paused")
x, y = matrix[dimension]
print(x,y)



