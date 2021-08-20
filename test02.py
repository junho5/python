def calculate_change(payment, cost):
    charge = payment - cost
    
    fifty = (charge-(charge%50000))/50000
    charge -= fifty*50000
    print("50000원 지폐: {:.0f}장".format(fifty))
    
    onemill = (charge-(charge%10000))/10000
    charge -= onemill*10000
    print("10000원 지폐: {:.0f}장".format(onemill))
    
    five = (charge-(charge%5000))/5000
    charge -= five*5000
    print("5000원 지폐: {:.0f}장".format(five))
    
    thousand = (charge-(charge%1000))/1000
    charge -= thousand*1000
    print("1000원 지폐: {:.0f}장".format(thousand))
    


# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)