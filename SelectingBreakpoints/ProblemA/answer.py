import heapq

n = int(input("Quantidade de atividades: "))
availableGrades = list(map(int, input("Nota das atividades: ").strip().split()))

heapq._heapify_max(availableGrades)
min = 50
grade = 0


print(f'Nota atual + Nota da atividade')
while(grade < min):
  tempGrade = heapq._heappop_max(availableGrades)
  if(grade <= min):
    print(f'{grade} + {tempGrade}')
    grade += tempGrade

print(f'Nota Final: {grade}')
