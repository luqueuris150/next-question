import time
from playsound import playsound
  
# define the countdown func.
def countdown(t):
    
    while t:
        mins, segs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, segs)
        #print(timer, end="\r \n") #<- tire o comentário se quiser ver a contagem
        time.sleep(1)
        t -= 1
      
    print('Próxima Questão!!')
    playsound('bell.wav')
  
  
# tempo em segundos
t = 360
counter = 0
while counter < 40:
    countdown(int(t))
    counter = counter + 1
