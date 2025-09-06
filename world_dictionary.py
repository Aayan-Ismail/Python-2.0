world_dictionary = {

}
while True:
    country = input("Type the country name. ")
    capital = input("Type the capital name. ")
    world_dictionary[country] = capital

    # for capital in world_dictionary :
    #     print(capital)
    
    # for country in world_dictionary.values() :
    #      print(country)
    
    # for country in world_dictionary.items() :
    #     print(f"{country}: {capital}")
                                            
    print(world_dictionary)