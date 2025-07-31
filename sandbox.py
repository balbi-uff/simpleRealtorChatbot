from realtor import RealtorBot

realtor = RealtorBot()

realtor.intro_message()
result = False

while not result:
    input_from_user = input("\n>>")
    result = realtor.fetch_building_information(input_from_user)

realtor.print_registered_buildings()

