group_a = {'Ana', 'Marcos', 'Carlos', 'Mario'}
group_b = {'Ana', 'Pedro', 'Carlos', 'Antonio'}
group_c = {'Ana', 'Antonio', 'Marcos', 'Pepe'}
all_students = group_a.union(group_b).union(group_c)

 for student in all_students:
     groups_in = []
     for letter, group in zip('ABC', [group_a, group_b, group_c]):
         if student in group:
             groups_in.append(letter)
     groups_str = '-'.join(groups_in)
     plural = 's' if len(groups_in) > 1 else ''
     print(f'{student} en grupo{plural}: {groups_str}')