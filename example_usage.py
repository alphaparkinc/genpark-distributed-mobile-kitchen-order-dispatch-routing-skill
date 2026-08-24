from client import DistributedMobileKitchenOrderDispatchRoutingClient

def main():
    client = DistributedMobileKitchenOrderDispatchRoutingClient()
    res = client.dispatch_mobile_restaurant_truck('Santa Monica, CA')
    print('Mobile Kitchen: ' + res['mobile_kitchen_unit'] + ' | Prep Time: ' + str(res['onboard_prep_time_mins']) + ' mins')
    print('Cook-to-Door ETA: ' + str(res['curbside_cook_to_door_mins']) + ' mins @ ' + str(res['food_freshness_temperature_celsius']) + 'C')
    print('Chef Grade Assured: ' + str(res['chef_grade_quality_assured']))

if __name__ == '__main__':
    main()
