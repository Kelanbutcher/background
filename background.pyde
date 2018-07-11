def setup():
    size(700,600)
    noStroke()
    r=random(0,0)
    x=0
   
    while x < 800:
        y=0
        while y< 600:
            if x % 200==0:
              
               fill(210,141,13)
               
            else:
                fill(r,r,r)
            ellipse(x,y,100,100)
            if y % 300==0:
                 fill(128,128,128)
                 
            y = y+70
        x = x +2
        fill(210,141,13)
    ellipse(80,275,100,100)
    ellipse(250,275,100,100)
    ellipse(450,275,100,100)
    ellipse(630,275,100,100)
    
    
    
          
     
               
        
    
