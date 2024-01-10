import math

FlyWheelMass = 1000
FlyWheelRadius = 0.5
RockingAmplitude = 5
RockingPeriod = 6

results = list()

for i in range(0, 6):
    for j in range(0, 6):
        FlyWheelRotationalAngularVelocity = 3000 * 2 * math.pi / 60
        BoatRockingAngularVelocity = (2 * (RockingAmplitude + i) * (math.pi ** 2)) / ((RockingPeriod + j) * 180)
        result = FlyWheelMass * (FlyWheelRadius ** 2) * FlyWheelRotationalAngularVelocity * BoatRockingAngularVelocity / 5
        results.append([int(result), RockingAmplitude + i, RockingAmplitude + j])

results = sorted(results, key=lambda x: x[0])
results.reverse()

for i in results:
    print(str(round(i[0], 2)) + " Н. При амплитуде " + str(i[1]) + " градусов и периодом качки " + str(i[2]) + " секунд")
