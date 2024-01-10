import math
import numpy as np
import matplotlib.pyplot as plt


def calc_min_velocity(radius, mu, phi: float) -> float:
    return math.sqrt(radius * 9.81 * (1 + abs(math.cos(phi)) * (1 + mu)))


def show_trajectory(radius, phi, velocity_start: float):
    # длина дуги по которой мы пройдем
    duga_length = math.pi * radius * (math.degrees(phi) / 180)

    X = np.array([])
    # выбрал удобный дискретный шаг
    discret_time = 0.1
    for i in np.arange(0, duga_length / velocity_start, discret_time):
        """
        Вывод формулы
        Мы (грубо говоря) бросаем наше тело с некоторой скорость v под углом a с высоты h
        Значит координата X в каждый момент времени будет равно
        X = v * cos(a) * t
        """
        X = np.append(X, velocity_start * math.cos(phi) * i)

    Y = np.array([])
    for i in np.arange(0, duga_length / velocity_start, discret_time):
        """
        Вывод формулы
        Мы (грубо говоря) бросаем наше тело с некоторой скорость v под углом a с высоты h
        Значит координата Y в каждый момент времени будет равно
        Y = v * sin(a) * t - g * t ^ 2 / 2
        """
        Y = np.append(Y, velocity_start * math.sin(phi) * i - 9.81 * i * i / 2)

    plt.plot(X, Y)
    plt.xlabel("Изменение по X")
    plt.ylabel("Изменение по Y")
    plt.text(
        -5, 3.1,
        "$v_{min}=$" + f"{velocity_start}м/с",
        fontsize=16,
        bbox=dict(facecolor='red', alpha=0.5)
    )
    plt.show()


def main():
    radius = 5
    phi = math.pi / 2 + math.pi / 6
    mu = 0.01

    velocity = calc_min_velocity(radius, mu, phi)
    print(velocity)

    show_trajectory(radius, phi, velocity)


if __name__ == '__main__':
    main()
