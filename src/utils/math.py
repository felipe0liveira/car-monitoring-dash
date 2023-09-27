def remap_value(number, minRange, maxRange, newMinRange, newMaxRange):
    if number < minRange:
        number = minRange
    elif number > maxRange:
        number = maxRange

    percentage = (number - minRange) / (maxRange - minRange)

    newValue = newMinRange + (percentage * (newMaxRange - newMinRange))

    return newValue
