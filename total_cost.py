tiсket_count = int(input("Ведите количество билетов: "))
total_cost = 0
discount = 0
for i in range(tiсket_count):
    age = int(input(f"Ведите возраст посетителя{i+1}: "))
    if age < 18:

        continue
    elif 18 <= age < 25:
        total_cost += 900
    else:
        total_cost += 1390

if tiсket_count > 3:
    discount = 0.1 * total_cost

total_cost -= discount

print(f"сума к оплате {total_cost} руб.")
