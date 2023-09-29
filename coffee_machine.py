def calculate():
    pass

def check_resources(res:dict, flavor:str):
    if flavor=="espresso":
        if res["water"]>50 and res['coffee']>18:
            return True

        else:
            return False
        
    if flavor=="latte":
        if res['water']>200 and res["coffee"]>24 and res["milk"]>150:
            return True

        else:
            return False
        
    if flavor=="cappuccino":
        if res['water']>250 and res["coffee"]>24 and res["milk"]>100:
            return True
        
        else:
            return False
    