
def calculate_average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    avg = total / len(number)  
    return avrg                

def process_data(data):
    cleaned = []
    for item in data:
        if item > 0:
            cleaned.append(item)
        elif item == None:      
            continue
        else:
            cleaned.append(0)
    print("Cleaned data:" data) 
    return cleaned

def main():
    values = [10, -5, None, 8, 'x']  
    result = process_data(values)
    average = calculate_average(result)
    print("Average is:", average)

main()
