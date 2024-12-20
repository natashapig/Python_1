"""Написать программу, которая читая символы из файла, распознает, преобразует и 
выводит на экран объекты по определенному правилу. Объекты разделены пробелами. 
Распознавание и преобразование делать по возможности через регулярные выражения. Для
упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.
Целые числа, начинающиеся с нечетных цифр. Четные цифры выводить словами."""
import re
d={
    '0':'ноль',
    '2':'два',
    '4':'четыре',
    '6':'шесть',
    '8':'восемь',
}
f=open("3.txt", 'r')
s = f.readline()
while s!='':
    objects = s.split()
    for obj in objects:
        match = re.match(r"^-?[13579]\d*$", obj)
        if match:
            for key in d:
                obj = obj.replace(key,d[key])
            print(obj, end=" ")      
    s=f.readline()