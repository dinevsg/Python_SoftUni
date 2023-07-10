length = int(input())
width = int(input())
height = int(input())
percent_acc = float(input())

volume = length * width * height
total_volume = volume / 1000
acc_volume = total_volume * (percent_acc / 100)
result = total_volume - acc_volume

print(result)
