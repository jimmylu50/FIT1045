jess = (["php", "java"], 200)
clark = (["php", "c++", "go"], 1000)
john = (["lua"], 500)
cindy = (["php", "go", "word"], 240)
candidates = [jess, clark, john, cindy]
project = ["php", "java", "c++", "lua", "go"]

def cost(candidates):
    price = 0
    for i in range(len(candidates)):
        price += candidates[i][1] #adding up all the price (of index 1)
    return(price)

def skills(candidates):
    skill = []
    for i in range(len(candidates)):
        for j in range(len(candidates[i][0])):
            skill.append(candidates[i][0][j]) #adding the skills to the list 'skill'
            for k in range(len(skill)-1): 
                if skill[-1] == skill[k]:
                    skill.pop(-1) #pop the last element of the list if they iterate so the list doesn't repeat itself
                    break
    return(skill)
    
def uncovered(project, skills):
    uncovered_project = []
    for i in range(len(project)):
        for j in range(len(skills)):
            if project[i] == skills[j]:
                break #break if they repeat the ones from project, so go on to next possible uncovered skill
            else:
                if j == len(skills)-1:
                    uncovered_project.append(project[i])
                    #if the skill in skills doesn't equal to any of the project skills and it is the last skill in skills, it becomes an uncovered skill
                    break
    return(uncovered_project)

def covered(project, skills):
    covered_project = []
    for i in range(len(skills)):
        for j in range(len(project)):
            if skills[i] == project[j]:
                covered_project.append(project[j])
                #if the one of the skills for candidates matches the ones in project, it is placed in the covered list
                break
    return(covered_project)

def best_individual_candidate(project, candidates):
    list_rate = []
    index = 0
    for i in range(len(candidates)):
        number_of_codes = len(covered(project, skills([candidates[i]])))
        rate = number_of_codes/candidates[i][1]
        list_rate.append(rate)
        #here we use the covered skills of candidates to calculate the worthiness of individual
        if i >= 1:
            if list_rate[i] > list_rate[index]:
                index = i
                #original index is 0, but if new i has greater rate, it becomes new index
    return(index)

def secondElement(list1):
    return list1[1]
    #used for the second element in function below

def team_of_best_individuals(project, candidates):
    team = []
    people = candidates
    first = best_individual_candidate(project, candidates)
    team.append(candidates[first])
    people.pop(first)
    #we first append the best individual to the team, then record the candidates in 'people'
    for i in range(len(candidates)-1):
        index = best_individual_candidate(uncovered(project, skills(team)), people)
        team.append(candidates[index])
        people.pop(index)
        #find the next best individual that covers the uncovered skills
    people.sort(key = secondElement)
    #this allows us to sort the rest of the people list with the minimum wage at index 0 and max wage at -1
    for i in range(len(people)):
        team.append(people[i])
        #then we simply append them to the team
    return(team)

def lex_suc(bitlst, upper_bounds):
    res = bitlst[:]
    n = int(len(bitlst)-1)
    while res[n] != upper_bounds[n]+1:
        res[n] += 1
        for i in range(n+1):
            if res[n] == upper_bounds[n]+1:
                res[n] = 0
                n -= 1
                res[n] += 1
            else:
                return(res)
            
def bounded_lists(upper_bounds):
    first = len(upper_bounds)*[0]
    last = []
    res = [first]
    i = 0
    while i < len(upper_bounds):
        last.append(upper_bounds[i])
        i += 1
    while res[-1] != last:
        res += [lex_suc(res[-1], upper_bounds)]
    return(res)
#the two functions above are for the lex successor is used from the lecture slides
#this is used for the optimal solution foor best_team function

def best_team(project, candidates):
    team = []
    final_team = []
    cost_price = 0
    list_of_candidates = []
    for i in range(len(candidates)):
        list_of_candidates.append(int(1))
    for_count = bounded_lists(list_of_candidates)
    #we creating all the possible outcomes by bruteforcing
    #this allows us to create as many lex suc as we want depending on the number of candidates
    #then they act as binary numbers, with 1 representing the candidate exists in team and 0 representing they are not
    for i in range(len(for_count)):
        for j in range(len(for_count[i])):
            if for_count[i][j] == 1:
                team.append(candidates[j])
                #we loop over to see the different possible solutions
                #if == 1, the team appends a candidate at its position
        if uncovered(project, skills(team)) == []:
            #if all the skills are covered
            if team != []:
                #so that the team is not empty
                if cost_price == 0:
                    cost_price = cost(team)
                    final_team.clear()
                    for k in range(len(team)):
                        final_team.append(team[k])
                    team.clear()
                    #this is for the first instance where cost price is set to 0
                    #this also clears the list of team so new team can be tried for possible solution 
                    #this is done so the below can measure if cost price is greater than the cost or not
                else:
                    if cost_price > cost(team):
                        cost_price = cost(team)
                        final_team.clear()
                        for k in range(len(team)):
                            final_team.append(team[k])
                        team.clear()
                        #here it allows to see whether if the cost of new team
                        #is lower than the cost price held by the previous possible
                        #solution, this gives us the possible lowest cost and at
                        #the same time able to cover all the skills required
        else:
            team.clear()
            i += 1
    return(cost_price, final_team)
