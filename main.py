import math

GRADE = {}

for score in range(0, 101):
  if score < 40:
    GRADE[score] = "U"
  elif score < 45 and score >= 40:
    GRADE[score] = "S"
  elif score < 50 and score >= 45:
    GRADE[score] = "E"
  elif score < 55 and score >= 50:
    GRADE[score] = "D"
  elif score < 60 and score >= 55:
    GRADE[score] = "C"
  elif score < 70 and score >= 60:
    GRADE[score] = "B"
  else:
    GRADE[score] = "A"

def read_testscores(filename):
  data_list = []
  with open(filename, "r") as file:
    header = file.readline().strip().split(",")
    for line in file:
      if len(line) != 0:
        row_dict = {}
        row = line.strip().split(",")
        row_dict["class"] = row[0]
        row_dict["name"] = row[1]
        overall = math.ceil((int(row[2])/30 * 15) +         
                            (int(row[3])/40 * 30) + 
                            (int(row[4])/80 * 35) + 
                            (int(row[5])/30 * 20))
                   
        row_dict["overall"] = overall
        row_dict["grade"] = GRADE.get(overall)
        data_list.append(row_dict)
    return data_list

def analyze_grades(studentdata):
  classes = {}
  for dict in studentdata:
    if classes.get(dict.get("class")) == None:
      classes[dict.get("class")] = {}
      
  for class_ in classes.keys():
    gradec = {}
    A, B, C, D, E, S, U = 0, 0, 0, 0, 0, 0, 0
    for dict in studentdata:
      if dict.get("class") == class_:
        if dict.get("grade") == "A":
          A += 1
        elif dict.get("grade") == "B":
          B += 1
        elif dict.get("grade") == "C":
          C += 1
        elif dict.get("grade") == "D":
          D += 1
        elif dict.get("grade") == "E":
          E += 1
        elif dict.get("grade") == "S":
          S += 1
        else:
          U += 1
          
    gradec["A"] = A
    gradec["B"] = B
    gradec["C"] = C
    gradec["D"] = D
    gradec["E"] = E
    gradec["S"] = S
    gradec["U"] = U
    classes.get(class_).update(gradec)
    
  return (classes)

        
        
    
      
    
      
    

    
    

