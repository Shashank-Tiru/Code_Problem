from operator import itemgetter

def avg_temp():
    n = int(input("Number of inputs: "))
    val = [] #Stores Sensor_id, time, temp
    time_temp = [] #stores time, temp
    avg_val_10999 = avg_val_11999 = avg_val_12999 = avg_val_13999 = 0
    count_1 = count_2 = count_3 = count_4 = 0
    for i in range(0, n):
        val.append((input().split(",")))
    # print(val)
    for i in val:
        time_temp.append([i[1], i[2]])
    # print("time_temp: ", sorted(time_temp))
    l = len(time_temp)
    for i in time_temp:
        if 10000 <= int(i[0]) <= 10999:
            count_1 += 1
            avg_val_10999 += int(i[1])
        if 11000 <= int(i[0]) <= 11999:
            count_2 += 1
            avg_val_11999 += int(i[1])
        if 12000 <= int(i[0]) <= 12999:
            count_3 += 1
            avg_val_12999 += int(i[1])
        if 13000 <= int(i[0]) <= 13999:
            count_4 += 1
            avg_val_13999 += int(i[1])
    print("10000-10999: ", avg_val_10999/count_1)
    print("11000-11999: ", avg_val_11999/count_2)
    print("12000-12999: ", avg_val_12999/count_3)
    print("13000-13999: ", avg_val_13999/count_4)

avg_temp()