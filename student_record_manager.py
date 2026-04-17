def get_roll_nos(data:list,criteria = None):
    average = sum(marks for _, marks in data) / len(data)
    print(average)
    if criteria == "above_average":
        return [roll for roll, marks in data if marks >= average]

    elif criteria == "below_average":
        return [roll for roll, marks in data if marks < average]

    elif criteria == "fail":
        return [roll for roll, marks in data if marks < 40]

    elif criteria == "toppers":
        return [roll for roll, marks in data if marks > 90]

    elif criteria is None:
        return [roll for roll, _ in data]

    else:
        return []

#sample data  
data = [('101',85), ('102',75), ('103',45),('104',95),('105',35)]
print(get_roll_nos(data,'above_average'))
print(get_roll_nos(data,'below_average'))
print(get_roll_nos(data,'fail'))
print(get_roll_nos(data,'toppers'))
print(get_roll_nos(data,None))
