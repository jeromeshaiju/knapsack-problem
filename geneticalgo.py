#gemnome is a list of items bringing in a backpack 
#each item is a list of 3 val[name,weight,val] with appropriate val and weight values
#partial is a template to create a obj


from functools import partial
import random

## information about the porogram
print("This program is a genetic algorithm implementation for the knapsack problem. The goal is to maximize the value of items packed in a backpack without exceeding a weight limit.")



items=[
    ["computer", 20, 500],
    ["laptop", 15, 400],
    ["tablet", 8, 250],
    ["phone", 5, 300],
    ["camera", 6, 280],
    ["headphones", 2, 150],
    ["mug", 1, 20],
    ["book", 1, 50],
    ["pen", 1, 5],
    ["notebook", 2, 80],
    ["microphone", 3, 250],
    ["airpods", 1, 200],
    ["joystick", 2, 120],
    ["sock", 1, 2],
    ["mouse", 1, 60],
    ["keyboard", 3, 150],
    ["monitor", 25, 600],
    ["speaker", 4, 220],
    ["webcam", 1, 180],
    ["router", 5, 280]
]
#limit of weight of bags
limit=40


def fitness_function(genome,wightlim,items)->int:
    sum_of_wieght=0
    sum_val=0
    for i in range(len(genome)):
        if genome[i]==1:
            sum_of_wieght += items[i][1]
            sum_val += items[i][2]
            if sum_of_wieght>wightlim:
                return 0
    return sum_val

#partial function to create a new function with fixed weight limit and items list
partial_fitness_function=partial(fitness_function,wightlim=limit,items=items)


def selection_function(population,fitness_function)-> list[list[int]]:
    return random.choices(
        population=population,
        weights=[partial_fitness_function(genome) for genome in population],
        k=2
    )

def crossfunction(selectedgenomes)->tuple[list[int]]:
    #we assume both items in selected genome is same length
    cutpoint=random.randrange(len(selectedgenomes[0]))
    child1 = selectedgenomes[0][:cutpoint] + selectedgenomes[1][cutpoint:]
    child2 = selectedgenomes[1][:cutpoint] + selectedgenomes[0][cutpoint:]
    return child1,child2

#usr defined probability
def mutation(genome,probability)->list[int]:
    randompoint=random.randrange(len(genome))
    if random.random()<probability:
        if genome[randompoint]==0:
            genome[randompoint]=1
        else:
            genome[randompoint]=0
    return genome

#population_size defined by user
def populate(population_size,genome_length)->list[list[int]]:
    population=[]
    while len(population)<population_size:
        genome=creategenome(genome_length)
        population.append(genome)
    return population

def creategenome(genome_length)->list[int]:
    return random.choices([0,1],k=genome_length)

# fittness_limit is user defined
# here we assume by only taking topmost value in reality the optimal value could also be in topmost indices other than 0th val  
def elitism(population,fittness_limit):
    sorted_population=sorted(population,key=lambda genome: partial_fitness_function(genome),reverse=True)
    top_two=[sorted_population[0],sorted_population[1]]
    print(sorted_population[0],top_two)
    if partial_fitness_function(sorted_population[0])>fittness_limit:
        return sorted_population[0],top_two
    print([],top_two)
    return [],top_two



def run(generational_limit,fittness_limit,probability,population_size):
        population=populate(population_size,genome_length=len(items))
        gencount=0
        
        while generational_limit>gencount:
            elites=elitism(population,fittness_limit)
            if elites[0] != []:
                print("you should pack")
                for index in range(len(elites[0])):
                    if elites[0][index]==1:
                        print(items[index][0],items[index][2])
                print(elites[0],"has gotten the value in",gencount,"generation for fittest value")
                print("the fittest value recieved is :",partial_fitness_function(elites[0]))
                break
            newpopulation=[]
            for n in range((population_size//2)-2):
                parents=selection_function(population,fitness_function)
                newpopulation.extend(crossfunction(parents))
            newpopulation.extend(elites[1])
            temp=[]
            for genome in newpopulation:
                temp.append(mutation(genome,probability))
            population=temp
            gencount+=1

        else:
            print("you should pack")
            elites=elitism(population,fittness_limit)
            for index in range(len(elites[1][0])):
                if elites[1][0][index]==1:
                    print(items[index][0])
            print(elites[1][0]," got the value at generation limit")
            print("the fittest value recieved is :",partial_fitness_function(elites[1][0]))

                
            

# add inputs for these functions and run the algorithm
generational_limit=int(input("enter the generational limit"))
fittness_limit=int(input("enter the fittness limit"))
probability=float(input("enter the mutation probability"))
population_size=int(input("enter the population size"))
run(generational_limit,fittness_limit,probability,population_size)
