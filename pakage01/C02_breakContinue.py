# break
#   - 만나면 해당 반복문을 탈출한다

# continue
#   - 만나면 해당 반복문을 1회 스킵한다

for i in range(1, 11):
    print(i, end=' ')

    if i == 7:
        break
print()

for i in range(1, 11):
    if i == 7:
        continue
    print(i, end=' ')

print()