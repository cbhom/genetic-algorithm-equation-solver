#Genetic Algorithm to solve a math equation
#Test equation is: x**4 + y*20 = 75
#Generation Limit: 1000
#Bias: (-75)
#Mutation: 2%

import random

solutions=[]
generation=[]

def get_fitness(x,y):
  ans = x**4 + y*20 - 75
  if ans==0:
    return 9999
  else:
    return 1/abs(ans)

def getSolution():
  for i in range(1000):
    x = random.uniform(-1000,1000)
    y = random.uniform(-1000,1000)
    solutions.append((get_fitness(x,y),x,y))
    solutions.sort()
    solutions.reverse()

def gen():
  generation = solutions[0:10]
  solutions.clear()
  for i in range(100):
    for j in range(10):
      new_x = generation[j][1] * random.uniform(0.98,1.02)
      new_y = generation[j][2] * random.uniform(0.98,1.02)
      solutions.append((get_fitness(new_x,new_y),new_x,new_y))

  solutions.sort()
  solutions.reverse()


getSolution()
for i in range(1000):
  gen()
  print(f"Generation: {i}\n{solutions[:10]}\n")
  if solutions[0][0] > 1000:
    print("Math equation : x**4 + y*20 = 75\nMutation Rate: 2%\n")
    print(f"\n--- Best Solution ---")
    print(f"Fitness Score: {solutions[0][0]}")
    print(f"x : {solutions[0][1]}\ny : {solutions[0][2]}")
    print(f"Total Generations: {i}")
    break
