#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    racine_carré = math.sqrt (a)
    return racine_carré


def square(a: float) -> float:
    carré = math.pow(a,2)
    return carré


def average(a: float, b: float, c: float) -> float:
    liste = [a,b,c]
    moyenne = sum(liste)/len(liste)
    return moyenne


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    minutes_à_degrés = angle_mins/60
    secondes_à_degrés = angle_secs/3600
    degré = angle_degs+minutes_à_degrés+secondes_à_degrés
    angle_radian = (degré*math.pi)/180
    return angle_radian


def to_degrees(angle_rads: float) -> tuple:
    radian_à_degré = (180*angle_rads)/math.pi
    degré = radian_à_degré//1
    reste_degré = radian_à_degré%1
    reste_en_minute = reste_degré*60
    minute = reste_en_minute//1
    reste_minute = reste_en_minute%1
    seconde = reste_minute*60

    return int(degré),int(minute),seconde


def to_celsius(temperature: float) -> float:
    température_celsius = (temperature-32)/1.8
    return température_celsius


def to_farenheit(temperature: float) -> float:
    température_fahrenheit = (temperature * 1.8) + 32
    return température_fahrenheit


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 180 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
