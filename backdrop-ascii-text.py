# The base letters are taken from https://patorjk.com/software/taag/, and the code will work with any representation with letters composed of '#.'
base ="""
   ###     
  ## ##    
 ##   ##   
##     ##  
#########  
##     ##  
##     ## 
*
########   
##     ##  
##     ##  
########   
##     ##  
##     ##  
######## 
*
 ######    
##    ##   
##         
##         
##         
##    ##   
 ###### 
* 
########   
##     ##  
##     ##  
##     ##  
##     ##  
##     ##  
######## 
*
########   
##         
##         
######     
##         
##         
######## 
*
########   
##         
##         
######     
##         
##         
## 
*
 ######    
##    ##   
##         
##   ####  
##    ##   
##    ##   
 ###### 
* 
##     ##  
##     ##  
##     ##  
#########  
##     ##  
##     ##  
##     ## 
*
####       
 ##        
 ##        
 ##        
 ##        
 ##        
#### 
*
      ##   
      ##   
      ##   
      ##   
##    ##   
##    ##   
 ###### 
* 
##    ##   
##   ##    
##  ##     
#####      
##  ##     
##   ##    
##    ## 
*
##         
##         
##         
##         
##         
##         
######## 
*
##     ##  
###   ###  
#### ####  
## ### ##  
##     ##  
##     ##  
##     ## 
*
##    ##   
###   ##   
####  ##   
## ## ##   
##  ####   
##   ###   
##    ## 
*
 #######   
##     ##  
##     ##  
##     ##  
##     ##  
##     ##  
 ####### 
* 
########   
##     ##  
##     ##  
########   
##         
##         
## 
*
 #######   
##     ##  
##     ##  
##     ##  
##  ## ##  
##    ##   
 ##### ## 
* 
########   
##     ##  
##     ##  
########   
##   ##    
##    ##   
##     ## 
*
 ######    
##    ##   
##         
 ######    
      ##   
##    ##   
 ###### 
* 
########   
   ##      
   ##      
   ##      
   ##      
   ##      
   ## 
*   
##     ##  
##     ##  
##     ##  
##     ##  
##     ##  
##     ##  
 ####### 
* 
##     ##  
##     ##  
##     ##  
##     ##  
 ##   ##   
  ## ##    
   ### 
*   
##      ## 
##  ##  ## 
##  ##  ## 
##  ##  ## 
##  ##  ## 
##  ##  ## 
 ###  ### 
* 
##     ##  
 ##   ##   
  ## ##    
   ###     
  ## ##    
 ##   ##
* 
##    ##  
##    ##   
 ##  ##    
  ####     
   ##      
   ##      
   ##      
   ## 
*   
########   
     ##    
    ##     
   ##      
  ##       
 ##        
########   """.split("*")
for i in range(len(base)):
    base[i] = base[i].replace("#", "█")
    temp = ""
    for j in base[i]:
        temp += j
        if temp[-2:] == "█ ":
            temp = temp[:-2]
            temp += "▓▒"
    base[i] = temp
#     print(base[i], "\n_______\n")
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def main():
    inp = [*(input("Enter only letters: ").replace(" ", "").upper())]
    for i in inp:
        print(base[alpha.index(i)], end="\n")
main()
