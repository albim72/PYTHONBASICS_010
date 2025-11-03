# Legacy version — intentionally messy
def process_data(data):
    result = []
    for i in range(len(data)):
        if data[i] != None:
            val = data[i]
            if val > 0:
                result.append(val * 2)
            else:
                result.append(0)
    print("Result:")
    for r in result:
        print(r)
    return result

values = [5, -3, None, 7, 0]
process_data(values)
