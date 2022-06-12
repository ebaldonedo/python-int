def run():
    my_list= [1,"Hello",True]
    my_dict= {"firstname": "Noyer", "lastname":"X"}

    super_list=[
        {"firstname": "Noyer", "lastname":"X"},
        {"firstname": "Juan", "lastname":"bal"},
        {"firstname": "Blank", "lastname":"Xy"},
        {"firstname": "Kakamon", "lastname":"Ultra"}
        
    ]

    super_dict={
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1,4,5,6.43]
    }


    for key, value in super_dict.items():
        print(key, "-", value)
        


if __name__ == '__main__':
    run()


