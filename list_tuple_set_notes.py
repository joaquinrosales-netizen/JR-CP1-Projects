# JR, lists tuples and sets

siblings = ["Alex","Katie","Andrew","Tia","Treyson","Xavier","Jake","Quandale dingle"]
print(f"My older brother is {siblings[0]}")
print(*siblings)
print(f"The youngest is {siblings[-1]}")
siblings.append("Jayshree")
siblings.insert(3, "Vienna")
siblings.extend(["Joe", "Isreal", "Zee"])
siblings.remove("Vienna")
siblings.pop(0)
print(*siblings)

subjects = ("CP1", "CP2", "Advanced CP", "CSP", "Utah studies" , "US 1", "US 2", "World Civ", "World Geography", "CCA buisness")
print(subjects[0])
print(*subjects)

#sets
visited = {"Texas", "Ohio", "Minnesota", "Virginia", "D.C.", "Utah", "California", "Nevada",}
           
print(*visited)
print(len(visited))
visited.add("Idaho")
print(*visited)
visited.update({"Montana", "Arizona", "Oklahoma", "New Mexico"})
print(*visited)
visited.remove("Arizona")
print(*visited)