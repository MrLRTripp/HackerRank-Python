def second_lowest(name_score_list):
    # Verify list is generated as expected
    # for i,elem in enumerate(std_score_list):
    #    print (f'{i= }  {elem= }')
    # Sort list by second element
    sorted_scores_list=sorted(name_score_list,key=lambda x: x[1], reverse=True)
    sorted_names_list=sorted(name_score_list,key=lambda x: x[0])
    second_highest = sorted_scores_list[1][1]
    # Print names in alphabetical order that have second highest
    print('Students with second highest scores:')
    for e in sorted_names_list:
        if e[1] == second_highest:
            print (e[0])
    # A not so obvious way is to do the print in a list comprehension.
    # Although it works, I think it is not a "pythonic" way of using a list comprehension
    # since you are not using the list that is generated and only using it for the side effect
    # of printing.
    # [print(e[0]) for e in sorted_names_list if e[1] == second_highest]


if __name__ == '__main__':
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append([name, score])
    second_lowest(score_list)