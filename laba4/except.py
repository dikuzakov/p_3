try:
    print(239 / 0)
except ZeroDivisionError as e:
    print("на ноль делить нельзя!")
finally:
    print("конец кода")

