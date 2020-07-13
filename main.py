import pygame

pygame.init()

screen_info=pygame.display.Info()
print(screen_info)
size=(width,hieght)=(screen_info.current_w,screen_info.current_h)
clock=pygame.time.clock
screen=pygame.display.set_mode(size)
color= (0,255,0)
def main():
  clock.tick(60)
  screen.fill
  pygame.display.flip()
if __name__=='__main__':
  main()